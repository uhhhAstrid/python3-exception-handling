# exception handling demo project
# this script circumvents the error using exception handling

def flawed_code():
    print ("This will print to console.") # Error has not occurred yet.
    print(10/0) # Error occurs
    print("This will not print to console.") # Whenever an error occurs, the code stops running that method completely.

if __name__ == '__main__':
    print("Running Code")
    
    # This will prevent the error from stopping the entire program
    # Instead, the code will stop the method that caused the error
    # In order to keep the program running
    try: # This means, "this code might not work, so if it breaks, don't stop the whole program"
        flawed_code()
    except ZeroDivisionError: # This means, "look for errors called 'ZeroDivisionError', and if there is one, run the nested code"
        # the code resumes here after catching the error
        print("Method failed to run; cannot divide by 0.")    
    
    # Because the error was caught, the main method wasn't stopped,
        # so this line will run too!
    print("Code ran")