# PharmaProject Flask Backend Setup Instructions

1. Install Python 3.8+ and PostgreSQL on your system.
2. Create a PostgreSQL database named `pharmadb` and a user with access.
3. Update the `backend/.env` file with your PostgreSQL credentials:
   DATABASE_URL=postgresql://<user>:<password>@localhost/pharmadb
4. Open a terminal in the `backend` directory and run:
   pip install -r requirements.txt
5. Initialize the database tables:
   python
   >>> from app import db
   >>> db.create_all()
   >>> exit()
6. Start the Flask server:
   python app.py

Your backend API will be running at http://127.0.0.1:5000/

 C:\Users\lenovo\AppData\Local\Programs\Python\Python312\python.exe app.py
 command to run at terminal


 SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';
select * from contact;
select * from newsletter_subscriber;

queries for postgreSQL