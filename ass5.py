#one:value_error
try:
    print(1/0)
except:
    print("Not divisible")
finally:
    print("Always printable")

#two: file handling(non-existing file)
try:
    f_o = open("hello.txt", "r")
except:
    print("unable to open file")
finally:
    print("maybe the file doesn't exist")

#three:type_error
try:
    print(10 + "10")
except:
    print("addition of number and string")
finally:
    print("It is an example of type error")

#four(multiple excepts)
a,b = 1,0
try:
    print(a/b)
    print("this won't be printed")
    print("15" + 10)
except TypeError:
    print("you added values of different types")
except ZeroDivisionError:
    print("You divided by zero")

#fifth(generic except)
try:
    print('1'+1)
    print(sum)
    print(1/0)
except NameError:
    print("sum does not exist")
except ZeroDivisionError:
    print("Cannot divide by 0")
except:
    print("Something went wrong")
    

