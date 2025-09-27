# a = int(input("Enter Your Number:-"))
# try : # try block will check for exception
    # print(10 / a) # ZeroDivisionError: division by zero
# except Exception as err: # except will handle the exception
#     print(f"There is an exception as {err}")
# else :
#     print("No Exception")
# finally : # finally will always execute
#     print("I will run no matter what")
# print("Done!!!")

try :
    age = int(input("Enter Your Age:-"))
    if age < 10 or age > 18 :
        raise ValueError("Age must be between 10 to 18") # raise will raise an exception
    else :
        print("You are eligible")
except Exception as err:
    print(f"There is an exception as {err}")
finally:
    print("I will run no matter what")
print("Done!!!")