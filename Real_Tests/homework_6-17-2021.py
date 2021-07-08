import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
browser = webdriver.Chrome(ChromeDriverManager().install())

#Amazon

amz_home_page = "https://www.amazon.com/ref=nav_logo"
kindle_url = "https://www.amazon.com/Kindle-eBooks/b/?ie=UTF8&node=154606011&ref_=nav_cs_kindle_books_cb90cf2f444c4309b8c318987bb36150"
home_page_title_amz = "Amazon.com. Spend less. Smile more."


#1.Navigate to the Amazon home page. Verify page title.
#Do a search for "MacBook Pro" and verify the title of the new page.
# browser.get("https://www.amazon.com/ref=nav_logo")
# assert browser.title == home_page_title_amz
# browser.maximize_window()
# browser.find_element_by_id("twotabsearchtextbox").send_keys("MacBook Pro" + Keys.ENTER)
# assert browser.title == "Amazon.com : MacBook Pro"

#2. Navigate to the Amazon home page.
#Click on "Kindle Books" from the top menu and verify the title of the new page and URL of the new page.
'''browser.get(amz_home_page)
browser.maximize_window()
browser.find_element_by_link_text("Kindle Books").click()
assert browser.current_url == kindle_url'''

#3. Navigate to the Amazon home page.
#Do a search for "Macbook" and press "down arrow" 3 times and then press Enter button.
'''browser.get(amz_home_page)
browser.maximize_window()
browser.find_element_by_id("twotabsearchtextbox").send_keys("Macbook")
time.sleep(3)
browser.find_element_by_id("twotabsearchtextbox").send_keys(Keys.ARROW_DOWN * 3 + Keys.ENTER)'''

#4. Navigate to the Amazon home page. Verify page title.
#Try to build a test which is doing 3 different searches "MacBook Pro", "Mac Mini" and "Linux Notebook".
#(You can use List and you can use FOR loop).
browser.get("https://www.amazon.com/ref=nav_logo")
assert browser.title == home_page_title_amz
searches = ["MacBook Pro", "Mac Mini", "Linux Notebook"]
for values in searches:
    browser.find_element_by_id("twotabsearchtextbox").send_keys(values + Keys.ENTER)





