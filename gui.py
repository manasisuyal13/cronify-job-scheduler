import tkinter as tk
import threading
from scheduler.scheduler import Scheduler
from scheduler.job import Job
from jobs.example_job import greet  # Make sure this function is correctly defined

# Initialize the scheduler
scheduler = Scheduler()

# Global variable to keep track of the scheduler thread
scheduler_thread = None
scheduler_running = False

# Function to add a new job
def add_job():
    try:
        job_name = job_name_entry.get()
        interval = int(interval_entry.get())

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
        update_job_list()

        # Display auto-closing notification
        show_auto_closing_popup(f"Job '{job_name}' added successfully.")
    except ValueError:
        show_auto_closing_popup("Please enter valid values for all fields.")

# Function to update the displayed list of jobs
def update_job_list():
    jobs_listbox.delete(0, tk.END)  # Clear existing list
    for job in scheduler.jobs:
        jobs_listbox.insert(tk.END, f"{job.name} - Every {job.interval} seconds")

# Function to show an auto-closing notification
def show_auto_closing_popup(message):
    popup_label = tk.Label(root, text=message, fg="green", font=("Arial", 12, "bold"), bg="#dff0d8", relief="solid", padx=10, pady=5)
    popup_label.place(x=200, y=300)  # Position the label on the window

    # After 3 seconds, destroy the label (auto-close)
    root.after(3000, popup_label.destroy)

# Function to start the scheduler
def start_scheduler():
    global scheduler_thread, scheduler_running

    if scheduler_running:
        show_auto_closing_popup("The scheduler is already running.")
        return

    show_auto_closing_popup("The scheduler is now running.")
    scheduler_thread = threading.Thread(target=scheduler.start, daemon=True)  # Start the scheduler in a separate thread
    scheduler_thread.start()
    scheduler_running = True

    # Update button states
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# Function to stop the scheduler
def stop_scheduler():
    global scheduler_running

    if not scheduler_running:
        show_auto_closing_popup("The scheduler is not running.")
        return

    # Stop the scheduler
    scheduler.stop()  # Call the stop method in the Scheduler
    scheduler_running = False
    show_auto_closing_popup("The scheduler has been stopped.")

    # Update button states
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

# Function to reset (clear) all jobs
def reset_jobs():
    scheduler.jobs.clear()  # Clear the list of jobs
    update_job_list()  # Update the Listbox to reflect the changes
    show_auto_closing_popup("All jobs have been reset.")

# Set up the main window
root = tk.Tk()
root.title("Job Scheduler")
root.geometry("500x400")  # Set the window size
root.config(bg="#f4f4f4")  # Set background color for the window

# Title label
title_label = tk.Label(root, text="Job Scheduler", font=("Arial", 18, "bold"), fg="#4a90e2", bg="#f4f4f4")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Labels and Entry fields
job_name_label = tk.Label(root, text="Job Name:", font=("Arial", 12), bg="#f4f4f4")
job_name_label.grid(row=1, column=0, padx=10, pady=5)
job_name_entry = tk.Entry(root, font=("Arial", 12), width=25)
job_name_entry.grid(row=1, column=1, padx=10, pady=5)

interval_label = tk.Label(root, text="Interval (seconds):", font=("Arial", 12), bg="#f4f4f4")
interval_label.grid(row=2, column=0, padx=10, pady=5)
interval_entry = tk.Entry(root, font=("Arial", 12), width=25)
interval_entry.grid(row=2, column=1, padx=10, pady=5)

# Add Job button
add_button = tk.Button(root, text="Add Job", command=add_job, font=("Arial", 12), bg="#4caf50", fg="white", relief="raised", bd=2, width=15)
add_button.grid(row=3, column=0, columnspan=2, pady=20)

# Listbox to show the jobs
jobs_listbox = tk.Listbox(root, font=("Arial", 12), width=45, height=8, bg="#f1f1f1", bd=2, relief="sunken")
jobs_listbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start Scheduler button
start_button = tk.Button(root, text="Start Scheduler", command=start_scheduler, font=("Arial", 12), bg="#008CBA", fg="white", relief="raised", bd=2, width=15)
start_button.grid(row=5, column=0, pady=10)

# Stop Scheduler button
stop_button = tk.Button(root, text="Stop Scheduler", command=stop_scheduler, font=("Arial", 12), bg="#f44336", fg="white", relief="raised", bd=2, width=15, state=tk.DISABLED)
stop_button.grid(row=5, column=1, pady=10)

# Reset Jobs button
reset_button = tk.Button(root, text="Reset Jobs", command=reset_jobs, font=("Arial", 12), bg="#ff9800", fg="white", relief="raised", bd=2, width=15)
reset_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI loop
root.mainloop()
