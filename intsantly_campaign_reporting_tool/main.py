import requests
import json
import append_campaign_data
from datetime import datetime, timedelta
import schedule
import time


def execute_code():
    # Define the API endpoint
    url = "https://api.instantly.ai/api/v1/analytics/campaign/count"
    Api_key = "example-api-key"
    Campaign_ids = ["example-campaign-id-1", "example-campaign-id-2"]
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    formatted_yesterday = yesterday.strftime("%Y-%m-%d")
    Start_date = formatted_yesterday
    End_date = formatted_yesterday

    # Manually map Instantly campaign IDs to names
    campaign_names = {
        "example-campaign-id-1": "Example Campaign Name 1",
        "example-campaign-id-2": "Example Campaign Name 2"
    }

    merged_list = []

    for Campaign_id in Campaign_ids:
        # Define the API key and other parameters
        params = {
            "api_key": Api_key,  # replace with your API Key
            "campaign_id": Campaign_id,  # replace with your campaign ID
            "start_date": Start_date,  # replace with the start date
            "end_date": End_date  # replace with the end date
        }

        # Make the GET request
        response = requests.get(url, params=params)

        # Parse the JSON response
        data = json.loads(response.text)
        print(data) # Print the response for debugging purposes
        
        # Assuming the response is a list of dictionaries, append it to merged_list
        for item in data:
            item['name'] = campaign_names[Campaign_id]  # Add the campaign name to each item
            merged_list.append(item)    # Append the merged data to append_campaign_data




    append_campaign_data.append_campaign_data(merged_list, Start_date, End_date)




if __name__ == '__main__':
    # Schedule the execute_code function to run every weekday at 06:30
    schedule.every().monday.at("06:30").do(execute_code)
    schedule.every().tuesday.at("06:30").do(execute_code)
    schedule.every().wednesday.at("06:30").do(execute_code)
    schedule.every().thursday.at("06:30").do(execute_code)
    schedule.every().friday.at("06:30").do(execute_code)  
    # Keep the script running continuously to execute scheduled tasks
    while True:
        schedule.run_pending()
        time.sleep(1)
