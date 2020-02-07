from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


driver = webdriver.Safari()
driver.get(url)
elem = driver.find_element_by_id('weblogin_netid')
elem.clear()
elem.send_keys(login)
q_types = ["recursive-tracing", "recursive-programming", "inheritance-polymorphism",
           "linkedlist-nodes", "arrayintlist-programming", "stacks-queues"]
time.sleep(1)
elem1 = driver.find_element_by_id('weblogin_password')
elem1.clear()

elem1.send_keys(pw)
elem.send_keys(Keys.ENTER)

time.sleep(2)
elem1 = driver.page_source
soup = BeautifulSoup(elem1, 'lxml')

links = []
for a in soup.find_all('a', href=True):
    links.append(a['href'])

print(links)


temp = q_types[0]
count = 1
q_types.pop(0)
links.pop(0)

for cur in links:
    if "collapse" not in cur:
        driver.get(cur)
        time.sleep(2)
        elem = driver.page_source
        soup1 = BeautifulSoup(elem, 'lxml')
        with open(temp + str(count) + '.txt', 'w') as f:
            f.write(soup1.prettify())

        print("saved file: " + temp + str(count) + '.html')
        count = count + 1
    else:
        temp = q_types[0]
        q_types.pop(0)
        count = 1
