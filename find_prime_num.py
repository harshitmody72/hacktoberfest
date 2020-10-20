while True:
    div = []
    num = int(input('Enter your number here to find if its a prime number '))
    for i in range(1,num+1):
        if num%i == 0:
            div.append(i)
    if len(div) > 2:
        print(f'Your number {num} is not a prime number')
    else:
        print(f'Your number {num} is prime!')