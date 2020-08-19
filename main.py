print("Hello User")
message = """
1. Add Data
2. Update Details
3. Delete Details
4. Check the list of animals
5. Check the list of types of animals
6. Generate the report
7. Exit"""

def getSelection(arg):
    if(arg == 1):
        print("1")
    if(arg == 2):
        print("2")
    if(arg == 3):
        print("3")
    if(arg == 4):
        print("4")
    if(arg == 5):
        print("5")
    if(arg == 6):
        print("6")
    if(arg == 7):
        exit(0)
    if(arg == 8):
        print("8")
    mainSection()


def mainSection():
    print(message)
    try:
        data = int(input("Selet the option: "))
    except :
        print("Please mention the number")
    getSelection(data)

if __name__ == "__main__":
    mainSection()