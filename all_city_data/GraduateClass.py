import copy
import requests
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
import re
import time
import lxml
import pandas as pd
import csv
class Graduate:
    def __init__(self, province, category, provinceName):

        self.head = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKi"
            "t/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
        }
        self.data = []
        self.province = province
        self.category = category
        self.provinceName = provinceName
# 第一步，输入省市、学科代码，获取学校urls
    def get_school_url(self):
        url = "https://yz.chsi.com.cn/zsml/queryAction.do"
        data = {
            "ssdm": self.province,
            "yjxkdm": self.category,
            # "dwmc":self.schoolname,
        }
        response = requests.post(url, data=data, headers=self.head)
        html = response.text
        reg = re.compile(r'(<tr>.*? </tr>)', re.S)
        content = re.findall(reg, html)
        schools_url = re.findall('<a href="(.*?)" target="_blank">.*?</a>',
                                str(content))
        return schools_url
    #获得地区、代码、学校确定下的学院url
    def get_college_data(self, url):
        response = requests.get(url, headers=self.head)
        html = response.text
        colleges_url = re.findall(
            '<td class="ch-table-center"><a href="(.*?)" target="_blank">查看</a>',
            html)
        return colleges_url
    
    #获取地区、专业、学校、学院下的信息
    def get_final_data(self, url):
        temp = []
        response = requests.get(url, headers=self.head)
        html = response.text
        soup = BeautifulSoup(html, features='lxml')
        summary = soup.find_all('td', {"class": "zsml-summary"})
        for x in summary:
            temp.append(x.get_text())
        summary = soup.find_all('span', {"class": "zsml-bz"})  #爬取备注
        temp.append(summary[1].get_text())
        html = html.replace("\r\n","")
        with open("爬取html.txt",'w',encoding='utf-8') as f:
            f.write(html)
            f.close()
        subjects = re.findall('<td>(.*?)<span class="sub-msg">',html,re.S)
        #保留前四个选项，没有添加比如俄语这样的选择
        for i,sub in enumerate(subjects): 
            if i == 4:
                break
            temp.append(sub)
        self.data.append(temp)
        
    #获取学校数据,调用getfinal
    def get_schools_data(self):
        url = "http://yz.chsi.com.cn"
        schools_url = self.get_school_url() #填入获取的学校urls
        amount = len(schools_url)
        i = 0
        for school_url in schools_url:
            i += 1
            page = 1
            temp = []
            while True:
                url_ = url + school_url + '&pageno={}'.format(page) # 将研招网网址url+学校url+page 组合成学校页url_
                colleges_url = self.get_college_data(url_) #获得地区、专业、学校下的所有学院url
                if colleges_url not in temp:
                    print('收集第{}页信息'.format(page))
                    temp.append(colleges_url)
                    page += 1
                    for college_url in colleges_url:
                        _url = url + college_url
                        self.get_final_data(_url)
                else:
                    break
            print("已完成" + self.provinceName + "第" + str(i) + "/" +
                  str(amount) + "个高校爬取")                  
#将数据输出为固定格式的excel
def get_data_frame(last_data,saveprovincename):
    # 定义列标题和数据
    csvname = saveprovincename + '_rawdata' + ".csv"
    # print(csvname)
    header = ['学校', '考试方式', '院系所', '专业', '学习方式', '研究方向', '指导教师',
            '拟招生人数', '备注', '政治', '外语', '业务课1', '业务课2']
    # 打开csv文件并写入数据
    with open(csvname, mode='w', newline='') as file:
        writer = csv.writer(file)
        # 写入列标题
        writer.writerow(header)
        # 逐行写入数据
        for row in last_data:
            writer.writerow(row)
    #删除不用列
    del_colum(csvname)
    #清理重复行
    # clean_csv(csvname)
    return csvname #返回字符串
    
#删除不用的列,并将研究方向改为不区分方向
def del_colum(csvname):   
    # 读取 CSV 文件
    with open(csvname, 'r') as input_file:
        reader = csv.reader(input_file)
        header = next(reader)  # 读取列标题
        #替换“不区分方向”
        rows = list(reader)
        for row in rows:
            row[5] = "不区分方向" 
        # rows = [row for row in reader]  # 读取数据行
    # 删除指定列
    cols_to_remove = [4,6,7,8]  # 要删除的列的索引，从0开始
    header = [header[i] for i in range(len(header)) if i not in cols_to_remove]  # 删除列标题
    rows = [[row[i] for i in range(len(row)) if i not in cols_to_remove] for row in rows]  # 删除数据列
    # 写入CSV文件
    with open(csvname, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)  # 写入修改后的列标题
        writer.writerows(rows)  # 写入修改后的数据行
    

# #清理重复行
# def clean_csv(cleaning_file_name):
#     df = pd.read_csv(cleaning_file_name,encoding='gbk')
#     # df.loc[1:, colum_name] = '不区分方向'
#     # df.iloc[:, 4] = '不区分方向'
#     df.drop_duplicates(inplace=True)
#     df.to_csv(cleaning_file_name, index=False)
    
