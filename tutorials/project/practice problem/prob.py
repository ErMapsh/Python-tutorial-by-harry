#when they turn 100 years old  (05-30-2000)
# take age or year of birth of user 
minimum_year_of_birth = 1950
last_year= 2090

current_date = '09-22-2021'
current_date_ls = current_date.split('-')

user_birth = input('Enter the birth date(mm-dd-yyyy): ')
user_birth_ls = user_birth.split('-')

if int(user_birth_ls[2]) <= minimum_year_of_birth:
    print(f"You seem to be the oldest person alive")
    
elif int(user_birth_ls[2]) > int(current_date_ls[2]):
    print('You are not yet born')

elif int(user_birth_ls[2]) < last_year:
    get_user_birth_year = int(user_birth_ls[2])#like 2000
    age = 0
    for i in range(get_user_birth_year , last_year):
        age += 1
    print(f'Age in 2090 is {age}')
    


