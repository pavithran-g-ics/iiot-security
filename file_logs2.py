import subprocess
import time

log_file = "/home/user/Logs/file_logs.txt"  # Replace with your desired file path
timestamp_file = "/home/user/Logs/last_timestamp.txt"  # File to store the last processed timestamp

# Function to get the latest logs since the last timestamp
def get_latest_logs(since_time):
    # Command to run ausearch and capture logs since the given timestamp
    command = ["ausearch", "-k", "Secret", "-ts", "recent"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

# Function to update the last processed timestamp
def update_timestamp():
    # Command to get the current timestamp in a suitable format
    command = ["date", "+%Y-%m-%d %H:%M:%S"]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

# Function to run ausearch and append only new logs to the top of a file
def append_new_audit_logs():
    # Read the last timestamp
    try:
        with open(timestamp_file, "r") as f:
            last_timestamp = f.read().strip()
    except FileNotFoundError:
        last_timestamp = "now-1d"  # Default to the last 24 hours if no timestamp file exists
    
    # Get the latest logs since the last timestamp
    new_logs = get_latest_logs(last_timestamp)
    
    # Check if there are new logs
    if new_logs:
        # Read existing content of the file
        try:
            with open(log_file, "r") as f:
                existing_logs = f.read()
        except FileNotFoundError:
            existing_logs = ""
        
        # Prepend new logs to the existing content
        new_content = new_logs + "\n\n" + existing_logs
        
        # Write the updated content back to the file
        with open(log_file, "w") as f:
            f.write(new_content)
        
        # Update the timestamp to the current time
        new_timestamp = update_timestamp()
        with open(timestamp_file, "w") as f:
            f.write(new_timestamp)
        
        # Print a message to indicate new logs have been appended
        print(f"Appended new audit logs to {log_file}")
    else:
        print("No new audit logs found.")

# Main loop to run the script every 5 seconds
if __name__ == "__main__":
    while True:
        append_new_audit_logs()
        time.sleep(5)  # Sleep for 5 seconds before running again
