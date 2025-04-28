# demo project - example version

def divide():
    print(10/0)

if __name__ == '__main__':
    print("Running")
    try:
        divide()
    except:
        print("Error.")
    print("Code ran successfully")