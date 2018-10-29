from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from datetime import timedelta
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


browser = webdriver.Chrome("/home/thusan/Downloads/chromedriver")
now = datetime.now()
booking_date = now + timedelta(days=14)
# "Sentralbygg 2 S22", "Sentralbygg 2 S23", "Sentralbygg 2 S24", "Elektro E/F EL23"
rooms = ["322255C", "322260A", "322260B", "341E404"]

browser.get('http://www.ntnu.no/romres')
#####
input_data = browser.find_element_by_id("org_selector-selectized")
input_data.send_keys("NTNU")
input_data.send_keys(Keys.ENTER)

usr_name = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")
usr_name.send_keys("piruthua")
password.send_keys("")
password.send_keys(Keys.ENTER)


date_picker = browser.find_element_by_id("preset_date")
string_date = str(booking_date.year) + "-" + str(booking_date.month) + "-" + str(booking_date.day)
script_string = "arguments[0].setAttribute('value', '{}')".format(string_date)
browser.execute_script(script_string, date_picker)

start_picker = browser.find_element_by_id("start")
start_picker.click()
start_picker.get_attribute("value")
start_picker.send_keys("0")
start_picker.click()
start_time = browser.find_element_by_xpath("//option[@selected='selected']")
start_time_value = start_time.get_attribute("value")
assert "08:15" in start_time_value


end_picker = browser.find_element_by_id("duration")
end_picker.click()
end_picker.get_attribute("value")
end_picker.send_keys("12")
end_picker.click()
end_time = browser.find_element_by_xpath("//option[@value='03:45']")
end_time_duration = end_time.get_attribute("selected")
assert "true" in end_time_duration

area_picker = browser.find_element_by_id("area")
area_picker.click()
area_picker.send_keys("g")
area_picker.click()

show_rooms = browser.find_element_by_id("preformsubmit")
show_rooms.click()

possible_rooms = browser.find_element_by_css_selector(".possible-rooms-table")
value = ""
for i in rooms:
    string_builder_room = '//*[@title="' + i + '"' + "]"
    try:
        room = browser.find_element_by_xpath(string_builder_room)
        value = i
        break
    except NoSuchElementException:
        pass
string_builder_choose = "//input[@name='room[]' and @value='" + value + "']"
try:
    choose_button = browser.find_element_by_xpath(string_builder_choose)
    choose_button.click()
except NoSuchElementException:
    print("Favorite rooms not avaiable")
    raise

submit_btn = browser.find_element_by_xpath("//input[@type='submit']")
submit_btn.click()

desc_input = browser.find_element_by_id("name")
desc_input.click()
desc_input.send_keys("jobbe as")

confirm_btn = browser.find_element_by_css_selector(".button.button--primary-green.button--block")
confirm_btn.click()

