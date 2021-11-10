from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

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


# print(driver.page_source)

data = driver.find_element_by_class_name('central-featured')
# print(type(data), "---")
# print(data, "---")
# print(data.text)

element1 = data.find_elements_by_class_name('central-featured-lang')
# print(element1)
for x in element1:
    # print(x.text)
    print(x.find_element_by_tag_name('strong').text)
    print(x.find_element_by_tag_name('small').text)

driver.close()
