contacts=[]
def add_contact(name,phone,email,address):
    contacts.append({"name":name,"phone":phone,"email":email,"address":address})
    print("contact added successfully")
    
def view_contacts():
    if contacts:
        for contact in contacts:
            print(f"name:{contact['name']},phone:{contact['phone']}")
    else:
        print("no contacts available")
        
def search_contact(keyword):
    found=False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"name:{contact['name']},phone:{contact['phone']}")
            found=True
    if not found:
        print('contact not found')
        
def update_contact(name,phone,email,address):
    for contact in contacts:
        if contact['name']==name:
            contact.update({'phone':phone,'email':email,'address':address})
            print("contact update successfully")
            return
        print('contact not found')
        
def delete_contact(name):
    for contact in contacts:
        if contact['name']==name:
            contacts.remove(contact)
            print("contact deleted successfully")
            return
    print('contact not found')
    
while True:
    print('\nmenu:')
    print('1.add contact')
    print('2.view contact list')
    print('3.search contact')
    print('4.update contact')
    print('5.delete contact')
    print('6.exit')
    
    choice=input("enter ur choice:")
    
    if choice=='1':
        name=input('enter name:')
        phone=input("enter phone number:")
        email=input('enter email:')
        address=input('enter address:')
        add_contact(name,phone,email,address)
        
    elif choice=='2':
        print('contacts list:')
        view_contacts()
        
    elif choice=='3':
        keyword=input("enter name or phone number to search:")
        search_contact(keyword)
        
    elif choice=="4":
        name=input("enter name of contact to update:")
        phone=input("enter new phone number:")
        email=input("enter new email:")
        address=input("enter new address:")
        update_contact(name,phone,email,address)
        
    elif choice=="5":
        name=input("enter name of contact to delete:")
        delete_contact(name)
        
    elif choice=="6":
        print("existng")
        break
    
    else:
        print("invalid choice.please enter a number between 1 and 6.")
        
        
    
