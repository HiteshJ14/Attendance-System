import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"",
    'storageBucket':""
})

ref = db.reference('Students')

data = {
    "07411502821":
        {
            "Name": "Hitesh Joshi",
            "Branch": "ECE2",
            "starting_year": 2021,
            "total_attendance": 30,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-20 00:54:34"
        },
    "09211502821":
        {
            "Name": "Abhishek Paul",
            "Branch": "ECE2",
            "starting_year": 2021,
            "total_attendance": 21,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-27 00:54:34"
        },
    "11111502821":
        {
            "Name": "Vinyas Sahai",
            "Branch": "ECE2",
            "starting_year": 2021,
            "total_attendance": 20,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2023-11-11 00:54:34"
        },
    "07711502821":
        {
            "Name": "Anshika Panwar",
            "Branch": "ECE2",
            "starting_year": 2021,
            "total_attendance": 32,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-11-28 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
