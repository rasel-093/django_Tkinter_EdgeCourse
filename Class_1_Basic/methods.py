def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
    while True:
        number = int(input('Enter an integer number to calculate factorial: '))
        if number == 0:
            break
        else:
            fact = factorial(number)
            print("Facetorial of ", number, 'is: ', fact)
            print(len(str(fact)))


