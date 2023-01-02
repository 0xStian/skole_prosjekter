import schedule
import time


def job():
    with open("welcome.txt", "r") as file:
        print(file.read())

schedule.every().second.do(job)
# schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1) 