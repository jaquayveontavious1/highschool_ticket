import sqlite3
import re
import bcrypt
def create_table () :

    db = sqlite3.connect("database_db.db")
    cursor = db.cursor()

    #CREATING A TABLE

    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS administration (
        ID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        Role TEXT NOT NULL
        )
        '''
    )
  
    cursor.execute (
        '''
        CREATE TABLE IF NOT EXISTS roles (
        role_id INTEGER PRIMARY KEY,
        role_name TEXT NOT NULL UNIQUE  
        )
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS permissions (
        permission_id INTEGER PRIMARY KEY,
        permission_name TEXT NOT NULL UNIQUE
        )
        '''
    )
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS role_permissions (
        role_id INTEGER,
        permission_id INTEGER,
        FOREIGN KEY (role_id) REFERENCES roles(role_id),
        FOREIGN KEY (permission_id) REFERENCES permissions (permission_id)
        )
        '''
    )
    db.commit()
create_table()
def details_table(details) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO administration (ID,Username,Email,Password,Role)
            VALUES(?,?,?,?,?)
            ''',(details['ID'],details['username'],details['email'],details['password'],details['role'])
        )
        

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(),salt)
    return hashed_password

def add_role (role_name) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO roles (role_name) VALUES(?)
            ''',(role_name,)
        )
        db.commit()

def add_permissions(permission_name) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute(
            '''
            INSERT OR IGNORE INTO permissions (permission_name) VALUES (?)
            ''',(permission_name,)
        )
        db.commit()

def assign_roles_to_permission(role_name,permission_name) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute (
            '''
            SELECT role_id FROM roles WHERE role_name = ?
            ''',(role_name,)
            
        )
        role_id = cursor.fetchone()[0]
        cursor.execute(
            '''
            SELECT permission_id FROM permissions WHERE permission_name = ?
            ''',(permission_name,)
        )
        permission_id = cursor.fetchone()[0]
        cursor.execute(
            '''
            INSERT INTO role_permissions (role_id,permission_id)
            VALUES (?,?)
            ''',(role_id,permission_id)
        )
        db.commit()
add_role("Admin")
add_role("Parent")
add_role("Student")

add_permissions("View Student Info")
add_permissions("Manage Bus Routes")
add_permissions("Manage Users")
add_permissions("Set system configurations")
add_permissions("Access Detailed Reports")
add_permissions("Manage Security")
add_permissions("View Booked Trips")
add_permissions("Book and Cancel Trips")
add_permissions("Update Student Info")
add_permissions("Manage Payment Methods")
add_permissions("View Notification")
add_permissions("View available buses")
add_permissions("Access Trip Details")
add_permissions("View personal booking history")
add_permissions("Request for additional rides")

assign_roles_to_permission("Admin","View Student Info")
assign_roles_to_permission("Admin","Manage Bus Routes")
assign_roles_to_permission("Admin","Manage Users")
assign_roles_to_permission("Admin","Set system configurations")
assign_roles_to_permission("Admin","Access Detailed Reports")
assign_roles_to_permission("Admin","Manage security")

assign_roles_to_permission("Parent","View Booked Trips")
assign_roles_to_permission("Parent","Book and Cancel Trips ")
assign_roles_to_permission("Parent","Update Student Info")
assign_roles_to_permission("Parent","Manage Payment Methods")
assign_roles_to_permission("Parent","View Notification")


assign_roles_to_permission("Student","View available buses")
assign_roles_to_permission("Student","Access Trip Details")
assign_roles_to_permission("Student","View personal booking history")
assign_roles_to_permission("Student","Request for additional rides")




def user_input () :
    details = {}
    while True :
        try :
            id = input("Enter a 3 digit number : ")
            if not id.isdigit() or len(id) != 3 :
                print("Invalid Input. Please enter 3 digits")
            else :
                details['ID'] = id
                break
        except ValueError :
            print("Enter a valid integer")
    while True :
        username = input("Please enter a username : ")
        if not username :
            raise ValueError("Invalid Input. Please enter a username")
        else :
            with sqlite3.connect("database_db.db") as db :
                cursor = db.cursor()
                cursor.execute(
                    '''
                    SELECT 1 FROM administration WHERE Username = ?
                    ''',(username,)
                )
                if cursor.fetchone():
                    print("Username has already been used")
                else :
                    details['username'] = username
                    break
    while True :
        email = input("Enter your email address (example@gmail.com) : ")
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern,email) :
            details['email'] = email
            break
        else :
            print("Invalid email address")
    while True :
        for _ in range(2) :
            password = input("Enter your password: ")
            if password != password :
                print("Access Denied")
            else :
                hashed_password = hash_password(password)
                details['password'] = hashed_password
                break
        else :
            continue
        break
    while True :
        role = input("Please enter your role : ")
        with sqlite3.connect("database_db.db") as db :
            cursor = db.cursor()
            cursor.execute("SELECT role_id FROM roles WHERE role_name = ? ", (role,))
            if cursor.fetchone() :
                details['role'] = role
                break
            else :
                print("Invalid role")
    return details

def check_permission (username,permission_name) :
    with sqlite3.connect("database_db.db") as db :
        cursor = db.cursor()
        cursor.execute("SELECT role_id FROM administration Username = ? ",(username,))
        role_id = cursor.fetchone()[0]
        cursor.execute("SELECT permission_id FROM permissions WHERE permissions = ? ",(permission_name))
        permission_id = cursor.fetchone()[0]
        cursor.execute("SELECT 1 FROM role_permissions WHERE role_id = ? AND permission_id = ? ",(role_id,permission_id))
        return cursor.fetchone() is not None
if check_permission("Admin","View Student Info") :
        print("Permission granted")
else :
        print("Permision denied")
details = user_input()
print("Information added successfully")

details_table(details)