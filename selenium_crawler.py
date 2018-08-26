from selenium import webdriver
import csv
from selenium.webdriver.common.by import By
import time

chrome_path = r"C:\Users\baoo\Desktop\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
url = "https://www.foody.vn/"
driver.get(url)
file_name = 'a.txt'
with open(file_name,'w',encoding='utf-8') as f:
    f.write("ID , Reviews\n")
    id_review = 1
    page_count = 1
    while (page_count != 0):

        # xpath = """//*[@id="ajaxRequestDiv"]/div/div[2]/div[""" + str(page_count) + "]/div[2]/div[2]/a"

        xpath = """//*[@id="ajaxRequestDiv"]/div/div[2]/div[""" + str(page_count) + "]/div[2]/div/a"
        link = driver.find_element_by_xpath(xpath)


        child_url = str(link.get_attribute("href"))
        driver.get(child_url)

        time.sleep(1)
        find_option = "//span[@ng-bind-html='Model.Description']"
        element = driver.find_elements_by_xpath(find_option)
        print(child_url)
        # while (review_count < 6)
         # current_url = driver.current_url
        i = 0
        for e in element:
            print(i+1 , " : ", e.text +"\n")
            #line = str(id_review + 1)+ " , " +
            f.write(str(id_review)+","+e.text+"\n")
            id_review = id_review +1

   # rxpath =
        driver.get(url)
        page_count = page_count + 1
    
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[1]/div[2]/div[2]/a
#driver.find_element_by_xpath("""//*[@id="ajaxRequestDiv"]/div/div[2]/div[1]/div[2]/div[2]""").click()
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[2]/div[2]/div[2]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[1]/div[2]/div[2]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[2]/div[1]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[2]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[3]
#/*[@id="ajaxRequestDiv"]/div/div[2]/div[3]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[4]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[5]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[6]
#//*[@id="ajaxRequestDiv"]/div/div[2]/div[72]