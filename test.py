
def add(list):
    name_to_add = input("what is the person's name?\n")
    connection_to_add = input("what is the connection that you want to connect with?\n")
    print("You just add" , name_to_add)
    print("with the connections of" , connection_to_add)
    connection_to_add = connection_to_add.split(',')
    list[name_to_add] = connection_to_add

def search(list):
    name_to_find = input("What is the name that you want to find?\n")
    if name_to_find in list:
        print(list[name_to_find])
    else:
        print("Did not find the name in the list")


list = {}
print("Welcome to use the program")
print("Please type in what do you want to do")
user_input = input("add, search, change, delete, quit\n")
while(user_input != "quit"):
    if(user_input == "add"):
        add(list)
    if(user_input == "search"):
        search(list)
    user_input = input("add, search, change, delete, quit\n")




#list = {"Jason": {"Anthony", "Joe"},
#        "Anthony": {"Jason", "Joe"},
#        "Joe": {"Anthony", "Jason"}}


#print(list["Jason"])
#list["Salem"] = {"Anthony", "Jason"}
#print(list["Salem"])
