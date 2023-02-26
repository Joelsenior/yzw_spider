import pandas as pd
def copy_paste_excel_columns(file_name,n,savepath,cityname):
    if n == 1:
    # 读取表格1中专业模板列数据
        df1 = pd.read_csv(file_name, usecols=[0,2,3,5,6,7,8],encoding='gbk')
        print(df1)
        # df1 = pd.read_csv(file_name, usecols=[0,2,3,5,6,7,8])
        df1.drop_duplicates(inplace=True)
        # 新建表格2，粘贴到表格2中A列和B列内容
        df2 = pd.DataFrame({'学校名称': df1.iloc[:, 0], '学院名称': df1.iloc[:, 1],'专业名称': df1.iloc[:, 2],'科目一': df1.iloc[:, 3],'科目二': df1.iloc[:, 4],'科目三': df1.iloc[:, 5],'科目四': df1.iloc[:, 6]})
        # 存储表格2
        savename =  savepath + cityname + '_专业模板' + '.xlsx'
        df2.to_excel(savename, index=False)
    if n == 2:
    # 读取表格1中方向模板列数据
        df1 = pd.read_csv(file_name, usecols=[0,2,3,4],encoding='gbk')
        df1.drop_duplicates(inplace=True)
        # 新建表格2，粘贴到表格2中A列和B列内容
        df2 = pd.DataFrame({'学校名称': df1.iloc[:, 0], '学院名称': df1.iloc[:, 1],'专业名称': df1.iloc[:, 2],'方向名称': df1.iloc[:, 3]})
        # df2 = pd.DataFrame({'学校名称': df1.iloc[:, 0], '学院名称': df1.iloc[:, 1],'专业名称': df1.iloc[:, 2]},'方向名称': df1.iloc[:, 3]})
        # 存储表格2
        savename = savepath + cityname +'_方向模板' + '.xlsx'
        df2.to_excel(savename, index=False) 
    if n == 3:
    # 读取表格1中学院模板列数据
        df1 = pd.read_csv(file_name, usecols=[0,2],encoding='gbk')
        df1.drop_duplicates(inplace=True)
        # 新建表格2，粘贴到表格2中A列和B列内容
        df2 = pd.DataFrame({'学校名称': df1.iloc[:, 0], '学院名称': df1.iloc[:, 1]})
        # 存储表格2
        savename = savepath + cityname +'_学院模板' + '.xlsx'
        df2.to_excel(savename, index=False)
    if n == 4:
    # 读取表格1中学校模板列数据
        df1 = pd.read_csv(file_name, usecols=[0],encoding='gbk')
        df1.drop_duplicates(inplace=True)
        # 新建表格2，粘贴到表格2中A列和B列内容
        df2 = pd.DataFrame({'学校名称': df1.iloc[:, 0]})
        # 存储表格2
        savename = savepath + cityname +'_学校模板' + '.xlsx'
        df2.to_excel(savename, index=False)