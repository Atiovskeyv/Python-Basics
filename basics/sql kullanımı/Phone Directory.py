import sqlite3
import re

while True:
    try:
        connection = sqlite3.connect("telephone_directory.db")
        cur = connection.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Directory(Name,Surname,phone_number INTEGER PRIMARY KEY,housephone INTEGER)""")
       
        infos = []

        def adding():
            print()
            while True:
                name = input(" Enter User Name :").strip()
                if len(name) < 3:
                    print(" User\'s name can\'t be shorter than 3 Digits")
                else:
                    break                
            while True:
                surname = input("  Enter User Surname :").strip()
                if len(surname) < 3:
                    print("  User\'s surname can\'t be shorter than 3 Digits")
                else:
                    break
            while True:
                number = input("   Enter User\'s Phone Number :")
                number = re.sub(r"\s+","",number)
                if len(str(number)) != 11:
                    print("   Your Phone Number Must Be 11 Digits")
                elif len(str(number)) == 11:
                    break
            number = int(number)
            infos.extend([name,surname,number])
            answer = input("   Does User Have Home Phone Number Yes or No :").lower()
            if answer == "yes":
                while True:
                    pnumber = input("    Enter User\'s Home Phone Number :")
                    pnumber = re.sub(r"\s+", "",pnumber)
                    if len(str(pnumber)) != 11:
                        print("    Your Home Phone Number Must Be 11 Digits")
                    elif len(str(pnumber)) == 11:
                        break
                pnumber = int(pnumber)
                infos.append(pnumber)
                pnumber = int(pnumber)
            elif answer == "no":
                infos.append(None)
                pass
            else:
                print("     Unknown İnput")
            
            cur.execute("""INSERT INTO Directory VALUES(?,?,?,?)""",(infos))
            connection.commit()



        def delete_person():
            print()
            while True:
                number = input("Enter the Phone Number You Want to Delete Without 0   :")
                number = re.sub(r"\s+","",number)
                if len(number) != 10:
                    print("     Phone Number You Want to Delete Must Be 10 Digits")
                elif len(number) == 10:
                    try:
                        number = int(number)
                        break
                    except ValueError:
                        print("     Only numbers allowed.")
            cur = connection.execute("""DELETE FROM Directory WHERE phone_number = ? """,(number,))
            connection.commit()
            if cur.rowcount == 0:
                print("     İnvalid Number")
            elif cur.rowcount > 0 :
                print("     Number deleted successfully.")
            


        def update():
            print()
            while True:
                person = input("Enter the person\'s number that you want to update without 0   :")
                person = re.sub(r"\s+","",person)
                if len(person) != 10:
                        print("   Phone Number You Want to Update Must Be 10 Digits")
                elif len(person) == 10:
                    try:
                        person = int(person)
                        break
                    except ValueError:
                            print("     Only numbers allowed.")
            cur = connection.execute("""SELECT phone_number FROM Directory WHERE phone_number = ?""",(person,))
            result = cur.fetchone()
            if result is None:
                print("     This person doesn\'t exist in the directory.")
                return
            req = input("Enter the info you want to change, name, surname, number, homephone :")
            if req == "name":
                while True:
                    name = input(" Enter the name you want to change").strip()
                    if len(name) < 3:
                        print(" User\'s name can\'t be shorter than 3 Digits")
                    else:
                        break 
                connection.execute("""UPDATE Directory SET Name = ? WHERE phone_number = ?""",(name,person))

            if req == "surname":
                while True:
                    surname = input(" Enter the surname you want to change").strip()
                    if len(surname) < 3:
                        print(" User\'s surname can\'t be shorter than 3 Digits")
                    else:
                        break
                connection.execute("""UPDATE Directory SET Surname = ? WHERE phone_number = ?""",(surname,person))

            if req == "number":
                while True:
                    number = input(" Enter the phone number you want to change without 0  :")
                    number = re.sub(r"\s+","",number)
                    if len(number) != 10:
                        print("   Your Phone Number Must Be 10 Digits")
                    elif len(number) == 10:
                        break
                connection.execute("""UPDATE Directory SET phone_number = ? WHERE phone_number = ?""",(number,person))

            if req == "homephone":
                while True:
                    homephone = input(" Enter the phonemuber you want to change without 0  :")
                    homephone = re.sub(r"\s+","",homephone)
                    if len(homephone) != 10:
                        print("   Your Home Phone Number Must Be 10 Digits")
                    elif len(homephone) == 10:
                        break
                connection.execute("""UPDATE Directory SET housephone = ? WHERE phone_number = ?""",(homephone,person))
                            
            else:
                print("  Please Chose the Correct Operation   :")

            connection.commit()



        def show():
            print()
            name = input("Enter the person\'s name you want to learn more about :").strip()
            surname = input("Enter the person\'s surname you want to learn more about :").strip()
            cur = connection.execute("""SELECT phone_number FROM Directory WHERE Name = ? AND Surname = ?""",(name,surname))
            result = cur.fetchone()
            if result is None:
                print("     This person doesn\'t exist in the directory.")
                return
            else:
                cur.execute("""SELECT * FROM Directory WHERE Name = ? AND Surname = ?""",(name,surname))
                data = cur.fetchone()
                print(data)
                connection.commit()


        
        op = input("""                      Press 1 for add a new person
                      Press 2 for delete someone
                      Press 3 for update someone's informations
                      Press 4 for show someone's informations   :""")
        
        if op == "1":
            adding()

        if op == "2":
            delete_person()

        if op == "3":
            update()

        if op == "4":
            show()
        
        if int(op) < 1 and int(op) > 4:
            print("     Wrong Operation")
            
                
        connection.commit()
        connection.close()

    except Exception as e:

        print("\n","        Error  :",e)
    finally:
        print()
        end = input("Do you want to quit? Yes or No :")
        print()
        if end == "Yes":
            break
        elif end == "No":
            pass

