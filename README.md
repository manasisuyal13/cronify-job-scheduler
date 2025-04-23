# Cronify Job Scheduler 🚀

Welcome to **Cronify Job Scheduler**! This is a flexible and easy-to-use Python-based job scheduler that allows you to schedule and manage jobs (tasks) with different intervals and priorities. It runs jobs in parallel threads, supports job retries, error logging, and provides a graphical user interface (GUI) to manage your scheduled jobs.

--- 

## Features ✨

- **Job Scheduling**: Schedule jobs at specific intervals.
- **Job Priorities**: Assign priorities to jobs to control execution order.
- **Job Execution Logs**: Log job execution details, including execution duration.
- **Graphical User Interface (GUI)**: A user-friendly interface to manage jobs easily.
- **Error Handling**: Catch and log errors for each job execution.
- **Reset Jobs**: Clear all scheduled jobs with a single click.
- **Auto-Closing Notifications**: Inform users about job statuses, such as when a job is added or the scheduler is started/stopped.

---

## Installation 🛠️

Follow these steps to install and use Cronify Job Scheduler on your machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/manasisuyal13/cronify-job-scheduler.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd cronify-job-scheduler
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage Guide 🏃‍♀️

### 1. **Running the Scheduler**

To start the job scheduler:

```bash
python main.py
```

This will launch the graphical user interface (GUI) for the job scheduler, where you can:

- Add jobs
- Start/stop the scheduler
- Reset all jobs

---

### 2. **Job Management**

**Add a Job**:
- Enter a job name and interval (in seconds).
- Click **"Add Job"** to schedule the job.
- Jobs will appear in the list on the left-hand side.

**Start the Scheduler**:
- Click **"Start Scheduler"** to begin executing scheduled jobs in parallel.
- The scheduler will check if jobs are due every second.

**Stop the Scheduler**:
- Click **"Stop Scheduler"** to halt job execution.

**Reset All Jobs**:
- Click **"Reset Jobs"** to remove all scheduled jobs.

---

### 3. **Job Scheduling Features**

- **Priority**: Jobs are executed based on priority (lower numbers = higher priority).
- **Repeat**: Jobs can be scheduled to repeat at fixed intervals.
- **Execution Logs**: See logs for each job's execution time, and monitor its performance.

---

## Code Structure 🗂️

Here's a brief overview of the code structure:

```
cronify-job-scheduler/
├── jobs/                   # Contains all job definitions (e.g., example jobs)
│   └── example_job.py      # A sample job (e.g., greet job)
├── scheduler/              # Core scheduler logic and job management
│   ├── __init__.py
│   ├── job.py              # Job class that defines job properties and behavior
│   └── scheduler.py        # Scheduler class that manages job execution
├── main.py                 # Main entry point for running the GUI
├── gui.py                  # GUI interface to interact with the scheduler
├── requirements.txt        # List of dependencies
└── README.md               # This file
```

---

## How It Works 💻

1. **Job Definition**:
   - Define jobs in `jobs/`.
   - A job consists of a name, function, interval (in seconds), and priority.

2. **Scheduler**:
   - The `Scheduler` class in `scheduler/scheduler.py` is responsible for running jobs based on the time interval.
   - Jobs are executed in parallel threads to avoid blocking the main thread.

3. **GUI**:
   - The GUI is built using **Tkinter** and provides a simple interface for users to add, remove, and manage jobs.

---

## Example Jobs 🧑‍💻

You can define your own jobs (functions) in the `jobs/` folder. Here's an example of a simple greeting job:

```python
# jobs/example_job.py

import time
from datetime import datetime

def greet():
    """
    This job will print a greeting message along with the current time.
    """
    print(f"Hello! The current time is {datetime.now()}")
    time.sleep(1)  # Simulate job execution time
```

You can then add it to the scheduler via the GUI by providing the job name and interval (in seconds).

---

## Screenshots 📸

Here are some screenshots to help you understand how the scheduler looks and works:

- **Main Window**: Displays job list, and buttons to add, start, and stop the scheduler.
- **Add Job Form**: Enter job details (name and interval).
- **Job List**: Shows all scheduled jobs.

---

## Contributing 🤝

We welcome contributions to make Cronify Job Scheduler even better! If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact 📧

If you have any questions or suggestions, feel free to reach out to me:

- **GitHub**: [manasisuyal13](https://github.com/manasisuyal13)
- **Email**: manasisuyal2003@gmail.com

---

Thank you for using **Cronify Job Scheduler**! 😊
