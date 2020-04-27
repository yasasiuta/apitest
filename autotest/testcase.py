#coding: utf-8
import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

class BaseModule(unittest.TestCase):
    def setUp(self):
        self.wb = webdriver.Chrome(r'D:\webdriver\chromedriver')
        self.wb.get('http://192.168.24.143:8080/clbs/login')
        self.wb.implicitly_wait(3)
        username = self.wb.find_element_by_id('email')
        username.send_keys('jiangtianshi')
        self.wb.implicitly_wait(3)
        password = self.wb.find_element_by_id('tg_password')
        password.send_keys('000000')
        login = self.wb.find_element_by_id('login_ok')
        login.click()
        self.wb.implicitly_wait(3)
    def tearDown(self):
        time.sleep(5)
        self.wb.close()

    def test_1_addtempsensor(self):
        # 进入应用管理
        application_management = self.wb.find_element_by_id('9f5ea704-6a90-11e6-8b77-86f30ca893d3')
        application_management.click()
        self.wb.implicitly_wait(3)
        # 温度传感器管理
        temp = self.wb.find_element_by_id('32e16952-622b-11e7-907b-a6006ad3dba0')
        temp.click()
        self.wb.implicitly_wait(3)
        temp_mage = self.wb.find_element_by_id('3d128b3a-622c-11e7-907b-a6006ad3dba0')
        temp_mage.click()
        self.wb.implicitly_wait(3)
        operation_meau = self.wb.find_element_by_id('dropdownMenu1')
        operation_meau.click()
        self.wb.implicitly_wait(3)
        addid = self.wb.find_element_by_id('addId')
        addid.click()
        self.wb.implicitly_wait(3)
        sensornumber = self.wb.find_element_by_css_selector('[id="sensorNumber"]')
        sensornumber.send_keys(u"自动新增1" )
        self.wb.implicitly_wait(3)
        filterFactor = self.wb.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/div[2]/div/select')
        Select(filterFactor).select_by_index(1)
        self.wb.implicitly_wait(3)
        compensate = self.wb.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/div[3]/div/select')
        Select(compensate).select_by_index(0)
        remark = self.wb.find_element_by_css_selector('[name="remark"]')
        remark.send_keys(u"自动")
        self.wb.implicitly_wait(3)
        doSubmitsAdd = self.wb.find_element_by_id('doSubmitsAdd')
        doSubmitsAdd.click()
        element = self.wb.find_elements_by_css_selector('td')
        print (element)
        sen = self.wb.find_element_by_css_selector('tr.odd:nth-child(1) > td:nth-child(4)')
        print (sen)
        self.assertIn('自动新增1',sen,msg='新增失敗')

    def test_2_deletesensor(self):
        # 进入应用管理
        application_management = self.wb.find_element_by_id('9f5ea704-6a90-11e6-8b77-86f30ca893d3')
        application_management.click()
        self.wb.implicitly_wait(3)
        # 温度传感器管理
        temp = self.wb.find_element_by_id('32e16952-622b-11e7-907b-a6006ad3dba0')
        temp.click()
        self.wb.implicitly_wait(3)
        temp_mage = self.wb.find_element_by_id('3d128b3a-622c-11e7-907b-a6006ad3dba0')
        temp_mage.click()
        self.wb.implicitly_wait(3)

