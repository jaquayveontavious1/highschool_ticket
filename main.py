import sqlite3
import re
import vonage
#FIRST I CREATE THE DATABASE

db = sqlite3.connect("database_db.db")
cursor = db.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS highschool_booking(
    ID INTEGER PRIMARY KEY,
    First_Name TEXT NOT NULL,
    Last_Name TEXT NOT NULL,
    School_Name TEXT NOT NULL,
    Depature_Date DATETIME NOT NULL,
    County TEXT NOT NULL,
    Contact_Number TEXT NOT NULL 
    
    )
    '''
)
db.commit()

def booking_table(booking_details) :
    


    
  

    

    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO  highschool_booking(id,first_Name,last_Name,school_Name,depature_date,county,contact_number)
            VALUES(?,?,?,?,?,?,?)
            ''',(booking_details['ID'],booking_details['first_Name'],booking_details['last_Name'],booking_details['school_Name'],booking_details['depature_date'],booking_details['county'],booking_details['contact_number'])
        )
    db.commit()
    


def user_input () :
    booking_details = {}

    while True :
        try :

            id = input("Enter the Student's ID : ")
            if not id.isdigit() or len(id) != 3 :
                print("Invalid Input. Please enter 3 digits")
            else :
                booking_details['ID'] = id
                break
        except ValueError :
            print("Enter a valid Integer")
    while True :
        first_Name = input("Enter Student's First Name : ").capitalize()
        if not first_Name :
            raise ValueError("Invalid Input. Please enter a name.")
        else :
            booking_details['first_Name'] = first_Name
            break
    while True :
        last_Name = input("Enter Student's Last Name : ").capitalize()
        if not last_Name :
            raise ValueError("Invalid Input. Please enter a name")
        else :
            booking_details['last_Name'] = last_Name
            break
    while True :
        school_Name = input("Enter Name of School for Student : ")
        if not school_Name :
            raise ValueError("Please enter name of the school")
        else :
            booking_details['school_Name'] = school_Name
            break
    while True :
        depature_date = input("Enter a depature data using the format (DD-MM-YYYY) : ")
        pattern = r'^\d{2}-\d{2}-\d{4}$'
        if not depature_date :
            raise ValueError("Invalid Input. Please enter a depature date.")
        elif re.match (pattern,depature_date) :
            booking_details['depature_date'] = depature_date
            break
    while True :
        county = input("Enter County you will be reporting from : ")
        if not county :
            raise ValueError("Invalid Input. Please enter a County")
        else :
            booking_details['county'] = county
            break
    while True :
        contact_number = input("Enter your countact number (10 digits starting with 254) : ")
        if not contact_number :
            raise ValueError("Invalid Input. Please enter your contact details")
        else :
            booking_details['contact_number'] = contact_number
            break

    return booking_details
booking_details = user_input()
print("Information added successfully")
def sending_message (booking_details) :
    API_KEY = "0a6c1a67"
    Client_Secret = "MGrYNiLuhbvK0uy2"
    client = vonage.Client(key=API_KEY,secret=Client_Secret)
    sms = vonage.Sms(client)
    studentID = booking_details["ID"]
    first = booking_details["first_Name"]
    last = booking_details["last_Name"]
    name_of_school = booking_details["school_Name"]
    depart = booking_details["depature_date"]
    station = booking_details["county"]
    contact = booking_details["contact_number"]


    responseData = sms.send_message(
        {
            "from" : "VonageAPI",
            "to" : "254714414432",
            "text" : f"Hello. This is confirmation that {first} {last} of Student ID : {studentID} who is in {name_of_school} will be departing on {depart} and will be reporting to {station} Station"
                
        }
    )
    if responseData['messages'][0]['status'] == "0" :
        print("Sent")
    else :
        print("Not sent")
    print(contact)
sending_message(booking_details)
booking_table(booking_details)
    
        
   

         
