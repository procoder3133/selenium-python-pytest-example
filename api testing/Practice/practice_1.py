from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
amztitle = "Amazon.com. Spend less. Smile more."
browser.get("https://www.amazon.com/ref=nav_logo")
browser.maximize_window()
browser.implicitly_wait(2)
assert browser.title == amztitle
browser.implicitly_wait(5)


browser.get("http://homepro.herokuapp.com/")
browser.find_element_by_link_text("Schedule an Appointment").click()
assert browser.current_url == "http://homepro.herokuapp.com/order.php"
browser.quit()
