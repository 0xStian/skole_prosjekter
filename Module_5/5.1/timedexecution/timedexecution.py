import schedule
import time
import os

def job():
    os.system("start chrome https://www.noroff.no")
    with open("welcome.txt", "r") as file:
        print(file.read())


schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
