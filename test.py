
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

def find(list):
    Starting = input("Who you want to start to?\n")
    Ending = input("Who you want to end with?\n")
    sublist = list[Starting]
    count = 1
    while(True):
        if (Ending in sublist):
            return count
        else:
            length = len(sublist)
            for i in range(length):
                getpeople = sublist[i]
                getfriend = list[getpeople]
                sublist.extend(getfriend)
            count += 1


list = {}
print("Welcome to use the program")
print("Please type in what do you want to do")
user_input = input("add, test, search, find, quit\n")
while(user_input != "quit"):
    if(user_input == "add"):
        add(list)
    if(user_input == "search"):
        search(list)

    if(user_input == "test"):
        list["Alex"] = ["Anthony"]
        list["Anthony"] = ["Alex", "Paul", "Karen", "Jason"]
        list["Paul"] = ["Anthony", "Karen"]
        list["Karen"] = ["Paul", "Anthony", "Salem", "Joe", "Sam"]
        list["Salem"] = ["Karen", "Jason", "Joe", "Nigel"]
        list["Jason"] = ["Miku", "Luka", "Jill", "Anthony", "Salem"]
        list["Miku"] = ["Jason", "Luka"]
        list["Luka"] = ["Jason", "Miku"]
        list["Jill"] = ["Jason", "Joe"]
        list["Joe"] = ["Jill", "Salem", "Joy", "Karen"]
        list["Joy"] = ["Joe"]
        list["Sam"] = ["Karen", "Tucker", "Dan", "Nigel"]
        list["Nigel"] = ["Salem", "Sam"]
        list["Tucker"] = ["Sam"]
        list["Dan"] = ["Sam"]
    if(user_input == "find"):
        Solution = find(list)
        print(Solution)
    user_input = input("add, test, search, find, quit\n")




#list = {"Jason": {"Anthony", "Joe"},
#        "Anthony": {"Jason", "Joe"},
#        "Joe": {"Anthony", "Jason"}}


#print(list["Jason"])
#list["Salem"] = {"Anthony", "Jason"}
#print(list["Salem"])
