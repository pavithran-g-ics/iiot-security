import subprocess
from datetime import datetime, timedelta
import time

log_file = "/home/user/Logs/file_logs.txt"  # Replace with your desired file path

# Function to run ausearch and append new logs from the previous minute to a file
def append_logs_from_previous_minute():
    while True:
        # Calculate time range for logs from the previous minute
       
     
        
        # Format time strings for ausearch command (using locale-independent format)
        
        
        # Command to run ausearch and capture output
        command = ["ausearch", "-k", "Secret_file_changed", "-i", "-ts", "12:55:00"]
        
        # Run ausearch command and capture output
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Check if there is any output
        if result.stdout:
            # Append new logs to the file
            with open(log_file, "a") as f:
                f.write(result.stdout)
                f.write("\n\n")  # Adding newline for separation of different queries or results
            
            # Print a message to indicate logs appended
            print(f"Appended audit logs from  to to {log_file}")
        else:
            print(f"No audit logs found from to .")
        
        # Sleep for 60 seconds before running again
        time.sleep(2)

# Run the function to append logs from previous minute
if __name__ == "__main__":
    append_logs_from_previous_minute()

