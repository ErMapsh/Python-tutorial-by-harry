word_dict = {"WHO": 'World Health Orginazation', 'WTF': 'What the fuck', 'EZ':"easy", "NT": 'nice try'}

print("1.WHO\n2.WTF\n3.EZ\n4.NT")
try:
    ans = input("Enter The Word:");
    print(f'Meaning of {ans} is \"{word_dict[ans]}"');
except Exception as e:
    print(e)