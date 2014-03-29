__author__ = 'prashanthp'
from splinter import Browser

class Vipdatabase():
    driver = Browser('firefox')
    #navigate to webpage
    driver.visit('http://www.ranorex.com/web-testing-examples/vip/')

    def test_add_name(self):
        driver =Browser('firefox')
        #navigate to webpage
        driver.visit('http://www.ranorex.com/web-testing-examples/vip/')
        #enter First name
        driver.find_by_xpath('//*[@id="'"FirstName"'"]').fill('Prasanth')
        #Enter Last name
        driver.find_by_xpath('//*[@id="'"LastName"'"]').fill('Patil')
        #Selecting the category
        driver.select_id('Category','Music')
        driver.choose('Gender','male')
        driver.find_by_xpath('//*[@id="'"Add"'"]').click()

    #def test_load(self):
        driver.find_by_xpath('//*[@id="'"Load"'"]').click()

    #def test_save(self):
        driver.find_by_xpath('//*[@id="'"Save"'"]').click()
        #switching to window
