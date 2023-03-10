import os
contact={}

def clsr():
    os.system("pause")
    os.system("cls")
#ini adalah tampilan judul kontak
def title(args):
    print("=============================")
    print("        Contact Book")
    print("=============================")
    print(">> " + args)
#ini penambahan menu
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
    global contact #untuk deklarasi variabel secara menyeluruh
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
#ini berfungsi untuk menghapus kontak 
def del_contact():
    global contact
    title("Delete Contact")
    key = input("Name : ")
    if isKey(key=key):
        del contact[key]
    else:
        print("Maaf" +key+ "tidak ada di kontak anda")
#ini penambahan display kontak
def display_contact():
    global contact
    print(contact)
#ini penambahan update kontak
def update_contact():
    global contact
    title("Update Contact")
    key = input("Name : ")
    if isKey(key):
        nohp = input("No Hp : ")
        contact[key] = nohp
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
#ini untuk penambahan fungsi menu
def main():
    i = -1
    while i != 0:
        i = menu()
        clsr()
        if i == 1:
            add_contact()
        elif i == 2:
            del_contact()
        elif i == 3:
            display_contact()
        elif i == 4:
            update_contact()
        elif i == 5:
            sort_contact()
        elif i == 6:
            save_contact()
        elif i == 7:
            load_contact()
        else:
            print("Terimakasih telah menggunakan program ini!")  
            
if __name__ == "__main__":
    main()