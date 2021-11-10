from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from django.utils.crypto import get_random_string

from webdriver_manager.chrome import ChromeDriverManager  # chrome

driver = webdriver.Chrome(ChromeDriverManager().install())
# from webdriver_manager.firefox import GeckoDriverManager  # firefox
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# driver = webdriver.Firefox()
driver.get('https://www.wikipedia.org/')
assert 'Wikipedia' in driver.title

# elem = driver.find_element_by_id('searchInput')  # Find the search box
# elem.clear()
# elem.send_keys('hey' + Keys.RETURN)
# print(driver.find_element_by_xpath('//*[@id="ca-history"]/a').text)


data = driver.find_element_by_class_name('central-featured')

element1 = data.find_elements_by_class_name('central-featured-lang')
lang_dict = {}
footer_dict = {}
lang_list = []
for x in element1:
    key = x.find_element_by_tag_name('strong').text
    value = x.find_element_by_tag_name('small').text

    lang_dict_1 = {key: value}
    lang_dict.update(lang_dict_1)

# -------------------------------
footer = driver.find_element_by_class_name('other-projects')
footer_elements = footer.find_elements_by_class_name('other-project')
for x in footer_elements:
    key = x.find_element_by_class_name('other-project-title').text
    value = x.find_element_by_class_name('other-project-tagline').text
    foot_dict_1 = {key: value}
    footer_dict.update(foot_dict_1)

# -------------------------------
lang_dict.update(footer_dict)
lang_list.append(lang_dict)

df = pd.DataFrame(lang_list)
# file_name = get_random_string(3) + ".csv"
# df.to_csv("file_name.csv", index=False)  # UN-COMMENT THIS LATER
print(df)
driver.close()
