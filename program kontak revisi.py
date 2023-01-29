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
#ini adalah menghapus kontak
def del_contact():
    global contact
    title("Delete Contact")
    key = input("Name : ")
    if isKey(key=key):
        del contact[key]
    else:
        print("Maaf" +key+ "tidak ada di kontak anda")
#ini adalah penambahan sort
def sort_contact():
    global contact
    title("Sort Contact")
    sort_contact = sorted(contact.items(), key=lambda x: x[0])
    print(sort_contact)
#ini penambahan save kontak
def save_contact():
    global contact
    title("Save Contact")
    file = open("contact.txt", "w")
    for key, value in contact.items():
        file.write(key + "," + value + "\n")
    file.close()
#ini penambahan load kontak
def load_contact():
    global contact
    title("Load Contact")
    file = open("contact.txt", "r")
    for line in file:
        key, value = line.split(",")
        contact[key] = value
    file.close()