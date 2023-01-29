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

def isKey(key):
    global contact
    if key in contact.keys():
        return True
    else:
        return False
#ini adalah opsi untuk menambahkan kontak yang ingin di tambahkan
def add_contact():
    global contact
    title("Add Contact")
    name = input("Nama  : ")
    nohp = input("No Hp : ")
    if not isKey(name):
        contact[name] = nohp
    else:
        print("Sorry your name was here")
    