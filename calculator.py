def calculator():
    print ("ctrl+c to terminate")
    print ("This Calculator is able to perform *, /, -, +, **, % , #, t for table, c for counting etc")
    cal = input("Now Enter the action Yo want to Perform: ")
    if cal == "t":
        if cal == 'c':
            if cal == '#':
                print("Welcome to advanced calculation")          
            else:
                value1 = input("Enter the number 1: ")
                while value1 == "":
                    value1 = input("Enter the number 1: ")
                    value2 = input("Enter the number 2: ")
                while value2 == "":
                    value2 = input("Enter the number 2: ")
                    value1 = float(value1)
                    value2 = float(value2)
                    result = None

    match cal:
        case 't':
            num = input("Enter the number whose table you want: ")
            while num == "":
                num = input("Enter the number whose table you want: ")
            limit = input("Enter the limit where its going to be stop: ")
            while limit == "":
                limit = input("Enter the limit where its going to be stop: ")
            num = int(num)
            limit = int(limit)
            for x in range(1, limit+1):
                result = int(num * x)
                print(num, " * ", x, ' = ', result)
                  
        case 'c':
            num = input("Enter the number where the counting begins: ")
            while num == "":
                num = input("Enter the number where the counting begins: ")
            limit = input("Enter the range where its going to be stop: ")
            while limit == "":
                limit = input("Enter the limit where its going to be stop: ")
            num = int(num)
            limit = int(limit)
            for x in range(num, limit+1):
                print(x)
        
        case '#':
            value = input("Enter the alphanumeric word you want to hash: ")     
            print (hash(value))                                  
        case '*':
            result = value1 * value2
            print("The Multiplication of ", value1 ," and ", value2, " is ", result)
        case '/':
            result = value1 / value2
            print("The Division of ", value1, " and ", value2, " is ", result)
        case '-':
            result = value1 - value2
            print("The Substraction of ", value1, " and ", value2, " is ", result)
        case '+':
            result = value1 + value2
            print("The Addition of ", value1, " and ", value2, " is ", result)
        case '**':
            result = value1 ** value2
            print("The Exponent of ", value1, " and ", value2, " is ", result)
        case '%':
            result = value1 % value2
            print("The Modulus of ", value1, " and ", value2, " is ", result)
        case _:
            print("So sorry this option is under contruction")


print ("Calculator")  
calculator()
        
retry = input("Do you want another calculation (y/n): ")
while retry == 'y':
    calculator()   
    retry = input("Do you want another calculation (y/n): ")
else:
    print("Thank you for using") 