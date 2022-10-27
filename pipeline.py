from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager(cache_valid_range=1).install(), options=options, )

driver.get('https://www.amazon.in/')

driver.find_element_by_xpath("//span[.='Hello, sign in']").click()
driver.find_element_by_id("ap_email").send_keys("kashifamansoor1995@gmail.com")
driver.find_element_by_id("continue").click()
driver.find_element_by_id("ap_password").send_keys("chulbul2020")

