import requests
import json
class common(object):

    def __init__(self):
        self.url = 'http://192.168.24.142:8080/clbs/j_spring_security_check'


    '''
    定义get方法
    
    '''
    def get(self, url, param = ''):
        url = self.url + url + param
        res = requests.get(url)
        return res

    '''
    定义post方法
    '''

    def post(self, url, param = ''):
        url = self.url + url + param
        res = requests.post(url)
        return res






if __name__ == '__main__':
    session = requests.session()
    login_url = 'http://192.168.24.142:8080/clbs/j_spring_security_check'
    data1 = 'username=jiangtianshi&key=&password=000000&captchaCode='
    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'

    }
    req = session.post(login_url, data1, header)
    json1 = req.text
    dic = json.loads(json1)
    token = dic['Cookie']
    print(token)

    # 新增温度传感器
    req_url = 'http://www.zoomwell.cn/clbs/v/TransduserMgt/add'
    # headers
    data = {
        'sensorNumber' : 199,
        'filterFactor' : 2,
        'compensate' : 2,
        'remark' : '231323423423',
        'sensorType' : 1

    }
    req_result = requests.post(req_url, data, cookies=token)

    print(req_result.json())


    req_url1 = 'http://www.zoomwell.cn/clbs/m/basicinfo/equipment/rodsensor/repetition'

    data = {
        'sensorNumber':'SAE-112',
        'username':'SAE-112'
    }

    req_result1 = requests.post(req_url1, data, cookies=token )
    req_result1.token
    print(req_result1.json())

    #删除温度传感器


    # requests.get('http://www.zoomwell.cn/clbs/getCaptchaString?date=1582705346064', params= '1582705346064')




