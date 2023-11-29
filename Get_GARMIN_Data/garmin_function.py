import pandas as pd
import datetime, os, json
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
            if func.__name__ == "get_steps_data":
                logged_data.extend(device_activity)
            else:
                logged_data.append(device_activity)
            pbar.update(1)

        return logged_data

def save_data(api, start_date, end_date, 
             func=[get_steps_data, get_heart_rates, get_sleep_data], 
             index=False):
    directory_path = "data/"
    # Check for path
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Create csv or json for every function in list
    for i, f in enumerate(func, start=1):
        file_extension = "csv" if f.__name__ == "get_steps_data" else "json"
        file_path = os.path.join(directory_path, f.__name__[4:] + f".{file_extension}")

        print(f"{i}/{len(func)} - Retrieving {f.__name__[4:]}")
        
        data = log_data(api, start_date, end_date, f)
        
        if data is not None:
            if file_extension == "csv":
                data = pd.DataFrame(data)
                data.to_csv(file_path, index=index)
            elif file_extension == "json":
                with open(file_path, "w") as json_file:
                    json.dump(data, json_file) 

if __name__ == "__main__":
    from main import init_garmin_api
    
    start_date = datetime.date(2023, 10, 1)
    end_date = datetime.date.today()

    # Enter your email address and password here to test individual methods more quickly with the api
    email = "..."
    password = "..."
    
    api = init_garmin_api(email, password)

    save_data(api, start_date, end_date, func=[get_steps_data, get_heart_rates, get_sleep_data])