import time
import logging
from datetime import datetime, timedelta  # Added timedelta import

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

class Job:
    def __init__(self, name, func, interval, repeat, job_id, priority=5):
        """
        Initializes the Job instance.
        
        :param name: Name of the job
        :param func: Function to run for the job
        :param interval: Interval time (seconds) between job executions
        :param repeat: If True, the job will repeat
        :param job_id: Unique identifier for the job
        :param priority: Job's priority (lower values indicate higher priority)
        """
        self.name = name
        self.func = func
        self.interval = interval
        self.repeat = repeat
        self.job_id = job_id
        self.priority = priority  # Add priority to control execution order
        self.execution_count = 0  # Track number of executions
        self.last_execution_time = None
        self.execution_duration = 0.0  # Track how long the job takes to execute

    def execute(self):
        """
        Executes the job's function and tracks execution details.
        """
        start_time = time.time()  # Record start time for execution duration
        try:
            self.func()  # Run the actual function
            self.execution_count += 1
            self.last_execution_time = datetime.now()  # Update last execution time
        except Exception as e:
            logging.error(f"Error executing job {self.name}: {str(e)}")  # Log the error
        finally:
            self.execution_duration = time.time() - start_time  # Calculate execution time
            logging.info(f"Job '{self.name}' executed in {self.execution_duration:.2f} seconds.")
            
    def is_due(self, current_time):
        """
        Check if the job is due for execution based on the interval.
        
        :param current_time: The current time to check against the job's execution schedule.
        :return: True if the job is due to run, False otherwise.
        """
        if self.last_execution_time is None:
            return True  # First execution
        next_execution_time = self.last_execution_time + timedelta(seconds=self.interval)
        return current_time >= next_execution_time
