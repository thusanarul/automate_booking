from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from datetime import timedelta
from selenium.common.exceptions import NoSuchElementException
from mail_script import send_mail
import os, sys


def job_evening(usrname, passwd, email, email_pwd):
    browser = webdriver.Chrome(os.path.join(sys.path[0], "chromedriver"))
    now = datetime.now()
    booking_date = now + timedelta(days=14)
    # "R30", "R80", "Sentralbygg 2 S22", "Sentralbygg 2 S23", "Sentralbygg 2 S24", "Elektro E/F EL23"
    rooms = ["360DU1-105", "360D5-133", "322255C", "322260A", "322260B", "341E404"]

    browser.get('http://www.ntnu.no/romres')
    #####
    input_data = browser.find_element_by_id("org_selector-selectized")
    input_data.send_keys("NTNU")
    input_data.send_keys(Keys.ENTER)

    usr_name = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    usr_name.send_keys(usrname)
    password.send_keys(passwd)
    password.send_keys(Keys.ENTER)


    date_picker = browser.find_element_by_id("preset_date")
    string_date = str(booking_date.day) + "." + str(booking_date.month) +  "." + str(booking_date.year)
    script_string = "arguments[0].setAttribute('value', '{}')".format(string_date)
    browser.execute_script(script_string, date_picker)

    start_picker = browser.find_element_by_id("start")
    start_picker.click()
    start_picker.get_attribute("value")
    start_picker.send_keys("12")
    start_picker.click()
    start_time = browser.find_element_by_xpath("//option[@selected='selected']")
    start_time_value = start_time.get_attribute("value")
    assert "12:00" in start_time_value


    end_picker = browser.find_element_by_id("duration")
    end_picker.click()
    end_picker.get_attribute("value")
    end_picker.send_keys("16")
    end_picker.click()
    end_time = browser.find_element_by_xpath("//option[@value='04:00']")
    end_time_duration = end_time.get_attribute("selected")
    assert "true" in end_time_duration

    area_picker = browser.find_element_by_id("area")
    area_picker.click()
    area_picker.send_keys("g")
    area_picker.click()

    show_rooms = browser.find_element_by_id("preformsubmit")
    show_rooms.click()

    value = ""
    for i in rooms:
        string_builder_room = '//*[@title="' + i + '"' + "]"
        try:
            assert browser.find_element_by_xpath(string_builder_room)
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

    string_builder_conf_room = "//span[@title='" + value + "']" + "//a[@target='_blank']"
    confirmed_room = browser.find_element_by_xpath(string_builder_conf_room).text

    send_mail(confirmed_room, "12:00-16:00", email, email_pwd)

    browser.close()
