import time
from plyer import notification

if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "**Please Drink Water Now!!",
 			message ="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
 			app_icon = "C:/temporary file/python study/project/1/Iconsmind-Outline-Glass-Water.ico",
 			timeout = 5)
 		time.sleep(60*35)




	



#background me run karna ho to (pythonw.exe file name ) cmd type karo
