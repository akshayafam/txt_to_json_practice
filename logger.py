# New Program logger.py for python practice with linux and DevOps
import os
from datetime import datetime

def main():
    folder_name = "data_logs"
    file_name = f"{folder_name}/timestamp.txt"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"[SUCCESS] Created Directory: {folder_name}")
    else:
        print(f"[INFO] Directory '{folder_name}' already exists. Skipping creation ")
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a" ) as f:
        f.write(f"Log Entry: {now}\n")

    file_size = os.path.getsize(file_name)
    print(f"[SUCCESS] Logged timestamp to {file_name}")
    print(f"[STATUS] Current log file size: {file_size} bytes")

if __name__ == "__main__":
    main()

