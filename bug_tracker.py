"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

while True:
    choice = input("Enter 'log' to record a bug, or 'quit' to stop: ")

    if choice.lower() == "quit":
        print("Bug log updated!")
        break

    if choice.lower() == "log":
        file_name = input("File name: ")
        description = input("Description of error: ")
        priority = input("Priority (High, Medium, Low): ")

        current_time = datetime.datetime.now()
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

        bug_log = {
            timestamp: [file_name, description, priority]
        }

        with open("bug_log.txt", "a") as file:
            file.write(f"""[{timestamp}]
File: {bug_log[timestamp][0]}
Status: {bug_log[timestamp][1]}
Priority: {bug_log[timestamp][2]}
--------------------------------------------------

""")