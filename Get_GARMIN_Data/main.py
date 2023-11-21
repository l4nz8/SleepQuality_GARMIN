from garminconnect import (Garmin,  
                           GarminConnectConnectionError, 
                           GarminConnectAuthenticationError, 
                           GarminConnectTooManyRequestsError)
import pandas as pd
from tqdm import tqdm 
import datetime, os, csv

def init_garmin_api(email, password):
    # Connect API
    try:  
        print("Try to connect with GARMIN...")
        api = Garmin(email, password)
        api.login() 
        print("Connected")
    # Error handling
    except(GarminConnectConnectionError, 
            GarminConnectAuthenticationError, 
            GarminConnectTooManyRequestsError
            ) as err: 
        return f"ERROR: {err}"
    return api

def get_steps_data(api, start_date):
    try:
        steps_data = api.get_steps_data(start_date)
    except Exception as e:
        return f"An error has occurred: {e}"
    return steps_data
        
def log_data(api, start_date, end_date):
    # Calculate the number of days for the progress bar
    total_days = (end_date - start_date).days + 1
    logged_data = []
    # Iterate from start to end date through the data
    with tqdm(total=total_days, desc="Progress") as pbar:
        for date in (start_date + datetime.timedelta(n) for n in range((end_date - start_date).days + 1)):
        
            device_activity = get_steps_data(api, date)
            # Add the data to a total list
            logged_data.extend(device_activity)

            pbar.update(1)

    data = pd.DataFrame(logged_data)
    return data

def save_csv():
    pass

if __name__ == "__main__":
    
    # Time span
    start_date = datetime.date(2023, 10, 1)
    end_date = datetime.date.today()

    # Link with Garmin-Connect account
    email = input("Email: ")
    password = input("Password: ")
    
    api = init_garmin_api(email, password)
    data = log_data(api, start_date, end_date)
    print(data)
