import logging
from datetime import datetime
import time

# Set up logging to a file
logging.basicConfig(filename='job_execution.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

# Example of a job function
def greet():
    """
    Example function to be used as a job.
    Prints a greeting message and logs execution time.
    """
    try:
        start_time = time.time()  # Record start time
        
        # Simulate a task (e.g., printing a message)
        print(f"Hello, Manasi! It's {datetime.now()}")
        
        end_time = time.time()  # Record end time
        execution_duration = end_time - start_time
        
        print(f"[INFO] Job executed in {execution_duration:.2f} seconds.")
        
        # Log the execution time to file
        log_execution(execution_duration)
        
    except Exception as e:
        # Handle any errors that occur during job execution
        print(f"[ERROR] Job execution failed: {e}")
        logging.error(f"Job execution failed: {e}")

def log_execution(execution_duration):
    """
    Log the job execution details such as execution time.
    
    :param execution_duration: Time taken for the job to execute
    """
    # Log the execution duration to a file
    logging.info(f"Job executed with duration: {execution_duration:.2f} seconds")
