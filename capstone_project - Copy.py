# COVID-19 PATIENTS DATA
patients_data=[ 
    {'nin':317501, 'name': 'William Thomas', 'age': 31, 'gender':'Male', 'address': 'Cipete', 'lab code':'C17.1', 'ct value': 19,'symptom classification':'Moderate', 'dose number of vaccination':'Second'},
    {'nin':317502, 'name': 'Deanna Barnum', 'age': 25, 'gender':'Female', 'address': 'Gandaria', 'lab code':'C17.2', 'ct value': 22,'symptom classification':'Mild', 'dose number of vaccination':'Third'},
    {'nin':317503, 'name': 'John Doe', 'age': 52, 'gender':'Male', 'address': 'Cilandak', 'lab code':'C18.1', 'ct value': 17,'symptom classification':'Severe', 'dose number of vaccination':'Second'},
    {'nin':317504, 'name': 'Robert Charles', 'age': 65, 'gender':'Male', 'address': 'Fatmawati', 'lab code':'C19.1', 'ct value': 14,'symptom classification':'Critical', 'dose number of vaccination':'First'},
    {'nin':317505, 'name': 'Sarah Samantha', 'age': 17, 'gender':'Female', 'address': 'Pondok Indah', 'lab code':'C19.2', 'ct value': 18,'symptom classification':'Mild', 'dose number of vaccination':'Third'},
    {'nin':317506, 'name': 'San Anderson', 'age': 19, 'gender':'Male', 'address': 'Lebak Bulus', 'lab code':'C19.3', 'ct value': 23,'symptom classification':'Moderate', 'dose number of vaccination':'Third'}
    ] 

# Display of Login Menu
def login():
    import getpass
    username='Covid19'
    password='patients2022'
    print('''
*******************  WELCOME TO THE COVID-19 PATIENTS DATA COLLECTION SYSTEM  *******************
*******************                     MAYAPADA HOSPITAL                     *******************''')
    print()
    print('Login')
    print()
    for login in range(2,-1,-1):
        a= input('Username  : ')
        b= getpass.getpass('Password  : ')
        if a==username and b==password:
            print()
            print('You have successfully entered The Main Menu!')
            break
        else:
            if login==2:
                print(f'The username or password you entered is incorrect. You have the option to login 2 more times!')
                print()
            elif login==1:
                print(f'The username or password you entered is incorrect. You have the option to login 1 more time!')
                print()
            else:
                print('The username or password you entered is incorrect. You are unable to login!')
                exit()

# MAIN MENU
def main_menu():
    while True:
        print()
        menu=int(input('''==========================================  MAIN MENU  ========================================== 

1. Information of Covid-19 Patients Data
2. Create Data on Covid-19 Patient Data
3. Update Data on Covid-19 Patient Data
4. Delete Data on Covid-19 Patient Data
5. Exit

Please enter menu 1-5: '''))
        print()
        if menu == 1:
            first_menu()
        elif menu==2:
            second_menu()
        elif menu==3:
            third_menu()
        elif menu==4:
            fourth_menu()
        elif menu==5:
            while True:
                exit_menu=input("Do you really want to exit? (Y/N): ")
                exit_menu=exit_menu.upper()
                if exit_menu=='Y':
                    print('Thank you! Stay healthy and happy:)')
                    exit()
                elif exit_menu=='N':
                    break
                else:
                    print("Please enter 'Y' to continue and 'N' to cancel!")
                    continue
        else:
            print('The menu option you entered is incorrect. Please enter menu 1-5!')
            continue  

# FIRST MENU (Read Data)
def first_menu():
    while True:
        print()
        read_data=int(input(f'''****************************** INFORMATION OF COVID-19 PATIENTS DATA ****************************

1. Information of All Covid-19 Patients Data
2. Search Data on Covid-19 Patient Data
3. Covid-19 Patient Reports
4. Back to The Main Menu

Please enter menu 1-4: '''))
        print()
        if read_data==1:
            print('INFORMATION OF ALL COVID-19 PATIENTS DATA') 
            print ()
            if len(patients_data)==0:
                print('Sorry, patient data is not available!')
            else:
                print(f"{'NO':<4}| {'NIN':<10}| {'NAME':<15}| {'AGE':<6}| {'GENDER':<9}| {'ADDRESS':<15}| {'LAB CODE':<9}| {'CT VALUE':<9}| {'SYMPTOM classification':<22}| {'DOSE NUMBER OF VACCINATION':<28}|")
                for i in range(len(patients_data)):
                    nin = patients_data[i]['nin']
                    name = patients_data[i]['name']
                    age = patients_data[i]['age']
                    gender = patients_data[i]['gender']
                    address = patients_data[i]['address']
                    labcode = patients_data[i]['lab code']
                    ctvalue = patients_data[i]['ct value']
                    symptom = patients_data[i]['symptom classification']
                    vaccination = patients_data[i]['dose number of vaccination']
                    print(f"{i+1:<4}| {nin:<10}| {name:<15}| {age:<6}| {gender:<9}| {address:<15}| {labcode:<9}| {ctvalue:<9}| {symptom:<22}| {vaccination:<28}|")
        elif read_data==2:
            while True:
                print('SEARCH DATA ON COVID-19 PATIENT DATA')
                print()
                nin=int(input('Enter The Patient NIN      : '))
                print()
                for i in range(len(patients_data)):
                    if nin == patients_data[i]['nin']:
                        print(f'''
COVID-19 PATIENT DATA
NIN                        : {patients_data[i]["nin"]}
Name                       : {patients_data[i]["name"]}
Age                        : {patients_data[i]["age"]}
Gender                     : {patients_data[i]["gender"]}
Address                    : {patients_data[i]["address"]}
Lab Code                   : {patients_data[i]["lab code"]}
CT Value                   : {patients_data[i]["ct value"]}
Symptom classification      : {patients_data[i]["symptom classification"]}
Dose Number of Vaccination : {patients_data[i]["dose number of vaccination"]}''')
                        break
                    elif i==len(patients_data)-1:
                        print('Sorry, patient data is not available!')
                        print()
                        continue
                break
        elif read_data==3:
            report()
        elif read_data==4:
            exit_menu()
        else:
            print("Please enter menu 1, 2, 3 or 4!")

# Covid-19 Patient Reports
def report():
    while True:
        print()
        print('************************************ COVID-19 PATIENT REPORTS ***********************************')
        print()
        based = input('Patient Reports based on: ')
        based = based.lower()
        if based=='gender':
            female = 0
            male = 0
            for a in range(len(patients_data)):
                if patients_data[a]['gender'] == 'Female' :
                    female += 1
                elif patients_data[a]['gender'] == 'Male' :
                    male += 1
            p_female = round((female/(female+male)*100),1)
            p_male = round((male/(female+male)*100),1)
            print(f'''
========================================
COVID-19 PATIENT REPORTS BASED ON GENDER

Total FEMALE          : {female}
Percentage            : {p_female}%

Total MALE            : {male}
Percentage            : {p_male}%
========================================''')   
            break

        elif based=='symptom classification':
            mild = 0
            moderate = 0
            severe = 0
            critical = 0
            for b in range(len(patients_data)):
                if patients_data[b]['symptom classification'] == 'Mild' :
                    mild += 1
                elif patients_data[b]['symptom classification'] == 'Moderate' :
                    moderate += 1
                elif patients_data[b]['symptom classification'] == 'Severe' :
                    severe += 1
                elif patients_data[b]['symptom classification'] == 'Critical' :
                    critical += 1
            p_mild = round((mild/len(patients_data)*100),1)
            p_moderate = round((moderate/len(patients_data)*100),1)
            p_severe = round((severe/len(patients_data)*100),1)
            p_critical = round((critical/len(patients_data)*100),1)
            print(f'''
=======================================================
COVID-19 PATIENT REPORTS BASED ON SYMPTOM classification

Total Patients with MILD Symptoms     : {mild}
Percentage                            : {p_mild}%

Total Patients with MODERATE Symptoms : {moderate}
Percentage                            : {p_moderate}%

Total Patients with SEVERE Symptoms   : {severe}
Percentage                            : {p_severe}%

Total Patients with CRITICAL Symptoms : {critical}
Percentage                            : {p_critical}%
=======================================================''') 
            break       

        elif based=='dose number of vaccination':
            first = 0
            second = 0
            third = 0
            for c in range(len(patients_data)):
                if patients_data[c]['dose number of vaccination'] == 'First' :
                    first += 1
                elif patients_data[c]['dose number of vaccination'] == 'Second' :
                    second += 1
                elif patients_data[c]['dose number of vaccination'] == 'Third' :
                    third += 1
            p_first = round((first/len(patients_data)*100),1)
            p_second = round((second/len(patients_data)*100),1)
            p_third = round((third/len(patients_data)*100),1)
            print(f'''
============================================================
COVID-19 PATIENT REPORTS BASED ON DOSE NUMBER OF VACCINATION

Total Patients with FIRST Dose Vaccination  : {first}
Percentage                                  : {p_first}%

Total Patients with SECOND Dose Vaccination : {second}
Percentage                                  : {p_second}%

Total Patients with THIRD Dose Vaccination  : {third}
Percentage                                  : {p_third}%
============================================================''')
            break
        
        else:
            print("Patient reports are not available. Please enter 'Gender', 'Symptom classification', or 'Symptom classification'!")
            continue

# SECOND MENU (Create Data)
def second_menu():
    while True:
        print()
        create_data=int(input(f'''****************************** CREATE DATA ON COVID-19 PATIENT DATA *****************************

1. Create Data on Covid-19 Patient data
2. Back to The Main Menu

Please enter menu 1 or 2: '''))
        print()
        if create_data==1:
            print('CREATE DATA ON COVID-19 PATIENT DATA')
            print()
            nin =int(input('Enter the Patient NIN      : '))
            for i in range(len(patients_data)):
                if nin == patients_data[i]['nin']:
                    print()
                    print('This patient data already exists!')
                    print()
                    continue
                elif i == len(patients_data)-1:
                    name        = input('Name                       : ')
                    age         = int(input('Age                        : '))
                    gender      = input('Gender                     : ')
                    address     = input('Address                    : ')
                    labcode     = input('Lab Code                   : ')
                    ctvalue     = int(input('CT Value                   : '))
                    symptom     = input('Symptom classification      : ')
                    vaccination = input('Dose Number of Vaccination : ')
                    while True:
                        question  = input('Do you really want to create data? (Y/N): ')
                        print()
                        question  = question.upper()
                        if question == 'Y':
                            patients_data.append({'nin': nin, 'name': name, 'age': age, 'gender': gender, 'address': address, 'lab code': labcode, 'ct value': ctvalue,'symptom classification': symptom, 'dose number of vaccination': vaccination})
                            print('The data successfully saved!')
                            break
                        elif question == 'N':
                            print('The data is not saved!')
                            break
                        else: 
                            print("Please enter 'Y' to continue and 'N' to cancel!")
                            print()
                            continue
        elif create_data==2:
            exit_menu()
        else:
            print("Please enter menu 1 or 2!")  

# THIRD MENU (Update Data)
def third_menu():
    while True:
        print()
        update_data= int(input('''****************************** UPDATE DATA ON COVID-19 PATIENT DATA *****************************

1. Update Data on Covid-19 Patient Data
2. Back to The Main Menu

Please enter menu 1 or 2: '''))
        print()
        if update_data==1:
            print('UPDATE DATA ON COVID-19 PATIENT DATA')
            print()
            nin=int(input('Enter the Patient NIN      : '))
            print()
            for i in range(len(patients_data)):
                if nin == patients_data[i]['nin']:
                    print(f'''
COVID-19 PATIENT DATA
NIN                        : {patients_data[i]["nin"]}
Name                       : {patients_data[i]["name"]}
Age                        : {patients_data[i]["age"]}
Gender                     : {patients_data[i]["gender"]}
Address                    : {patients_data[i]["address"]}
Lab Code                   : {patients_data[i]["lab code"]}
CT Value                   : {patients_data[i]["ct value"]}
Symptom classification      : {patients_data[i]["symptom classification"]}
Dose Number of Vaccination : {patients_data[i]["dose number of vaccination"]}''')
                    while True:
                        print()
                        question=input('Do you really want to update patient data? (Y/N): ')
                        question=question.upper()
                        print()
                        if question=='Y':
                            update=input('Enter the data you want to update : ')
                            update=update.lower()
                            if update=='nin':
                                print('Sorry, NIN cannot be changed!')
                                continue
                            elif update in patients_data[i]:
                                key_baru= input(f'Enter new "{update}" : ')
                                while True:
                                    question2= input(f'Do you really want to save this new data? (Y/N): ')
                                    question2= question2.upper()
                                    if question2=='Y':
                                        patients_data[i][update]=key_baru
                                        print()
                                        print(f'New "{update}" successfully updated!')
                                        break
                                    elif question2=='N':
                                        print(f'New "{update}" is not updated!')
                                        break
                                    else:
                                        print("Please enter 'Y' to continue and 'N' to cancel!")
                                        continue
                                break
                            else:
                                print(f"Sorry, patient {update} data is not available!")
                                break
                        elif question=='N':
                            print('Patient data is not updated!')
                            break
                        else:
                            print("Please enter 'Y' to continue and 'N' to cancel!")
                            continue
                elif i==len(patients_data)-1:
                    print('Sorry, patient data is not available!')
                    break
        elif update_data==2:
            exit_menu()
        else:
            print("Please enter menu 1 or 2!")
 
# FOURTH MENU (Delete Data)
def fourth_menu():
    while True:
        print()
        delete_data=int(input('''********************************* DELETE DATA ON COVID-19 PATIENT DATA *********************************

1. Delete Data on Covid-19 Patient Data
2. Back to The Main Menu

Please enter menu 1 or 2: '''))
        print()
        if delete_data==1: 
            print('DELETE DATA ON COVID-19 PATIENT DATA')
            print()
            nin=int(input('Enter the Patient NIN : '))
            print()
            for i in range(len(patients_data)):
                if nin == patients_data[i]['nin']:
                    print(f'''
COVID-19 PATIENT DATA
NIN                        : {patients_data[i]["nin"]}
Name                       : {patients_data[i]["name"]}
Age                        : {patients_data[i]["age"]}
Gender                     : {patients_data[i]["gender"]}
Address                    : {patients_data[i]["address"]}
Lab Code                   : {patients_data[i]["lab code"]}
CT Value                   : {patients_data[i]["ct value"]}
Symptom classification      : {patients_data[i]["symptom classification"]}
Dose Number of Vaccination : {patients_data[i]["dose number of vaccination"]}''')
                    print()
                    while True:
                        question=input('Do you really want to delete patient data? (Y/N): ')
                        question=question.upper()
                        if question=='Y':
                            print('Patient data deleted successfully!')
                            del patients_data[i]
                            break
                        elif question=='N':
                            print('Patient data is not deleted!')
                            break
                        else: 
                            print("Please enter 'Y' to continue and 'N' to cancel!")
                            continue
                elif i==len(patients_data)-1:
                    print('Sorry, patient data is not available!')
                    print()
                    break
        elif delete_data==2:
            exit_menu()
        else:
            print("Please enter menu 1 or 2!")
        
# Menu Exit
def exit_menu():
    while True:
        exit=input("Do you really want to go back to The Main Menu? (Y/N): ")
        exit=exit.upper()
        if exit=='Y':
            main_menu()
        elif exit=='N':
            break
        else:
            print("Please enter 'Y' to continue and 'N' to cancel!")
            continue

# Aplikasi
login()
main_menu()






                   














