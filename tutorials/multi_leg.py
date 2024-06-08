import sqlite3
#CREATE THE DATABASE
#INSERTING THE INFORMATION
# ASKING FOR USER INPUT
#CREATING AN ALGORITHM

def create_table () :
    db = sqlite3.connect("database_db.db")
    cursor = db.cursor()

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS routes (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Origin TEXT NOT NULL,
        Destination TEXT NOT NULL,
        Travel_Time INTEGER,
        Depature DATETIME NOT NULL,
        Stops TEXT ,
        Company TEXT NOT NULL,
        Route_Number TEXT NOT NULL 
        )
        '''
    )
    db.commit()

create_table()



def insert_info (database) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO routes (id,origin,destination,travel_time,depature,stops,company,route_number)
            VALUES(?,?,?,?,?,?,?,?)
            ''', (database['id'],database['origin'],database['destination'],database['travel_time'],database['depature'],database['stops'],database['company'],database['route_number'])
        )
        db.commit()
def info_data () :


    id = input("Enter an ID (3 digits) : ")
    origin = input("Enter your original destination : ")
    destination = input("Enter your Destination : ")
    travel_time = input("Enter Duration of Trip : ")
    depature = input("Enter date of depature : ")
    stops = input("Enter stops if any : ")
    company = input("Enter Company Bus : ")
    route_number = input("Enter your route number : ")

    database = {
        "id" : id,
       "origin" : origin,
        "destination" : destination,
        "travel_time" : travel_time,
        "depature" : depature,
        "stops" : stops,
        "company" : company,
        "route_number" : route_number
    }
    return database
database = info_data()


insert_info(database)

def search_routes (database) :
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
                print(f"Route found !!")
                print(f"Route ID : {route[0]}")
                print(f"Route Origin : {route[1]}")
                print(f"Route Destination : {route[2]}")
                print(f"Travel Time : {route[3]}")
                print(f"Depature : {route[4]}")
                print(f"Stops : {route[5]}")
                print(f"Company : {route[6]}")
                print(f"Route Number : {route[7]}")
                print()
            
        else :
            print("Route not found")
search_routes(database)




