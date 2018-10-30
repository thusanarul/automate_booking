from script_morning import job_morning
from script_evening import job_evening
import schedule
import time


schedule.every().day.at("00:00").do(job_morning)
schedule.every().day.at("00:01").do(job_evening)
while 1:
    schedule.run_pending()
    time.sleep(1)