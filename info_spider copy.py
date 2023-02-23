import time
from GraduateClass import Graduate,get_data_frame
from copypasteexcel import copy_paste_excel_columns
from excel2dict import excel2dict
n = range(1,5)
if __name__ == '__main__':
    ##################################
    ##################################
    # categories = ["0855","0831","0777","1001","1009","0811","0810","0804","0802","0805","0823","1202","1201"] # 北航专业代码
    # category = ["0807","0701"]
    # categories = ["0777","0831","0855"]
    # schoolname = '北京航空航天大学'
    savepath = r'C:\Users\lenovo\Desktop\BCI APPLICATION\webProj\item\yzw_spider\所有数据'
    last_data = []
    # savepath = r'C:\Users\lenovo\Desktop\勤思2023\spider_fromcuiqingcai\yzw_spider\所有数据'
   
    provinceNmaeDict = {
    '11': '北京市',
    # '37': '山东省',
    # '22': '吉林省',
    # '12': '天津市',
    # '13': '河北省',
    # '14': '山西省',
    # '15': '内蒙古自治区',
    # '21': '辽宁省',
    # '23': '黑龙江省',
    # '31': '上海市',
    # '32': '江苏省',
    # '33': '浙江省',
    # '34': '安徽省',
    # '35': '福建省',
    # '36': '江西省',
    # '41': '河南省',
    # '42': '湖北省',
    # '43': '湖南省',
    # '44': '广东省',
    # '45': '广西壮族自治区',
    # '46': '海南省',
    # '50': '重庆市',
    # '51': '四川省',
    # '52': '贵州省',
    # '53': '云南省',
    # '54': '西藏自治区',
    # '61': '陕西省',
    # '62': '甘肃省',
    # '63': '青海省',
    # '64': '宁夏回族自治区',
    # '65': '新疆维吾尔自治区',
    # '71': '台湾省',
    # '81': '香港特别行政区',
    # '82': '澳门特别行政区'
    }
    ##################################
    ##################################
    for i in list(provinceNmaeDict.keys()): #将keys转化为列表
        dicts = excel2dict()
        print(type(dicts))
        for key in dicts:
            for category in dicts[key]:
        # for category in categories:
                province = i
                if province in provinceNmaeDict.keys():
                    spyder = Graduate(province, category, provinceNmaeDict[province],key)
                    spyder.get_schools_data()
                    # spyder2 = Graduate(province, category, provinceNmaeDict[province],schoolname)
                    # B = spyder.get_final_data()
                    last_data.extend(spyder.data)
                    # print(last_data)
        openfilename = get_data_frame(last_data) 
        time.sleep(1) # 延迟时间1s
                 
for i in n:
    copy_paste_excel_columns(openfilename,i,savepath) 

