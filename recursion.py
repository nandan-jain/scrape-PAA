from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import time
import json
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?q=python")

def get_questions_elements(driver):
    #TODO Change the way to get spans
    # paa_spans = driver.find_elements("xpath", "//span[text()='Questions related to your search']")
    paa_spans = driver.find_elements("xpath", "//span[text()='People also ask']")
    # print(len(paa_spans))
    if not paa_spans:
        paa_spans = driver.find_elements("xpath", "//span[text()='Questions related to your search']")
        if not paa_spans:
            paa_spans = driver.find_elements("xpath", "//span[text()='More to ask']")


    paa_main_div = paa_spans[0].find_element("xpath", "../../../..")    
    return paa_main_div.find_elements("xpath", ".//div[@jsname = 'yEVEwb']")

def get_question_text(element):
    soup = BeautifulSoup(element.get_attribute("innerHTML"), "html.parser")
    return soup.find('span',{'class' : 'CSkcDe'}).text

def get_questions(driver):
    questions_elements = get_questions_elements(driver)
    question_list = set()
    for i,element in enumerate(questions_elements):
        question_text = get_question_text(element)
        question_list.add(question_text)
    return question_list

body = driver.find_element(By.TAG_NAME, "body")

level_1_questions = get_questions_elements(driver)
collection = [get_question_text(question) for question in level_1_questions]
print(list(level_1_questions))
print(collection)

def create_nested_dict(div_elements, depth=0, max_depth=1):
    if not div_elements or depth > max_depth:
        return {f"{get_question_text(item)}": {} for item in div_elements}

    result = {}
    for element in div_elements:
        question_text = get_question_text(element)        
        existing_divs = set(get_questions_elements(driver))
        body.send_keys(Keys.HOME)
        time.sleep(2)
        element.click()
        time.sleep(2)
        updated_divs = set(get_questions_elements(driver))
        new_divs = updated_divs - existing_divs
        result[question_text] = create_nested_dict(new_divs, depth + 1, max_depth)

    return result

nested_dict = create_nested_dict(level_1_questions)
print(json.dumps(nested_dict, indent=4))