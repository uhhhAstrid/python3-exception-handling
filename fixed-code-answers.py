# exception handling demo project
# this script circumvents the error using exception handling

def flawed_code():
    print ("This will print to console.") # Error has not occurred yet.
    print(10/0) # Error occurs
    print("This will not print to console.") # Whenever an error occurs, the code stops running that method completely.

if __name__ == '__main__':
    print("Running Code")
    
    # This will prevent the exception from stopping the entire program
    # Instead, it will stop the method that caused the error
    try:
        flawed_code()
    except ZeroDivisionError: 
        # the code resumes here after catching the error
        print("Method failed to run; cannot divide by 0.")    
    
    # Because the exception was caught, the main method wasn't stopped,
        # so this line will run too!
    print("Code ran")