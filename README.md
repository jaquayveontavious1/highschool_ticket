High School Bus Ticket Booking System
Overview
This project is a Python-based application designed to allow Kenyan high school students to book bus tickets for their school commute. The application collects booking details from the user, stores them in an SQLite3 database, and sends a confirmation message via SMS using an API.

Features
Collects user input for bus ticket booking.
Stores booking details in an SQLite3 database.
Sends a confirmation SMS to the user with booking details.
Requirements
Python 3.x
Libraries: sqlite3, requests
Setup and Installation
Clone the Repository:

sh
Copy code
git clone https://github.com/yourusername/bus-ticket-booking.git
cd bus-ticket-booking
Install Required Libraries:

sh
Copy code
pip install requests
Setup SMS API:

Register for an account with a suitable SMS API provider (e.g., Twilio, Africa's Talking, Nexmo).
Obtain your API credentials (API key, Account SID, Auth Token, etc.).
Database Schema
The SQLite database has a single table named bookings with the following columns:

id: INTEGER PRIMARY KEY AUTOINCREMENT
student_name: TEXT NOT NULL
school_name: TEXT NOT NULL
bus_route: TEXT NOT NULL
departure_time: TEXT NOT NULL
phone_number: TEXT NOT NULL
Usage
Run the Application:

sh
Copy code
python main.py
Input Details:

The program will prompt you to enter the following details:
Student's name
School's name
Bus route
Departure time
Phone number
Receive Confirmation:

After inputting the details, the program stores the information in the database.
An SMS confirmation is sent to the provided phone number with the booking details.
Example Workflow
Start the program.
Enter the student's name, school name, bus route, departure time, and phone number when prompted.
The program validates the inputs and stores them in the SQLite3 database.
A confirmation message is sent to the user's phone number via SMS API.
Error Handling
The program includes basic error handling for:
Invalid input formats (e.g., phone number).
Database connection issues.
SMS API request failures.
Contributions
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License.

Contact
For any questions or support, please contact:

Your Name: kanyingitiffany.email@example.com