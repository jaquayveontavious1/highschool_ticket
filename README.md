<h1><b><strong>High School Bus Ticket Booking System</strong></b></h1>
<h2><br>Overview </br></h2>
This project is a Python-based application designed to allow Kenyan high school students to book bus tickets for their school commute. The application collects booking details from the user, stores them in an SQLite3 database, and sends a confirmation message via SMS using an API.
<br></br>
<h2><b>Features</b></h2>
<ul>
<li>Collects user input for bus ticket booking.</li>
<li>Stores booking details in an SQLite3 database.</li>
<li>Sends a confirmation SMS to the user with booking details.</li>
</ul>
<h2><b>Requirements</b></h2>
<ul>
<li>Python 3.x</li>
<li>Libraries: sqlite3, requests</li>
</ul>

<h2><b>Setup and Installation</b></h2>
<h3><b>Clone the Repository:</b></h3>


<div style='border: 1px solid #000; padding: 10px; background-color:#f9f9f9'>
<pre>
git clone https://github.com/jaquayveontavious1/bus-ticket-booking.git
cd bus-ticket-booking
</pre>
</div>
<h3><b>Install Required Libraries:</b></h3>


<div style= 'border 1px solid #000; padding: 10px; background-color: #f9f9f9'>
<pre>
pip install requests
</pre>
</div>
<h3><b>Setup SMS API:</b></h3>
<ul>
<li>Register for an account with a suitable SMS API provider (e.g., Twilio, Africa's Talking, Nexmo).</li>
<li>Obtain your API credentials (API key, Account SID, Auth Token, etc.).</li>
</ul>
<h2><b>Database Schema</b></h2>
The SQLite database has a single table named bookings with the following columns:
<ul>
<li>id: INTEGER PRIMARY KEY AUTOINCREMENT</li>
<li>student_name: TEXT NOT NULL</li>
<li>school_name: TEXT NOT NULL</li>
<li>bus_route: TEXT NOT NULL</li>
<li>departure_time: TEXT NOT NULL</li>
<li>phone_number: TEXT NOT NULL</li>
</ul>

<h2><b>Usage</b></h2>
<h3><b>Run the Application:</b></h3>

<div style='border: 1px solid #000; padding: 10px;background-color: #f9f9f9'>
<pre>
python main.py
</pre>
</div>
<h3><b>Input Details:</b></h3>

The program will prompt you to enter the following details:
<ul>
<li>Student's name</li>
<li>School's name</li>
<li>Bus route</li>
<li>Departure time</li>
<li>Phone number</li>
</ul>
<h3><b>Receive Confirmation:</b></h3>
<ul>
<li>After inputting the details, the program stores the information in the database.</li>
<li>An SMS confirmation is sent to the provided phone number with the booking details.</li>
</ul>
<h2><b>Example Workflow</b></h2>
<ol>
<li>Start the program.</li>
<li>Enter the student's name, school name, bus route, departure time, and phone number when prompted.</li>
<li>The program validates the inputs and stores them in the SQLite3 database.</li>
<li>A confirmation message is sent to the user's phone number via SMS API.</li>
</ol>
<h3><b>Error Handling</b></h3>
The program includes basic error handling for:
<ul>
<li>Invalid input formats (e.g., phone number).</li>
<li>Database connection issues.</li>
<li>SMS API request failures.</li>
</ul>
<h3><b>Contributions</b></h3>
Contributions are welcome! Please fork the repository and create a pull request with your changes.

<h3><b>License</b></h3>
This project is licensed under the MIT License.

<h3><b>Contact</b></h3>
For any questions or support, please contact:
<ul>
<li>Your Name: kanyingitiffany@gmail.com</li>
</ul>