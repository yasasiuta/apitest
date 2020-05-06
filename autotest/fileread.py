import xlrd
import xml.dom.minidom
import yaml
'''
excel文件读取
'''



class read_file():
    def read_excel(filepath,sheetname):
        data1 = []
        get_excel = xlrd.open_workbook(filepath) #获取excel文件并打开
        get_sheet = get_excel.sheet_by_name(sheetname)#找到对应页签
        nrows = get_sheet.nrows #获取行数
        ncols = get_sheet.ncols #获取列数
        print(nrows,ncols)
        for i in (1,nrows-1):
            data1.append(get_sheet.row_values(i))
        print(data1)

    def read_xml(filename):
        dom = xml.dom.minidom.parse(filename)
        print(dom)
        rootdata = dom.documentElement
        print(rootdata)
        data = dom.getElementsByTagName("y")
        print(data[0])

    def read_yml(filename):
        with open(filename, 'r',encoding="utf-8") as f:
            print(yaml.load(f.read(), Loader=yaml.Loader))










if __name__ == '__main__':
    # filepath = r"C:\Users\zwkj\Downloads\test1.xls"
    # sheetname = 'Export'
    # read_file.read_excel(filepath,sheetname)
    # read_file.read_xml('test77.xml')
    read_file.read_yml('sensorname.yaml')






