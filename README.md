## Instantly API Reporting using Google Sheets

This project provides a streamlined solution for fetching analytics data from the Instantly API and seamlessly integrating it into Google Sheets for reporting and analysis purposes.

### Features:

- **Automated Data Retrieval**: Schedule data retrieval from the Instantly API using Python scripts.
- **Data Transformation**: Convert the retrieved data into a format suitable for Google Sheets.
- **Google Sheets Integration**: Append the data to a specified Google Sheets document for easy visualization and analysis.
- **Customizable**: Easily customize the script to fit your specific Instantly campaign IDs and date ranges.
- **Secure**: Utilizes secure authentication methods for accessing the Instantly API and Google Sheets.

### Getting Started:

1. Clone this repository to your local machine.
2. Set up your Instantly API key and configure the campaign IDs and other variables `main.py`.
3. Configure Google Sheets access by providing the necessary credentials in `append_campaign_data.py`.
4. Replace 'example.json' with your google service account Json key
5. Run the `main.py` script to fetch data from the Instantly API and append it to your Google Sheets document.


### Usage:

1. Run `python main.py` to fetch data and append it to your Google Sheets document.
2. Schedule the script to run at desired intervals using cron jobs or task schedulers.

### Contributions:

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests.

### License:

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
