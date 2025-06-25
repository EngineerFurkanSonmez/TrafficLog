# Google Maps Driving Duration Logger

This Python script retrieves the driving duration between two specified locations using the Google Maps Directions API and logs this information to an Excel file.

## Features

-   Fetches real-time driving duration (considering current traffic if "now" is used for departure time).
-   Logs data including timestamp, origin, destination, and duration (in minutes) to an Excel file (`gmap_log.xlsx`).
-   Automatically creates the Excel file with a header row if it doesn't exist.
-   Appends new data to the existing file on subsequent runs.

## Prerequisites

1.  **Python 3**: Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).
2.  **pip**: Python's package installer. It usually comes with Python 3.
3.  **Google Maps API Key**: You need a valid Google Maps Directions API key.
    *   Go to the [Google Cloud Console](https://console.cloud.google.com/).
    *   Create a new project (or select an existing one).
    *   Enable the "Directions API" for your project.
    *   Create an API key under "Credentials".
    *   **Important**: Secure your API key. Restrict its usage to the Directions API and specific IP addresses if possible.

## Installation

1.  Clone this repository or download the `gmap_duration_logger.py` script.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you cloned or downloaded the files.
4.  Install the required Python packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```
    This will install `googlemaps`, `openpyxl`, and their necessary dependencies.

## How to Use

1.  **Add your API Key**:
    Open the `gmap_duration_logger.py` script in a text editor.
    Locate the following line:
    ```python
    API_KEY = "YOUR_API_KEY_HERE"
    ```
    Replace `"YOUR_API_KEY_HERE"` with your actual Google Maps API key.

2.  **Customize Origin and Destination (Optional)**:
    In the `if __name__ == "__main__":` block at the bottom of the script, you can change the `example_origin` and `example_destination` variables:
    ```python
    # --- Example Usage ---
    # You can change these addresses
    example_origin = "Times Square, New York, NY"
    example_destination = "Empire State Building, New York, NY"

    # Or use coordinates:
    # example_origin = "40.7580, -73.9855"
    # example_destination = "40.7484, -73.9857"
    ```

3.  **Run the Script**:
    Execute the script from your terminal:
    ```bash
    python gmap_duration_logger.py
    ```

## Output

Each time the script runs successfully:
-   It will print the retrieved driving duration to the console.
-   It will append a new row to the `gmap_log.xlsx` file in the same directory as the script.

The `gmap_log.xlsx` file will have the following columns:
-   **Timestamp**: The date and time when the script was run (e.g., `2023-10-27 14:30:00`).
-   **Origin**: The starting address or coordinates.
-   **Destination**: The ending address or coordinates.
-   **Duration (min)**: The calculated driving duration in minutes. If an error occurred (e.g., API key invalid, no route found), this might be empty or indicate an error.

## Troubleshooting

-   **`Error: Please replace 'YOUR_API_KEY_HERE'...`**: You haven't replaced the placeholder API key in the script.
-   **`Google Maps API Error: ...`**: This could be due to an invalid API key, the Directions API not being enabled for your project, or billing issues with your Google Cloud account. Check the specific error message and your Google Cloud Console.
-   **`No route found between 'origin' and 'destination'.`**: The API could not find a driving route between the specified points. Check for typos or try different locations.
-   **`PermissionError: [Errno 13] Permission denied: 'gmap_log.xlsx'`**: The script doesn't have permission to write the Excel file. Ensure the file is not open in another program and that you have write permissions in the script's directory.

This project provides a basic framework. You can extend it further, for example, by reading origin/destination pairs from a CSV file, scheduling the script to run at regular intervals, or adding more robust error logging.
