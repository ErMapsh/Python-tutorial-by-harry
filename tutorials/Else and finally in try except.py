
try:
    f1 = open("asie hi.txt", "w") 
    f = open("random.txt")   
except EOFError as e:
    print(EOFError)
except IOError as e:
    print(f"input output error occur : {IOError}")


else:
    print("This run only if except is not running..")

finally: 
    print("kuch bhi ho jaye ye print hona chahiye aur complete hona hi chahiye")
    f1.close()
    print("files are closed, and work completed")

print("Some important stuff out side the try and finally..")