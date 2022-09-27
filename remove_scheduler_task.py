import os, ctypes, sys, time

task_name = "task name"
time_between_removal = 600

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    while True:
            os.system(f"SchTasks /DELETE /F /TN {task_name}")
            time.sleep(time_between_removal)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
