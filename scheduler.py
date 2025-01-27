import time
import schedule
import subprocess

def job():
    subprocess.run(["/bin/bash", "/workspaces/test/automate_report.sh"])

# Schedule the job every day at 7 AM Armenia time (3 AM UTC)
schedule.every().day.at("3:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait for 1 minute before checking again
