#palindrome : Next palindrome number of your enter palindrome
'''
author: ermapsh
Date: 22/09/21
purpose: next palindrome of ur palindrome
'''
def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n
        

def is_palindrome(n):
    return str(n) == str(n)[::-1]



if __name__ == '__main__':
    test_cases_no = int(input("enter the no of test cases:"))
    no = [int(input("enter the your palindorm no:")) for i in range(test_cases_no)]
    print(f"Data in List: {no}")
    
    for i in no:
        print(f"Next Palindrome for {i} is {next_palindrome(i)}")
