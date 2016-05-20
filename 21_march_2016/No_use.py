from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://stackoverflow.com/")
results = []


def collecting_links():
    body = driver.find_element_by_tag_name("body")
    links = driver.find_elements_by_class_name('question-hyperlink')

    for link in links:
        results.append(link.get_attribute('href'))

collecting_links()

for result in results:
    driver.get(result)
    collecting_links()

    
#body.send_keys(Keys.CONTROL + 't')
#driver.get('http:www.wapindia.co')
#body = driver.find_element_by_tag_name("body")
#body.send_keys(Keys.CONTROL + 'w')


print(results)
driver.quit()
