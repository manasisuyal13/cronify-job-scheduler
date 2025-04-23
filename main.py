import time
import threading
from datetime import datetime
from scheduler.job import Job  # Correct import for Job class
from jobs.example_job import greet

# Initialize the scheduler
scheduler = Scheduler()

# Global variable to keep track of the scheduler thread
scheduler_thread = None
scheduler_running = False

# Function to add a new job
def add_job(job_name, interval):
    try:
        # Ensure the interval is a positive integer
        if interval <= 0:
            raise ValueError("Interval must be a positive integer.")

        # Create a new Job object
        job = Job(
            name=job_name,
            func=greet,
            interval=interval,
            repeat=True,
            job_id=len(scheduler.jobs) + 1
        )

        # Add the job to the scheduler
        scheduler.add_job(job)
        print(f"Job '{job_name}' added successfully.")
        return True
    except ValueError as ve:
        print(f"Error: {ve}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return False

# Function to start the scheduler
def start_scheduler():
    global scheduler_thread, scheduler_running

    if scheduler_running:
        print("The scheduler is already running.")
        return

    print("The scheduler is now running.")
    scheduler_thread = threading.Thread(target=scheduler.start, daemon=True)  # Start the scheduler in a separate thread
    scheduler_thread.start()
    scheduler_running = True

# Function to stop the scheduler
def stop_scheduler():
    global scheduler_running

    if not scheduler_running:
        print("The scheduler is not running.")
        return

    # Stop the scheduler
    scheduler.stop()  # Call the stop method in the Scheduler
    scheduler_running = False
    print("The scheduler has been stopped.")

# Function to reset (clear) all jobs
def reset_jobs():
    scheduler.jobs.clear()  # Clear the list of jobs
    print("All jobs have been reset.")
