# Pip install commands:
# pip install googlemaps
# pip install openpyxl

import googlemaps
import openpyxl
from datetime import datetime
import os

# ---- Configuration ----
# Enter your Google Maps API Key here:
API_KEY = "YOUR_API_KEY_HERE"
# -------------------------

DEFAULT_EXCEL_FILENAME = "gmap_log.xlsx"

def get_driving_duration(api_key, origin, destination):
    """
    Retrieves the driving duration between two locations using the Google Maps Directions API.

    Args:
        api_key (str): Your Google Maps API key.
        origin (str): The starting address or coordinates.
        destination (str): The ending address or coordinates.

    Returns:
        int: Driving duration in minutes, or None if an error occurs or no route is found.
    """
    if api_key == "YOUR_API_KEY_HERE":
        print("Error: Please replace 'YOUR_API_KEY_HERE' with your actual Google Maps API key in the script.")
        return None

    gmaps = googlemaps.Client(key=api_key)

    try:
        # Request directions
        directions_result = gmaps.directions(origin,
                                             destination,
                                             mode="driving",
                                             departure_time="now") # Using "now" for traffic estimation

        # Check if directions_result is not empty and has the expected structure
        if directions_result and isinstance(directions_result, list) and len(directions_result) > 0:
            # Get the duration in seconds from the first route
            duration_seconds = directions_result[0]['legs'][0]['duration']['value']
            duration_minutes = int(duration_seconds / 60)
            return duration_minutes
        else:
            print(f"No route found between '{origin}' and '{destination}'.")
            return None
    except googlemaps.exceptions.ApiError as e:
        print(f"Google Maps API Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def log_to_excel(filename, timestamp_val, origin_val, destination_val, duration_minutes_val):
    """
    Logs the driving duration data to an Excel file.

    Args:
        filename (str): The name of the Excel file.
        timestamp_val (datetime): The timestamp of the query.
        origin_val (str): The origin address.
        destination_val (str): The destination address.
        duration_minutes_val (int): The driving duration in minutes.
    """
    file_exists = os.path.exists(filename)

    if not file_exists:
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        # Add header row
        headers = ["Timestamp", "Weekday", "Origin", "Destination", "Duration (min)"]
        sheet.append(headers)
        print(f"Created new Excel file: '{filename}' with headers.")
    else:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active

    # Determine weekday
    weekday_str = timestamp_val.strftime("%A") # %A gives full weekday name (e.g., "Monday")

    # Append data row
    data_row = [timestamp_val.strftime("%Y-%m-%d %H:%M:%S"), weekday_str, origin_val, destination_val, duration_minutes_val]
    sheet.append(data_row)

    try:
        workbook.save(filename)
        print(f"Successfully logged data to '{filename}'.")
    except Exception as e:
        print(f"Error saving Excel file '{filename}': {e}")


if __name__ == "__main__":
    # --- Example Usage ---
    # You can change these addresses
    example_origin = "Times Square, New York, NY"
    example_destination = "Empire State Building, New York, NY"

    # For coordinates example:
    # example_origin = "40.7580, -73.9855"  # Times Square coordinates
    # example_destination = "40.7484, -73.9857" # Empire State Building coordinates

    print(f"Attempting to get driving duration from '{example_origin}' to '{example_destination}'...")

    current_time = datetime.now()
    duration = get_driving_duration(API_KEY, example_origin, example_destination)

    if duration is not None:
        log_to_excel(DEFAULT_EXCEL_FILENAME, current_time, example_origin, example_destination, duration)
        print(f"The estimated driving duration is: {duration} minutes.")
    else:
        print("Failed to retrieve driving duration. Please check your API key and addresses.")
        # Optionally, log the failure attempt as well if desired
        # log_to_excel(DEFAULT_EXCEL_FILENAME, current_time, example_origin, example_destination, "ERROR")

    print("\nScript finished.")
    print(f"Note: If you see 'YOUR_API_KEY_HERE' errors, please update the API_KEY variable in the script.")
