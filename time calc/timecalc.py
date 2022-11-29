import time

first_number = input("first number: ")
second_number = input("second number: ")

time_to_sleep = int(first_number) + int(second_number)
start = time.time()
time.sleep(time_to_sleep)
end = time.time()
result = end - start
print("{0:.2f}".format(result))