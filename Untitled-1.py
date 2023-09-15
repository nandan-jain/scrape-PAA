import time
import json
from selenium import webdriver
from bs4 import BeautifulSoup

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/search?q=python")

span_element = driver.find_element("xpath", "//span[text()='People also ask']")

parent_element = span_element.find_element("xpath", "../../../..")

child_divs = parent_element.find_elements("xpath", "//div[@jsname = 'yEVEwb']")
collection = []
qts_list = set()
for i, element in enumerate(child_divs):
    soup = BeautifulSoup(element.get_attribute("innerHTML"), "html.parser")
    qts = soup.find('span', {'class': 'CSkcDe'}).text
    qts_list.add(qts)
    collection.append({
        "question": qts
    })

for i, qts in enumerate(child_divs):
    qts.click()
    time.sleep(5)
    span_element = driver.find_elements("xpath", "//span[text()='People also ask']")
    parent_element = span_element[0].find_element("xpath", "../../../..")
    updated_qts = parent_element.find_elements("xpath", ".//div[@jsname = 'yEVEwb']")

    qts_list_updated = set()
    for j, element in enumerate(updated_qts):
        soup = BeautifulSoup(element.get_attribute("innerHTML"), "html.parser")
        qts = soup.find('span', {'class': 'CSkcDe'}).text
        qts_list_updated.add(qts)

    collection[i]["children"] = [{"question": question} for question in qts_list_updated-qts_list]
    qts_list = qts_list_updated

print(json.dumps(collection, indent=4))
