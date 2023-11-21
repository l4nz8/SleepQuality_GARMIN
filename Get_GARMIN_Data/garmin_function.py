import pandas as pd
import datetime, os
from tqdm import tqdm 

def get_steps_data(api, start_date):
    try:
        steps_data = api.get_steps_data(start_date)
    except Exception as e:
        return f"An error has occurred: {e}"
    return steps_data

def get_heart_rates(api, start_date):
    try:
        steps_data = api.get_heart_rates(start_date)
    except Exception as e:
        return f"An error has occurred: {e}"
    return steps_data

def get_sleep_data(api, start_date):
    try:
        steps_data = api.get_sleep_data(start_date)
    except Exception as e:
        return f"An error has occurred: {e}"
    return steps_data
        
def log_data(api, start_date, end_date, func):
    logged_data = []
    # Calculate the number of days for the progress bar
    total_days = (end_date - start_date).days + 1
    
    # Iterate from start to end date through the data with tqdm progressbar
    with tqdm(total=total_days, desc=func.__name__) as pbar:
        for date in (start_date + datetime.timedelta(n) for n in range(
            (end_date - start_date).days + 1)):
            
            device_activity = func(api, date)
            # Add the data to a total list
            logged_data.extend(device_activity)
            pbar.update(1)

    data = pd.DataFrame(logged_data)
    return data

def save_csv(api, start_date, end_date, 
             func=[get_steps_data, get_heart_rates, get_sleep_data], 
             index=False):
    directory_path = "data/"
    # Check for path
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Create csv for every function in list
    for i, f in enumerate(func, start=1):
        print(f"{i}/{len(func)} - Retrieving {f.__name__[4:]}")
        file_path = os.path.join(directory_path, f.__name__[4:]+".csv")
        log_data(api, start_date, end_date, f).to_csv(file_path, index=index)
