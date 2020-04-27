import requests
import json

'''
根据用例中的method来判断请求方式，执行对应的接口请求
'''

class http_request():
    def __init__(self):
        self.session = requests.session()
        login_url = 'http://192.168.24.142:8080/clbs/j_spring_security_check'
        data1 = 'username=jiangtianshi&key=&password=000000&captchaCode='
        header = {
            'Content-Type':'application/x-www-form-urlencoded',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

        }
        req = self.session.post(login_url,data1,header)
        json1 = req.text
        dic = json.loads(json1)
        token = dic['Cookie']
        print(token)



    def get_request(self, url):
        result = requests.get(url=url)
        return result



    def post_request(self, url):
        result = requests.post(url=url)
        result = result.json()
        return result

    def chose_request(self, method, url, data):
        result = ''
        if method == 'post':
            result = self.post_request(url, data)
        elif method == 'get':
            result = self.get_request(url, data)
        else:
            print("method错误！")
        return result









# if __name__ =="__main__":
#
#     login_url = 'http://192.168.24.142:8080/clbs/j_spring_security_check'
#     login_data = {
#         'username': 'jiangtianshi',
#         'password': '0000000'
#     }
#     s = requests.session()
#     r = requests.post(url= login_url, data = login_data)
#
#     jsession = r.headers['Cookie']
#     print(jsession)



    # req_url = 'http://www.zoomwell.cn/clbs/v/TransduserMgt/add'
    # data = 'sensorNumber=7878&filterFactor=2&compensate=1&remark=&sensorType=1'
    # req_result = post_request(req_url, data, cookies)
    # print(req_result)

