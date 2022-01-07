from selenium import webdriver
import time
import pandas

URL = "https://www.careerguide.com/career-options"

#setting up selenium chrome driver
chrome_driver_path = "E:\\Python\\Selenium\\chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_driver_path)

driver.get(URL)

time.sleep(10)

#------------------------------------Part1----------------------------


data = {"cat":'', "subCategory": []}
data_list =[]

#Getting the categories and subcategories
divs = driver.find_elements_by_class_name('col-md-4')

for div in divs:
    
    category = div.find_elements_by_tag_name('h2')
    for item in category:
        data["cat"] = item.text        

        
    ul_list = div.find_elements_by_class_name('c-theme')
    for item in ul_list:
        sub_category = item.find_elements_by_tag_name('li')

        subcat_list =[]
        for kitem in sub_category:
            subcat_list.append(kitem.text)
            
        data['subCategory'] = subcat_list
        
        data1 = data.copy()
        data_list.append(data1)


df = pandas.DataFrame(data_list)
df.to_csv('data.csv')

        
