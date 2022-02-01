import os

# Context for what the program does:
print("\nThis program helps you store and retrieve your passwords easily and securely.")

# Encryption method for ROT3. Can use for both to encoding & decoding by changing "value"
def rot(entry,x):
    global master_key
    master_key = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<,+"
    encode = "".join([master_key[(master_key.find(c)+x)%94] for c in entry])
    return encode

# Method for getting for Username, Password & URL from the user and appending to credentials.txt
# If credentials.txt is unavailable, Python will create automatically.
def add_data():
    print("Do NOT use empty spaces")
    userName = input("Enter your username: ")
    passWord = input("Enter your password: ")
    url = input("Enter URL: ")
    # Encode the inputs with ROT3 and change into different variables before saving into credentials.txt
    encName = rot(userName,3)
    encPw = rot(passWord,3)
    encUrl = rot(url,3)
    if not os.path.exists("credentials.txt"):
        i = open("credentials.txt", "x")
        i.close()
        f = open("credentials.txt", "a")
    else:
        f = open("credentials.txt", "a")
    f.write(encName + " " + encPw + " " + encUrl + " " + "\n")
    f.close()

# Method to read the credentials and display in a visually presentable manner
# Use ROT3 to decrypt the text file.
def read_data():
    if not os.path.exists("credentials.txt"):
        i = open("credentials.txt", "x")
        i.close()
        f = open("credentials.txt", "r")
    else:
        f = open("credentials.txt", "r")
    # Make sure the headings are seperated from each other by equal spacing
    print(f"{'USER NAME' :<30} {'PASSWORD' :^30} {'WEBSITE ADDRESS' :>36}")
    print("\n")
    # Make sure the data entries are displayed under each allocated heading
    for data in f:
        x = data.split(" ")
        print(f"{rot(x[0],-3) :<30} {rot(x[1], -3) :^30} {rot(x[2],-3) :>36}")
    print("\n")
    f.close()

choice = ''

# Create a loop that will repeat menu options unless exit option selected
while choice != '3':
    print("""
    [1] Enter Credentials
    [2] Retrieve Credentials
    [3] Exit Program""")
    #Get user choice
    choice = input("\nPlease enter your choice: ")
    if choice == '1':
        add_data()
    elif choice == '2':
        read_data()
    elif choice == '3':
        print("Exited the program.")
        break
    else:
        print("Enter a numeric value between 1 and 3: ")

        