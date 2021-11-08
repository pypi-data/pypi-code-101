import requests
import datetime
from rich import print

def get_forecast_data():
	url = (
		f"https://api.openweathermap.org/data/2.5/forecast?q={location}"
		f"&appid{get_config_data()['api_key']}&cnt={count}&units={unit}&lang={lang}"
	)

	try:
		response = requests.get(url)
		response.raise_for_status()
	except requests.HTTPError:
		status = response.status_code
        if status == 401:
            print("[orange1]Invalid API key.[/]")
        elif status == 404:
            print("[orange1]Invalid input. See pwy -h for more information.[/]")
        elif status in (429, 443):
            print("[orange1]API calls per minute exceeded.[/]")

        sys.exit(1)


	data = response.json()

	forecast_info = {

	}

	return forecast_info
