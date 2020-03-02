import xlrd

'''
读取接口测试用例excel
'''

class read_excel():

    def get_excel(filepath, sheetname):
        cls = []
        get_excel = xlrd.open_workbook(filepath) #打开excle
        get_sheet = get_excel.sheet_by_name(sheetname)#找到对应的表
        nrows = get_sheet.nrows#获取表的行数
        for i in range(1,nrows):
            # if get_sheet.row_values(i)[0] != u'case_name':#表头字段不获取
            cls.append(get_sheet.row_values(i))
        return cls

    def nrows(filepath, sheetname):
        get_excel = xlrd.open_workbook(filepath)  # 打开excle
        get_sheet = get_excel.sheet_by_name(sheetname)  # 找到对应的表
        nrows = get_sheet.nrows  # 获取表的行数
        return nrows







if __name__ == "__main__":
    # al = read_excel().get_excle(r'E:\apitest\config\apitest.xlsx', 'test')
    print(read_excel().get_excle(r'E:\apitest\config\apitest.xlsx', 'test')[1][2])
