from garminconnect import (Garmin,  
                           GarminConnectConnectionError, 
                           GarminConnectAuthenticationError, 
                           GarminConnectTooManyRequestsError)
import datetime
import pandas as pd
import csv

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

if __name__ == "__main__":
    
    # Link with Garmin-Connect account
    email = input()
    password = input()
    
    api = init_garmin_api(email, password)
