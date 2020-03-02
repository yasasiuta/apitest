import requests

class common(object):

    def __init__(self):
        self.url = 'http://www.zoomwell.cn/clbs'


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
    cookies = {
        'JSESSIONID': 'EDCAFE2FB5B838A7426CE6776B7FAEF3'
    }

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
    req_result = requests.post(req_url, data, cookies=cookies)

    print(req_result.json())


    req_url1 = 'http://www.zoomwell.cn/clbs/m/basicinfo/equipment/rodsensor/repetition'

    data = {
        'sensorNumber':'SAE-112',
        'username':'SAE-112'
    }

    req_result1 = requests.post(req_url1, data, cookies=cookies )
    req_result1.token
    print(req_result1.json())

    #删除温度传感器


    # requests.get('http://www.zoomwell.cn/clbs/getCaptchaString?date=1582705346064', params= '1582705346064')




