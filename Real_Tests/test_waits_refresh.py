from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
expected_title = "Electronics, Cars, Fashion, Collectibles & More | eBay"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://www.ebay.com/")
assert browser.title == expected_title

browser.find_element_by_id("gh-ac").send_keys("Dodge")
#element = WebDriverWait(browser,5).until(lambda x: x.find_element_by_xpath())
#or
#element = WebDriverWait(browser,5).until(EC.presence_of_element_located((By.XPATH,"xpath")))
