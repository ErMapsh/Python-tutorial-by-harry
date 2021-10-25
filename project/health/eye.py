import time
from plyer import notification

if __name__ == '__main__':
    while True:
		notification.notify(
			title = "**Do eye training!!",
			message = "its important to do, Eyes health",
			app_icon ='C:/temporary file/python study/project/1/eye_icon-icons.com_71204.ico',
			timeout = 5)
		time.sleep(60*30)