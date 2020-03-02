from common.read_excel import read_excel
from common.http_request import http_request



path = r'E:\apitest\config\apitest.xlsx'
cookies = {
        'JSESSIONID': '73675862C2B2FD40BB44197C25DE1978'
    }
for i in range(0,read_excel.nrows(path, 'test')-1):  #遍历执行test.xlsx的接口用例
    req_url = read_excel.get_excel(path,'test')[i][1]
    data = read_excel.get_excel(path,'test')[i][2]
    method = read_excel.get_excel(path, 'test')[i][3]
    req_reslut = http_request.post_request(method, req_url, data)
    print(req_reslut)

