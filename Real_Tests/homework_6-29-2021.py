from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(ChromeDriverManager().install())

#Test 1:
#1. Navigate to Ebay.com
#browser.get("https://www.ebay.com/")
#browser.maximize_window()
#2. Verify title
#assert browser.title == "Electronics, Cars, Fashion, Collectibles & More | eBay"
#3. Type in Lexus in the search field
#browser.find_element_by_id("gh-ac").send_keys("Lexus")
#4. Click on the 3rd element from the bottom (for example Lexus ES) using xpath and Explicit Wait
#es_element = WebDriverWait(browser, 4).until(EC.presence_of_element_located((By.XPATH, "//a[@aria-label='lexus is300']")))
#5. Verify title of the newly opened page.
#assert browser.current_url == "https://www.ebay.com/"

#Test 2:
#1. Navigate to Ebay.com
browser.get("https://www.ebay.com/")
browser.maximize_window()
#2. Verify title
assert browser.title == "Electronics, Cars, Fashion, Collectibles & More | eBay"
#3. Click on "Motors" link at the top menu
browser.find_element_by_link_text("Motors").click()
#4. Verify title (that you are on Motors page)
assert browser.current_url == "https://www.ebay.com/b/Auto-Parts-and-Vehicles/6000/bn_1865334"
#5. complete the form Find Vehicle -> Cars and Trucks
#Select "Aston Martin" from Make dropdown (using xpath and Explicit Wait)
browser.find_element_by_name("Make").click()
ast_martin = WebDriverWait(browser, 4).until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='mainContent']//div[@class='motors-finder vehicles']/div[@class='motors-finder__body tabs']/form[@role='tabpanel']//div[@class='motors-finder__menus']/span[1]//option[@value='Aston Martin']")))
ast_martin.click()
#browser.find_element_by_xpath("//div[@id='mainContent']//div[@class='motors-finder vehicles']/div[@class='motors-finder__body tabs']/form[@role='tabpanel']//div[@class='motors-finder__menus']/span[1]//option[@value='Aston Martin']").click()



#6. Select "DB11" from model dropdown (using xpath and Explicit Wait)
#7. Enter your zip code
#8. click on "Find Vehicle" button
#9. Verify title of the page

#1. Test 3 (optional) for implicit wait:
#2. Specify implicitly_wait for 5 seconds
#3. Navigate to Ebay.com
#4. Verify title
#5. Type in Lexus in the search field
#6. Click on the 3rd element from the bottom (for example Lexus ES) using xpath or ID or link text
#7. Verify title of the newly opened page.