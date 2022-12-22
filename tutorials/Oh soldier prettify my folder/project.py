#this that normal
import os

def sodier(path_name, txt_file, extension):
    all_dir = os.listdir(path_name)
    os.chdir(path_name)

    ls = []
    with open(txt_file) as f:
        all_word = f.readlines()
        # print(all_word)
        for i in all_word:
            ls.append(i)
        # print("ls list", ls)

    with open(txt_file, 'w') as f1:
        for i in ls:
            if i in ['this\n', 'that\n', 'normal\n']: 
                f1.write(i.lower())
            else: 
                f1.write(i.capitalize())
        print("word are capitiliaze except 'this','that', 'normal' ")

    #jpeg format 
    os.chdir('image')#change directory
    no = 12
    for i in os.listdir():
       if os.path.isfile(i):
           sep = i.split('.')[1] 
           if sep in extension:
               os.rename(i, f"{no}.{extension}")
               no += 1
    print("specific type of extension renamed")
        

if __name__ == '__main__' :
    sodier(r"Oh Soldier Prettify My Folder", r"txt folder/ErMapsh.txt", "jpg")
