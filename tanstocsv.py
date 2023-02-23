import csv
def get_data_frame(last_data):
    # 定义列标题和数据
    header = ['学校', '考试方式', '院系所', '专业', '学习方式', '研究方向', '指导教师',
            '拟招生人数', '备注', '政治', '外语', '业务课1', '业务课2']

    # data = [['1','2','3','4','5','6','7','8','9','10','11','12','13'],
    #         ['1','2','3','4','5','6','7','8','9','10','11','12','13'],
    #         ['1','2','3','4','5','6','7','8','9','10','11','12','13']]

    # 打开csv文件并写入数据
    with open('output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # 写入列标题
        writer.writerow(header)
        
        # 逐行写入数据
        # for row in data:
        for row in last_data:
            writer.writerow(row)
    csvname = "所有专业原始数据.csv"
        #重复行清理
    clean_csv(csvname)
    return csvname #返回字符串
