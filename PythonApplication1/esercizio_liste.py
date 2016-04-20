from random import randint

def main():
    l = GetFamousPeopleList()
    print(l)


    print(GetFirstPersonByFirstName(l,"ian"))
    print(GetAllPersonByFirstName(l,"angus"))
    print(GetFirstPersonByLastName(l,"gilmour"))
    print(LastPerson(l))
    print(l)
    print(RandomPerson(l))
    print(GetPersonByIndex(l,3))
    print(GetFirstPersonByLastName(l, "gilmour"))
    RemovePersonByLastName(l,"gilmour")
    print(l)

def GetFamousPeopleList():
    return [("jimi","hendrix"),("dave","gilmour"),("angus","young"),("ian","gillan"),("david", "coverdale")]

def RemovePersonByLastName(the_list, lastName):
    the_list.remove(GetFirstPersonByLastName(the_list, lastName))

def LastPerson(the_list):
    if(not the_list):
        return []
    else:
        return the_list.pop()

def RandomPerson(the_list):
    return the_list[randint(0,len(the_list) - 1)]

def GetPersonByIndex(the_list, index):
    if(index > len(the_list)):
        return []
    else:
        return the_list[index]

def GetAllPersonByLastName(the_list, lastName):
    return [x for x in the_list if x[1] == lastName]

def GetAllPersonByFirstName(the_list, firstName):
    return [x for x in the_list if x[0] == firstName]

def GetFirstPersonByLastName(the_list, lastName):
    found = [x for x in the_list if x[1] == lastName]
    if(not found):
        return []
    else:
        return found[0]

def GetFirstPersonByFirstName(the_list, firstName):
    found = [x for x in the_list if x[0] == firstName]
    if(not found):
        return []
    else:
        return found[0]

def isEmpty(the_list):
    if(not the_list):
        print("The list is empty")

if __name__ == "__main__":
    main()