
import sqlite3
import re
import vonage
#FIRST I CREATE THE DATABASE
print("WLECOME TO THE HIGH SCHOOL BOOKING SYSTEM")
def create_tables () :

    db = sqlite3.connect("database_db.db")
    cursor = db.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS booking(
        ID INTEGER PRIMARY KEY,
        First_Name TEXT NOT NULL,
        Last_Name TEXT NOT NULL,
        School_Name TEXT NOT NULL,
        Depature_Date DATETIME NOT NULL,
        Start TEXT NOT NULL,
        Finish TEXT NOT NULL,
        Contact_Number TEXT NOT NULL
        
        
        )
        '''
    )
    
 
    

def booking_table(booking_details) :
    


    
  

    

    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO booking(id,first_Name,last_Name,school_Name,depature_date,start,finish,contact_number,No_of_Seats)
            VALUES(?,?,?,?,?,?,?,?,?)
            ''',(booking_details['ID'],booking_details['first_Name'],booking_details['last_Name'],booking_details['school_Name'],booking_details['depature_date'],booking_details['start'],booking_details['finish'],booking_details['contact_number'],booking_details['seats'])
        )
   
    


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
        start = input("Enter County you will be reporting from : ")
        if not start :
            raise ValueError("Invalid Input. Please enter a County")
        else :
            booking_details['start'] = start
            break
    while True :
        finish = input("Enter Destination headed to : ")
        if not finish :
            raise ValueError("Invalid input. Please enter a final destination")
        else :
            booking_details['finish'] = finish
            break
    while True :
        contact_number = input("Enter your contact number (10 digits starting with 254) : ")
        if not contact_number :
            raise ValueError("Invalid Input. Please enter your contact details")
        else :
            booking_details['contact_number'] = contact_number
            break
    while True :
        number_of_seats = input("Please input how many seats you would like to book : ")
        if not number_of_seats :
            raise ValueError("Invalid Input")
        else :
            booking_details['seats'] = number_of_seats
            break

    print("Information added successfully")
    return booking_details




     


def search_routes() :
    starting_location = input("Enter your original location : ")
    final_destination = input("Enter your final destination : ")
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''  
            SELECT * FROM routes WHERE Origin = ? AND Destination = ?
            ''',(starting_location,final_destination)
            )
        routes = cursor.fetchall()
        if routes :
            for route in routes :
                print(f"ROUTE FOUND !!")
                print(f"Route ID : {route[0]}")
                print(f"Route Origin : {route[1]}")
                print(f"Route Destination : {route[2]}")
                print(f"Travel Time : {route[3]}")
                print(f"Depature : {route[4]}")
                print(f"Stops : {route[5]}")
                print(f"Company : {route[6]}")
                print(f"Route Number : {route[7]}")
                print()
                
            else  :
                print(f"Route not found")
search_routes()
     


def sending_message (booking_details) :
    #API_KEY = "6d7d76af"
    #Client_Secret = "19Ug99bNVFaqIZjq"
    client = vonage.Client(key="6d7d76af", secret="19Ug99bNVFaqIZjq")
    sms = vonage.Sms(client)
   
    studentID = booking_details["ID"]
    first = booking_details["first_Name"]
    last = booking_details["last_Name"]
    name_of_school = booking_details["school_Name"]
    depart = booking_details["depature_date"]
    station = booking_details["start"]
    destination = booking_details['finish']
    


    responseData = sms.send_message(
        {
            "from" : "VonageAPI",
            "to" : "254757448550",
            "text" : f"Hello. This is confirmation that {first} {last} of Student ID : {studentID} who is in {name_of_school} will be departing on {depart} from {station} headed to {destination}"
                
        }
    )
    if responseData['messages'][0]['status'] == "0" :
        print("Sent")
    else :
        print("Not sent")
    

booking_details = user_input()
booking_table(booking_details)
sending_message(booking_details)
  
 

    
        
   

         
