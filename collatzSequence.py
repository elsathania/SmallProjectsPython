def collatz():
    number = input()
    try:
        number = int(number)
        while True:
            print(int(number))
            if number%2 ==0 and number!=1:
                number =number/2
            elif number%2 ==1 and number!=1:
                number = number*3+1
            elif number==1:
                break
    except ValueError :
        print('You must enter an integer')
        return(collatz())
print('Please type a number')
collatz()
