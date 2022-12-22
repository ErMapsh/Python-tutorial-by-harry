dier(path_name, txt_file, extension):
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
    os.chdir('C:/temporary file/python study/Oh Soldier Prettify My Folder/image')#change directory
    no = 3
    for i in os.listdir():
       if os.path.isfile(i):
           sep = i.split('.')[1] 
           if sep in extension:
            #    print(i)
               os.rename(i, f"{no}.jpg")
               no += 1
    print("File updated of specific format")
        