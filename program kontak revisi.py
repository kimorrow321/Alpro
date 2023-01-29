import os
contact={}

def clsr():
    os.system("pause")
    os.system("cls")
#ini adalah tampilan menu
def title(args):
    print("=============================")
    print("        Contact Book")
    print("=============================")
    print(">> " + args)

def menu():
    title("Menu")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Display Contact")
    print("4. Update Contact")
    print("5. Sort Contact")
    print("6. Save Contact")
    print("7. Load Contact")
    print("0. Exit")
    choose = int(input("Choose : "))
    return choose