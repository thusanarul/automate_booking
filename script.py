from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from datetime import timedelta



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
start_picker.send_keys("00")
start_picker.send_keys(Keys.ENTER)

end_picker = browser.find_element_by_id("duration")
end_picker.click()
end_picker.get_attribute("value")
end_picker.send_keys("12")
end_picker.send_keys(Keys.ENTER)

area_picker = browser.find_element_by_id("area")
area_picker.click()
area_picker.send_keys("g")
area_picker.send_keys(Keys.ENTER)

show_rooms = browser.find_element_by_id("preformsubmit")
show_rooms.click()

possible_rooms = browser.find_element_by_css_selector(".possible-rooms-table")
room = browser.find_element_by_xpath('//*[@title="322255C"]')
for row in room.find_element_by_xpath(".//td"):
    print(row)
print(room)
print(browser.find_element_by_xpath('//*[@title="Velg"]').click())
choose_button = browser.find_element_by_css_selector(".bestillchk")
script_button = "arguments[0].setAttribute('value', '{}')".format("322255C")
browser.execute_script(script_button, possible_rooms)
print(choose_button.get_attribute("value"))