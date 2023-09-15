from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

driver = webdriver.Chrome()
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/search?q=python")
span_element = driver.find_element("xpath", "//span[text()='People also ask']")
print(span_element.text)

parent_element = span_element.find_element("xpath", "../../../..")
print(parent_element.get_attribute("class"))

child_divs = parent_element.find_elements("xpath", "//div[@jsname = 'yEVEwb']")
print(len(child_divs))

child_divs[0].click()

import time
time.sleep(5)

# with open("test.html", "w", encoding="utf-8") as f:
#     f.write(parent_element.get_attribute("innerHTML"))

soup = BeautifulSoup(parent_element.get_attribute("innerHTML"), "html.parser")
# print(soup)
elements_with_jsname_yEVEwb = soup.find_all(attrs={"jsname": "yEVEwb"})
print(len(elements_with_jsname_yEVEwb))
# for ele in elements_with_jsname_yEVEwb:
#     span_elements = ele.find_all('span')
#     print(span_elements)

# child_divs = parent_element.find_elements("xpath", "//div[@jsname = 'yEVEwb']")
# print(len(child_divs))


# print(child_divs[0].get_attribute("innerHTML"))

# span_element = driver.find_element("xpath", "//span[text()='People also ask']")
# print(span_element.text)

# parent_element = span_element.find_element("xpath", "../../../..")
# print(parent_element.get_attribute("class"))

# child_divs = parent_element.find_elements("xpath", "//div[@jsname = 'yEVEwb']")
# print(len(child_divs))
