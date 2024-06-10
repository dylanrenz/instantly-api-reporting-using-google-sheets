from google.oauth2 import service_account
import gspread


def append_campaign_data(campaign_data, Start_date, End_date):
    # Define the scope and credentials
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'example.json'  # Path to the JSON key file

    # Authenticate using service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Authorize the client
    client = gspread.authorize(credentials)

    # Open the Google Sheet by its ID
    sheet_id = 'Google Sheet ID'
    sheet = client.open_by_key(sheet_id)

    # Select the worksheet to append data to
    worksheet = sheet.get_worksheet(0)  # Assuming the first worksheet


    decimal_start = float(Start_date.replace('-', ''))
    decimal_end = float(End_date.replace('-', ''))

    # Convert data to rows, starting from the second row
    data = []
    for campaign in campaign_data:
       data.append([campaign["name"], campaign["emails_sent"], campaign["emails_read"], decimal_start, decimal_end])


    # Append data to the worksheet
    worksheet.append_rows(data, value_input_option='USER_ENTERED', insert_data_option='INSERT_ROWS')

    print("Data appended successfully.")
  


