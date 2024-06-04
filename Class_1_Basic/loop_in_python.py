import math

if __name__ == '__main__':
    # while loop
    # i = 0
    # while i<10:
    #     print(i, end=' ')
    #     i = i+1
    #
    # print('\n')
    # for i in range(10):
    #     print(i, end=' ')
    #
    # print('\n')
    # for i in range(1, 10, 2):
    #     print(i, end=' ')
    # print('\n')
    #
    # list_food = ['Burger', 'Pizza', 'Pasta']
    # for food in list_food:
    #     print(food)

    #Nested loop
    #number = int(input("Enter an integer number"))
    import math
    for i in range(2, 101, 1):
        flag = 1
        for p in range(2, int(math.sqrt(i))+1, 1):
            if i%p ==0:
                flag = 0
                break
        if flag == 1:
            print(i , end=' ')
