from time import sleep
from selenium import webdriver

d=webdriver.Chrome()
d.get('http://google.com')
search_bx=d.find_element_by_name('q')
search_bx.send_keys('invaana\n')
index=0
res=[]
urls=d.find_elements_by_css_selector('h3.r a')
while index<= 12:
    next_page=d.find_element_by_css_selector('#pnnext')
    next_page.click()
    sleep(5)
    urls=d.find_elements_by_css_selector('h3.r a')
    for l in urls:
        res.append(l.get_attribute('href'))
        l.get_attribute('href')
    index=index+1
    sleep(2)

print(res)
for i in res:
    body = d.get(i)
    body = d.find_element_by_tag_name('body')
    print(body.text)

