from flask import Flask
import requests
import json

coronavirus_monitor_headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "a2b7a42111msh85890ae2a8f427ep1bd07cjsn553e032b147d"
}

covid_19_coronavirus_statistics_headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "a2b7a42111msh85890ae2a8f427ep1bd07cjsn553e032b147d"
}

app = Flask(__name__)


@app.route('/coronavirus/masks')
def get_random_masks_usage_instructions():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/masks.php"

    response = requests.request("GET", url, headers=coronavirus_monitor_headers)

    return response.text


@app.route('/coronavirus/affected_countries')
def get_affected_countries():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/affected.php"

    response = requests.request("GET", url, headers=coronavirus_monitor_headers)

    return response.text


@app.route('/coronavirus/cases_by_particular_country/<string:country>')
def get_history_by_particular_country(country):
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_particular_country.php"

    country_text = str(country).lower().capitalize()
    querystring = {"country": country_text}

    response = requests.request("GET", url, headers=coronavirus_monitor_headers, params=querystring)

    return response.text


@app.route('/coronavirus/history_by_country_and_date/<string:country>/<string:date>')
def get_history_by_particular_country_by_date(country, date):
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/history_by_country_and_date.php"

    country_text = str(country).lower().capitalize()
    date_text = '{}-{}-{}'.format(str(date)[0:4], str(date)[4:6], str(date)[6:8])
    querystring = {"country": country_text, "date": date_text}

    response = requests.request("GET", url, headers=coronavirus_monitor_headers, params=querystring)

    return response.text


@app.route('/coronavirus/cases_by_country')
def get_cases_by_country():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/cases_by_country.php"

    response = requests.request("GET", url, headers=coronavirus_monitor_headers)

    return response.text


@app.route('/coronavirus/canada_stat_small')
def get_canada_covid19_general_statistic():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

    querystring = {"country": "Canada"}

    response = requests.request("GET", url, headers=coronavirus_monitor_headers, params=querystring)

    json_str = json.loads(response.text)
    candada_stats_str = json_str["latest_stat_by_country"][0]

    candada_stats_str.pop("id")
    candada_stats_str.pop("country_name")

    return str(candada_stats_str)


@app.route('/coronavirus/canada')
def get_canada_cases():
    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country": "Canada"}

    response = requests.request("GET", url, headers=covid_19_coronavirus_statistics_headers, params=querystring)

    return response.text


@app.route('/coronavirus/cases_by_particular_country/<string:country>')
def get_latest_stat_by_country_name(country):
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

    country_text = str(country).lower().capitalize()
    querystring = {"country": country_text}

    response = requests.request("GET", url, headers=coronavirus_monitor_headers, params=querystring)

    return response.text


@app.route('/coronavirus/worldstat')
def get_world_total_stat():
    url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/worldstat.php"

    response = requests.request("GET", url, headers=coronavirus_monitor_headers)

    return response.text


if __name__ == '__main__':
    app.run()