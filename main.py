import hashlib 
import json
import os
from encryption import key_main,encrypt_password,decrypt_password
import getpass


def enterPassword():
   website = input('Enter website name:').title()
   username = input('Enter your username:').title()
   password = getpass.getpass('Enter your password:')
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

def saveBrowserPassword(website, username, password):

   print("Browser password received.")
   
   key = key_main()
   encrypted_password = encrypt_password(password,key)

   if os.path.exists('passwords.json'):
      with open ('passwords.json','r') as file:
         data = json.load(file)
        
         
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
         key = key_main()
                  
      if not passwords:
         print('No saved password yet')
      else:
         for index, account in enumerate(passwords):
           encrypted_password = account['Password']
           decrypted_password = decrypt_password(encrypted_password,key)
           print(f'{index + 1}. Website ==> {account['Website']}\n Username ==> {account['Username']}\n Password ==> {decrypted_password}')

         
def password_edit():
   
   if os.path.exists('passwords.json'):
      websiteEdit = input('Input name of website ').title()
      with open("passwords.json","r") as file:
         data = json.load(file)
         for extreme in data['passwords']:
            if extreme['Website'] == websiteEdit:
                print('Website found!')
                passwordChange = getpass.getpass('Enter new password here')
                key = key_main()
                newly_encrypted = encrypt_password(passwordChange,key)

                extreme['Password'] = newly_encrypted
                with open("passwords.json","w") as file:
                   json.dump(data,file, indent = 4)

                print('Password changed successfully')
                break
         else:
            print('No website match!')
   else:
      print('No saved passwords yet')


def delete_password():
   
   if os.path.exists('passwords.json'):
      password_delete = input('Input website you want to delete').title()
      with open("passwords.json") as file:
         data = json.load(file)
         passwords = data['passwords']
         for extreme in passwords:
            if extreme['Website'] == password_delete:
               passwords.remove(extreme)
               with open('passwords.json','w') as file:
                  json.dump(data,file, indent = 4)
               print('Password deleted successfully')
               break
         else:
            print('No website match')
   else:
      print('No saved passwords yet')


def search_password():

   if os.path.exists('passwords.json'):
      password_search = input('Input name of website ').title()
      with open('passwords.json','r') as file:
         data = json.load(file)
         for extreme in data['passwords']:
            if extreme['Website'] == password_search:
               password = extreme['Password'] 
               key = key_main()
               currentPassword = decrypt_password(password , key)
               print(f'Website  ===> {extreme['Website']}')
               print(f'Username ===> {extreme['Username']}')
               print(f'Password ===> {currentPassword}')
               break
         else:
            print('Website does not exist in saved passwords')
   else:
      print('No saved passwords yet')


def ask_to_save(accountName,password):
   while True:
      answer = input('Do you want to save password ?(yes/no):').strip().lower()

      if answer == 'yes':
         enterPassword()
         print('Password saved successfully')
         break
      elif answer == 'no':
         print('Password was not saved')
         break
      else:
         print('Pleas enter yes or no.')




   

def menu():
   while True:
      print("=========================")
      print("MENU SECTION")
      print("=========================")  
      print("Please pick an option")
      print("1. Add password")
      print("2. View password")
      print("3. Edit password")
      print("4. Delete password")
      print("5. Search password")
      print("6. Check password strength")
      print("7. Suggest strong password")
      print("8. Exit Menu")
      

      choice = int(input('What would you like to do? Input an option'))
      if choice == 1:
         enterPassword()
      elif choice == 2:
         print('Input your master pin')
         pinConfirm = input()
         if pinConfirm == entered_pin:
           view_password()
         else:
            print('Pin is incorrect!')
      elif choice == 3:
         password_edit()
      elif choice == 4:
         delete_password() 
      elif choice == 5:
         search_password() 
      elif choice == 8:
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
      pin = getpass.getpass('Create your 4-digit master pin :')
      if len(pin) == 4 and pin.isdigit():
       confirm_pin = getpass.getpass('Confirm pin')
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
        