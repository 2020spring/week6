import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# keywords: HTML (DOM),
#   locator: xpath(querying), cssSelector(querying) can be customized using tags and attributes
#   locators on html: id, name, link_name, partial_link_name, class_name

# Google search scenario:
# 1. Open the browser, launch the website google.com (Given condition in Gherkin scenario)
# 2. type 'selenium python' in the search and hit Enter (Actions - When)
# 3. Verify the result is more 20 mln (Test here, check point - Then)
# 4. Verify that it take less than a second for the search (Test here, check point - Then)
# 5. close the browser

driver = webdriver.Chrome()  # start the browser
driver.get("https://google.com")
print("opened the browser and google website")
time.sleep(3)
search_text_box = driver.find_element_by_name("q")  # finding(locating) search box element in the HTML DOM
print("identified google search box")

search_text_box.clear()  # just in case clearing the search field
search_text_box.send_keys("python selenium")  # enter provided text in the search box
print("cleared the search box then typed 'python selenium' words in it")
search_text_box.send_keys(Keys.RETURN)  # simulates hitting the Enter key on your keyboard
print("hit the enter button")
time.sleep(3)

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)

# "About 31,100,000 results (0.39 seconds)"
# verify the result num is > 20 mln
result_msg_list = result_msg.split()
result_num_str = result_msg_list[1].replace(',', '')
result_num = int(result_num_str)
assert result_num > 20000000, "Result num is less than 20 mln"
print("Verifying result number Passed.")

# Verifying the performance , less than a second
result_time_str = result_msg_list[3].replace('(', '')
result_time = float(result_time_str)
assert result_time < 1, "Search took more than a second!"
print("Verifying search performance Passed.")

print("now closing the browser...")
driver.close()
