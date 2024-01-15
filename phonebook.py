def intro():
    option = int(input("Electronic Phone Book."
                        "1. look up an entry"
                        "2. set an entry"
                        "3. delete an entry"
                        "4. list all entries"
                        "5. quit"
                        "what would you like to do? (1-5) "
                        ))
    return options

def phone_book():
    contact = {}
    
    while True:
        option = intro()
        
        # ???entry 1
        
        if option == 2:
            contact_name = input("enter contact name")
            phone_number = input("enter your contact phone number")
            
        elif option == 3:
            name =input("delete entry") 
              