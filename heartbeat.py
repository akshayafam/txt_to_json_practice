import time
import os

def main():
    print("Self-healing monitor active... (Press Ctrl+C to stop)")
    try:
        while True:
            # Get the current time
            now = time.strftime("%Y-%m-%d %H:%M:%S")
            
           
            if os.path.exists("data_logs"):
                print(f"[{now}] System is healthy.")
            else:

                # 1 - Alert the terminal about missing logs folder
                print(f"[{now}] ALERT: Folder missing! Repairing...")
                # 2 - Perform the repair:
                os.makedirs("data_logs")
                print(f"[{now}] REPAIR: Folder recreated successfully.")
                # 3 - Log the security incident:
                with open("security.log", "a") as sec_log:
                    sec_log.write(f"REPAIR_EVENT at {now}: Created missing directory 'data_logs' \n")
            
            # Wait for 5 seconds before checking again
            time.sleep(5)
            
    except KeyboardInterrupt:
        print("\nStopping Heartbeat monitor. Goodbye!")

if __name__ == "__main__":
    main()