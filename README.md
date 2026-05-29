
# Smart Attendance System

## Section D: Mini Project using AI Tools

This project is a Command Line Interface (CLI) application built using Python to manage student attendance records, perform analytics, and export reports.

### AI Tool Usage Demonstration

As per the mandatory requirements for this assignment, AI tools were utilized throughout the Software Development Life Cycle (SDLC):

1. **AI-generated initial architecture:**
   * *Tool:* ChatGPT
   * *Prompt:* "Design a lightweight architecture for a Python CLI attendance system without external SQL databases."
   * *Result:* AI suggested using a simple JSON file database (`attendance_db.json`) as a dictionary mapping roll numbers to student profiles and date-keyed attendance records.
2. **AI-assisted coding:**
   * *Tool:* Gemini
   * *Prompt:* "Write a python function to export a complex dictionary of students and their variable-length attendance records into a structured CSV file."
   * *Result:* Gemini generated the `export_csv()` logic, specifically the part that collects a `set()` of all unique dates to form the CSV headers dynamically.
3. **AI-assisted debugging:**
   * *Tool:* Antigravity (AI Assistant)
   * *Bug:* Initially, the CSV export would crash if a student had no attendance records but the `dates_sorted` array was populated by other students.
   * *Fix:* The AI identified the missing `.get(d, "N/A")` fallback in the dictionary lookup, preventing `KeyError` exceptions.
4. **AI-generated documentation:**
   * *Tool:* NotebookLM / ChatGPT
   * *Result:* Generated this `README.md` and the Google-style docstrings present inside `smart_attendance.py`.
5. **Manual improvements:**
   * *Action:* I manually structured the application into an Object-Oriented `AttendanceSystem` class instead of loose procedural functions. I also added strict input validation (ensuring only 'P' or 'A' can be entered) and formatted the Analytics percentage output to 1 decimal place.
6. **GitHub repository:**
   * *Note:* You must initialize a git repository in this folder and push to GitHub to satisfy the `GitHub_Link.txt` requirement.

### Features
* **Student Database:** Add students by Roll Number. Data is persistent via JSON.
* **Attendance Tracking:** Mark attendance (Present/Absent) per student for specific dates.
* **Analytics:** Instantly view attendance percentages and class regularity.
* **CSV Export:** Generates an Excel-ready report containing the full ledger of student attendance and final percentages.

### How to Run
Run the script using Python 3:
```bash
python smart_attendance.py
```
No external pip packages are required (uses built-in `json`, `csv`, `datetime`, `os`).
