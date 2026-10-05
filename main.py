import hashlib 
import json
import os
from encryption import key_main,encrypt_password,decrypt_password


def enterPassword():
   website = input('Enter website name')
   username = input('Enter your username')
   password = input('Enter your password')
   key = key_main()
   encrypted_password = encrypt_password(password,key)

   if os.path.exists('passwords.json'):
      with open ('passwords.json','r') as file:
         data = json.load(file)
         myPassword = {
           'Website'  : website,
           'Username' : username,
          'Password' : encrypted_password    }
         
         data['passwords'].append(myPassword)
         with open ('passwords.json','w') as file:
           json.dump(data, file, indent = 4)
           print("Password saved successfully")
         
   else:
      data = {'passwords' : []}

      myPassword = {
            'Website'  : website,
            'Username' : username,
            'Password' : encrypted_password
         }
      data['passwords'].append(myPassword)
      with open ('passwords.json','w') as file:
         json.dump(data, file, indent = 4)
       
         print("Password saved successfully")

def view_password():
   if not os.path.exists('passwords.json'):
      print("No saved password yet")
      return
   else:
      with open ('passwords.json','r') as file:
         data = json.load(file)
         passwords = data['passwords'] 
         for items in passwords:
            encrypted_password = items['Password']
       
         key = key_main()
         decrypted_password = decrypt_password(encrypted_password,key)
         
      if not passwords:
         print('No saved password yet')
      else:
         for index, account in enumerate(passwords):
           print(f'{index + 1}. Website ==> {account['Website']}\n Username ==> {account['Username']}\n Password ==> {decrypted_password}')
         


def menu():
   while True:
      print("=========================")
      print("DE BEST PASSWORD MANAGER")
      print("=========================")  
      print("WELCOME")
      print("MENU (Please pick an option)")
      print("1. Add password")
      print("2. View password")
      print("3. Edit password")
      print("4. Delete password")
      print("5. Check password strength")
      print("6. Suggest strong password")
      print("7. Exit Menu")

      choice = int(input('What would you like to do? Input an option'))
      if choice == 1:
         enterPassword()
         return
      elif choice == 2:
         print('Input your master pin')
         pinConfirm = input()
         if pinConfirm == entered_pin:
           view_password()
           return
         else:
            print('Pin is incorrect!')
      elif choice == 5:
         print("Goodbye! See you later.")
         break
      else:
         print('Invalid input. Please choose correct option')

      




   
while True:
    print('========Welcome======== ')
    print("=========================")
    print("DE BEST PASSWORD MANAGER")
    print("=========================")  
    if os.path.exists("masterPinSaver.json"):
      with open ("masterPinSaver.json", "r") as file:
          data = json.load(file)
          savedHash = data["master_pin_hash"]
          attempt = 3
          while attempt > 0:
             entered_pin = input("Enter you Master pin")
             entered_pinHash = hashlib.sha256(entered_pin.encode()).hexdigest()
      
             if entered_pinHash == savedHash:
               print('Access granted. Welcome!')
               menu()   
               break  
             else: 
               attempt = attempt - 1
               print('Incorrect Master pin')
               print(f'You have {attempt} attempt(s) left')
               
          if attempt == 0:
             print(' Too many incorrect attempts. Try again later')
             break

    else:
      print('DE BEST')
      print('Password Manager')
      pin = input('Create your 4-digit master pin :')
      if len(pin) == 4 and pin.isdigit():
       confirm_pin = input('Confirm pin')
       if confirm_pin == pin:
          pinHash = hashlib.sha256(pin.encode()).hexdigest()
        
          with open ("masterPinSaver.json","w") as file:
            json.dump({"master_pin_hash" : pinHash}, file)
        
            print("Congratulations,  You have successfully created your master password!")
            menu()
            
            break
       else:
         print('Pins do not match')
      else:
        print('PIN must be exactly 4 digits')
        