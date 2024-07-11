import mysql.connector
import streamlit as st
import hashlib
import time
from cryptography.fernet import Fernet as AES

# Define the Fernet key for encryption
fernet_key = b'rrm-9Rx_5eeVLJQRehibrO_AwjazFV_mEb7RrzcHans='
cipher = AES(fernet_key)

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital_db"
)
c = conn.cursor()

# Create tables if they do not exist
c.execute('''
    CREATE TABLE IF NOT EXISTS patients (
        pid VARCHAR(255) PRIMARY KEY,
        name TEXT,
        btype TEXT,
        gender TEXT,
        age INTEGER,
        dob TEXT,
        height INTEGER,
        weight INTEGER,
        allergies TEXT,
        medications TEXT,
        conditions TEXT,
        pTestRep TEXT,
        phone TEXT,
        emerno TEXT,
        remarks TEXT,
        time TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        did VARCHAR(255) PRIMARY KEY,
        hash TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS logbook (
        doctor_id TEXT,
        timestamp TEXT,
        patient_id TEXT
    )
''')

conn.commit()

# Patient record management class
class medRecord:
    def __init__(self):
        self.pid = ""
        self.name = ""
        self.btype = ""
        self.gender = ""
        self.age = 0
        self.dob = ""
        self.height = 0
        self.weight = 0
        self.allergies = []
        self.medications = []
        self.conditions = []
        self.pTestRep = ""
        self.phone = ""
        self.emerno = ""
        self.remarks = []
        self.time = ""

    def insRecord(self):
        self.pid = cipher.encrypt(st.text_input("Enter patient ID: ").encode())
        self.name = cipher.encrypt(st.text_input("Enter patient name: ").encode())
        self.btype = cipher.encrypt(st.text_input("Enter patient blood type: ").encode())
        self.gender = cipher.encrypt(st.text_input("Enter patient gender: ").encode())
        self.age = int(st.text_input("Enter patient age: "))
        self.dob = cipher.encrypt(st.text_input("Enter patient's DoB: ").encode())
        self.height = int(st.text_input("Enter patient's height: "))
        self.weight = int(st.text_input("Enter patient's weight: "))
        n = st.number_input("Enter no: of allergies: ", min_value=0, step=1)
        for i in range(n):
            self.allergies.append(cipher.encrypt(st.text_input(f"Enter allergy {i+1}: ").encode()))
        n = st.number_input("Enter no: of medications: ", min_value=0, step=1)
        for i in range(n):
            self.medications.append(cipher.encrypt(st.text_input(f"Enter medication {i+1}: ").encode()))
        n = st.number_input("Enter no: of medical conditions: ", min_value=0, step=1)
        for i in range(n):
            self.conditions.append(cipher.encrypt(st.text_input(f"Enter medical condition {i+1}: ").encode()))
        self.pTestRep = cipher.encrypt(st.text_input("Enter pathological test report: ").encode())
        self.phone = cipher.encrypt(st.text_input("Enter phone no.: ").encode())
        self.emerno = cipher.encrypt(st.text_input("Enter emergency no.: ").encode())
        n = st.number_input("Enter no: of remarks: ", min_value=0, step=1)
        for i in range(n):
            self.remarks.append(cipher.encrypt(st.text_input(f"Enter remarks {i+1}: ").encode()))
        self.time = cipher.encrypt(str(time.asctime(time.localtime(time.time()))).encode())

        # Insert the record into the database
        c.execute('''
            INSERT INTO patients (pid, name, btype, gender, age, dob, height, weight, allergies, medications, conditions, pTestRep, phone, emerno, remarks, time)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (self.pid, self.name, self.btype, self.gender, self.age, self.dob, self.height, self.weight, 
              ','.join(map(lambda x: x.decode(), self.allergies)), ','.join(map(lambda x: x.decode(), self.medications)), 
              ','.join(map(lambda x: x.decode(), self.conditions)), self.pTestRep.decode(), 
              self.phone.decode(), self.emerno.decode(), ','.join(map(lambda x: x.decode(), self.remarks)), 
              self.time.decode()))
        conn.commit()

    def printRec(self):
        st.write("Patient ID: ", cipher.decrypt(self.pid).decode())
        st.write("Patient name: ", cipher.decrypt(self.name).decode())
        st.write("Patient blood type: ", cipher.decrypt(self.btype).decode())
        st.write("Patient gender: ", cipher.decrypt(self.gender).decode())
        st.write("Patient age: ", self.age)
        st.write("Patient's DoB: ", cipher.decrypt(self.dob).decode())
        st.write("Patient height: ", self.height)
        st.write("Patient weight: ", self.weight)
        st.write("Patient allergies:")
        for i in self.allergies:
            st.write("\t-", cipher.decrypt(i).decode())
        st.write("Patient medications:")
        for i in self.medications:
            st.write("\t-", cipher.decrypt(i).decode())
        st.write("Patient medical conditions:")
        for i in self.conditions:
            st.write("\t-", cipher.decrypt(i).decode())
        st.write("Pathological test report: ", cipher.decrypt(self.pTestRep).decode())
        st.write("Patient phone no.: ", cipher.decrypt(self.phone).decode())
        st.write("Patient emergency no.: ", cipher.decrypt(self.emerno).decode())
        st.write("Remarks:")
        for i in self.remarks:
            st.write("\t-", cipher.decrypt(i).decode())
        st.write("Patient since : ", cipher.decrypt(self.time).decode())

# Doctor management class
class doc:
    def __init__(self):
        self.did = ""
        self.hash = ""

    def insrec(self):
        self.did = st.text_input("Enter doctor ID: ")
        P1 = st.text_input("Enter new password: ", type='password')
        self.hash = (hashlib.sha256(P1.encode())).hexdigest()

        # Check if the doctor ID already exists
        c.execute('SELECT * FROM doctors WHERE did=%s', (self.did,))
        existing_record = c.fetchone()
        if existing_record:
            st.error("Doctor ID already exists. Please choose a different ID.")
            return
        
        # Insert the new doctor record
        c.execute('''
            INSERT INTO doctors (did, hash)
            VALUES (%s, %s)
        ''', (self.did, self.hash))
        conn.commit()

# Patient management function
def pat(T):
    choice = st.selectbox("Select an option", ["Exit", "Add patient record", "Display patient record"])
    if choice == "Add patient record":
        p1 = medRecord()
        p1.insRecord()
    elif choice == "Display patient record":
        pid = st.text_input("Enter patient ID: ")
        if pid:
            c.execute('SELECT * FROM patients WHERE pid=%s', (cipher.encrypt(pid.encode()),))
            record = c.fetchone()
            if record:
                p1 = medRecord()
                p1.pid = record[0]
                p1.name = record[1]
                p1.btype = record[2]
                p1.gender = record[3]
                p1.age = record[4]
                p1.dob = record[5]
                p1.height = record[6]
                p1.weight = record[7]
                p1.allergies = record[8].split(',')
                p1.medications = record[9].split(',')
                p1.conditions = record[10].split(',')
                p1.pTestRep = record[11]
                p1.phone = record[12]
                p1.emerno = record[13]
                p1.remarks = record[14].split(',')
                p1.time = record[15]
                p1.printRec()
            else:
                st.write("Patient doesn't exist")
            c.execute('''
                INSERT INTO logbook (doctor_id, timestamp, patient_id)
                VALUES (%s, %s, %s)
            ''', (T, str(time.asctime(time.localtime(time.time()))), pid))
            conn.commit()

# Dean's hash for verification
DH = "0be64ae89ddd24e225434de95d501711339baeee18f009ba9b4369af27d30d60"

# Main control flow
def main():
    st.title("Hospital Management System")
    c0 = st.selectbox("Select an option", ["Exit", "Dean login", "Doctor login", "Patient login"])
    
    if c0 == "Dean login":
        P = st.text_input("Enter password: ", type='password')
        deanh = (hashlib.sha256(P.encode())).hexdigest()
        if deanh == DH:
            st.success("Verified")
            c1 = st.selectbox("Select an option", ["Exit", "Add new doctor credentials", "Access patient record", "Access log book"])
            if c1 == "Access patient record":
                pat("Dean")
            elif c1 == "Access log book":
                c.execute('SELECT * FROM logbook')
                for record in c.fetchall():
                    st.write(record)
            elif c1 == "Add new doctor credentials":
                d1 = doc()
                d1.insrec()
            else:
                st.write("Access denied")
    elif c0 == "Doctor login":
        did = st.text_input("Enter doctor ID: ")
        dip = st.text_input("Enter password: ", type='password')
        dih = (hashlib.sha256(dip.encode())).hexdigest()
        c.execute('SELECT * FROM doctors WHERE did=%s AND hash=%s', (did, dih))
        record = c.fetchone()
        if record:
            st.success("Verified")
            pat(did)
        else:
            st.error("Access denied or Doctor does not exist")
    elif c0 == "Patient login":
        pid = st.text_input("Enter patient ID: ")
        pdob = st.text_input("Enter date of birth: ")
        if pid and pdob:
            c.execute('SELECT * FROM patients WHERE pid=%s AND dob=%s', 
                      (cipher.encrypt(pid.encode()), cipher.encrypt(pdob.encode())))
            record = c.fetchone()
            if record:
                p1 = medRecord()
                p1.pid = record[0]
                p1.name = record[1]
                p1.btype = record[2]
                p1.gender = record[3]
                p1.age = record[4]
                p1.dob = record[5]
                p1.height = record[6]
                p1.weight = record[7]
                p1.allergies = record[8].split(',')
                p1.medications = record[9].split(',')
                p1.conditions = record[10].split(',')
                p1.pTestRep = record[11]
                p1.phone = record[12]
                p1.emerno = record[13]
                p1.remarks = record[14].split(',')
                p1.time = record[15]
                p1.printRec()
            else:
                st.error("Access denied or Patient doesn't exist")

if __name__ == "__main__":
    main()
