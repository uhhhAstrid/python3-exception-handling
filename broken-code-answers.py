# exception handling demo project
# this script returns a divide by 0 error

def flawed_code():
    print("This will print to console because the error has not happened yet.")
    print(10/0) # the error happens *here*, because the error is caused by dividing by 0

if __name__ == '__main__':
    print("Running Code")
    
    # The terminal will list line 22 as one of the errors,
        # even though that line ran without any errors!
    
    # To find out why, we need to look at the list of errors,
        # The list of errors, by the way, is called the "STACK TRACE"

    # The top of the list, where "flawed_code()" is listed, 
        # will always be the first part of the code that started us towards the error
    
    # The bottom of the list, where "print(10/0)" is listed, 
        # will always be the line that threw the error
    flawed_code()

    # when a program throws an error like this, the code stops running completely
    # therefore, this print statement will never run
    print("Code ran")