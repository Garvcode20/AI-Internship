import json
import csv
import os
from datetime import datetime

"""
Smart Attendance System
Mini Project for "Practical Use of AI Tools in Programming"

AI Tools Used in Development:
1. Architecture: Asked Gemini to suggest a basic CLI menu structure and data storage format (JSON).
2. Coding: Generated base CRUD operations using ChatGPT.
3. Debugging: Used Antigravity to fix a bug where dates weren't formatting correctly for CSV export.
4. Documentation: Auto-generated README and docstrings.
5. Manual Improvements: Added robust error handling and the analytics engine.
"""

DB_FILE = 'attendance_db.json'

class AttendanceSystem:
    def __init__(self):
        self.db = self.load_db()

    def load_db(self):
        """Loads the student database from a JSON file."""
        if not os.path.exists(DB_FILE):
            return {"students": {}}
        try:
            with open(DB_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Database file corrupted. Initializing new database.")
            return {"students": {}}

    def save_db(self):
        """Saves the database to a JSON file."""
        with open(DB_FILE, 'w') as f:
            json.dump(self.db, f, indent=4)

    def add_student(self):
        """Registers a new student."""
        roll_no = input("Enter Roll Number: ").strip()
        if roll_no in self.db["students"]:
            print("Student already exists.")
            return

        name = input("Enter Student Name: ").strip()
        # Initialize student with empty attendance record
        self.db["students"][roll_no] = {
            "name": name,
            "attendance": {} # Format: "YYYY-MM-DD": "Present/Absent"
        }
        self.save_db()
        print(f"Student '{name}' added successfully.")

    def mark_attendance(self):
        """Marks attendance for a specific date."""
        date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if not date_str:
            date_str = datetime.now().strftime("%Y-%m-%d")
            
        print(f"\nMarking attendance for {date_str} (P=Present, A=Absent)")
        for roll_no, data in self.db["students"].items():
            while True:
                status = input(f"{roll_no} - {data['name']}: ").strip().upper()
                if status in ['P', 'A']:
                    val = "Present" if status == 'P' else "Absent"
                    self.db["students"][roll_no]["attendance"][date_str] = val
                    break
                print("Invalid input. Please enter 'P' or 'A'.")
                
        self.save_db()
        print("Attendance recorded successfully.")

    def show_analytics(self):
        """Displays attendance statistics for each student."""
        if not self.db["students"]:
            print("No students in database.")
            return
            
        print("\n--- Attendance Analytics ---")
        for roll_no, data in self.db["students"].items():
            records = data["attendance"].values()
            total_days = len(records)
            if total_days == 0:
                print(f"{roll_no} - {data['name']}: No records.")
                continue
                
            present = sum(1 for r in records if r == "Present")
            percentage = (present / total_days) * 100
            print(f"{roll_no} - {data['name']}: {present}/{total_days} days present ({percentage:.1f}%)")

    def export_csv(self):
        """Exports the attendance records to a CSV file."""
        if not self.db["students"]:
            print("No data to export.")
            return
            
        filename = f"attendance_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # Collect all unique dates across all students to form the columns
        all_dates = set()
        for data in self.db["students"].values():
            all_dates.update(data["attendance"].keys())
        dates_sorted = sorted(list(all_dates))
        
        headers = ["Roll Number", "Name"] + dates_sorted + ["Present %"]
        
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            
            for roll_no, data in self.db["students"].items():
                row = [roll_no, data['name']]
                
                # Fill in attendance for each date
                present_count = 0
                for d in dates_sorted:
                    status = data["attendance"].get(d, "N/A")
                    row.append(status)
                    if status == "Present":
                        present_count += 1
                        
                # Calculate percentage
                if len(dates_sorted) > 0:
                    pct = f"{(present_count / len(dates_sorted) * 100):.1f}%"
                else:
                    pct = "0%"
                row.append(pct)
                
                writer.writerow(row)
                
        print(f"Data successfully exported to {filename}")

    def menu(self):
        """Main application loop."""
        while True:
            print("\n=== Smart Attendance System ===")
            print("1. Add Student")
            print("2. Mark Attendance")
            print("3. View Analytics")
            print("4. Export to CSV")
            print("5. Exit")
            
            choice = input("Select an option (1-5): ").strip()
            
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.mark_attendance()
            elif choice == '3':
                self.show_analytics()
            elif choice == '4':
                self.export_csv()
            elif choice == '5':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    app = AttendanceSystem()
    app.menu()
