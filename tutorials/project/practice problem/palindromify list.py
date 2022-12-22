# given a list content a numbers, if number is greater than 10 then print next palindrome number of that number
ls = [1, 6, 87, 92]
def is_palindrome(no):
    '''
    this function check given no is palindrome, if given no is palindrome then is return True
    '''
    # return str(no) == str(no)[::-1]
    return str(no) != str(no)[::-1]

def next_palindrome(no):
    '''
    first we directly passing argument in this function, but we want next no, so normally increase that no by 1 and run 
    in while loop and check no is palindrome or not, if no is palindrome then is while condition false and while loop exit and 
    return next palindrom no
    '''
    no += 1
    # while not is_palindrome(no):
    while is_palindrome(no):
        no += 1
    return no


if __name__ == "__main__":
    for i in ls:
        if i > 10:
            print(f"Number of {i} is next palindrome is {next_palindrome(i)}")