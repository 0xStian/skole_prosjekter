import os, ctypes, sys, time

task_name = "task name" # name of task
time_between_removal = 600 # time to sleep between removal


def is_admin(): # checks if admin, if not puts up prompt asking for admin rights
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

    
if is_admin():
    while True:
            os.system(f"SchTasks /DELETE /F /TN {task_name}") # deletes schedular task with cmd command
            time.sleep(time_between_removal)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
