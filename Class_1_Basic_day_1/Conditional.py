if __name__ == '__main__':
    # number = int(input("Enter an integer: "))
    # if number%2 == 1:
    #     print("The number is odd\n")
    # else: print("The number is even\n")

    # Nested conditional
    std_marks = int(input("Enter marks\n"))
    if std_marks >= 80:
        print('A+')
    elif std_marks>=70 and std_marks <80:
        print('A Grade\n')
    elif std_marks>=60 and std_marks<70:
        print("B Grade\n")
    elif std_marks>=50 and std_marks<60:
        print("C Grade")
    else:
        print('Best wishes for next time\n')
