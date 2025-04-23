import time
import threading
from datetime import datetime
from scheduler.job import Job  # Correct import for Job class

class Scheduler:
    def __init__(self):
        """
        Initializes the Scheduler with an empty list of jobs.
        """
        self.jobs = []  # List of scheduled jobs
        self.running = False  # Flag to check if the scheduler is running

    def add_job(self, job):
        """
        Add a job to the scheduler and sort by priority.
        
        :param job: Job object to schedule
        """
        self.jobs.append(job)
        # Sort jobs by priority: lower priority value indicates higher priority
        self.jobs = sorted(self.jobs, key=lambda x: x.priority)
        print(f"[INFO] Job added: {job.name} with priority {job.priority}")

    def start(self):
        """
        Starts the scheduler and runs the jobs in the correct order.
        """
        self.running = True
        print("[INFO] Scheduler started. Press Ctrl+C to stop.")
        try:
            while self.running:
                current_time = datetime.now()  # Get current time
                for job in self.jobs:
                    if job.is_due(current_time):  # Check if the job is due for execution
                        threading.Thread(target=self._run_job, args=(job,)).start()  # Run each job in a separate thread
                time.sleep(1)  # Check jobs every 1 second
        except KeyboardInterrupt:
            print("\n[INFO] Scheduler stopped by user.")

    def stop(self):
        """
        Stop the scheduler from running.
        """
        self.running = False
        print("[INFO] Scheduler stopped.")

    def _run_job(self, job):
        """
        Internal method to run the job function and handle errors.
        """
        try:
            job.execute()  # Execute the job
        except Exception as e:
            # In case of an error, log the issue
            print(f"[ERROR] Job {job.name} failed: {str(e)}")
