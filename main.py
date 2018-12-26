from script_morning import job_morning
from script_evening import job_evening
import schedule
import time


usrnames = []

try:
    f = open("passwords.txt", "r")
    for line in f:
        usrnames.append(line.strip("\n").split(","))
except:
    print("failed")


usrname, passwd = usrnames[0][0], usrnames[0][1]
email, email_pwd = usrnames[1][0], usrnames[1][1]


schedule.every().day.at("20:43").do(job_morning, usrname, passwd, email, email_pwd)
schedule.every().day.at("20:39").do(job_evening, usrname, passwd, email, email_pwd)
while 1:
    schedule.run_pending()
    time.sleep(1)