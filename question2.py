import os
import csv
import math

TEMPERATURE_FOLDER_PATH = "temperatures"
MONTHS = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

def get_season(month):
    if month in ["December", "January", "February"]:
        return "Summer"
    elif month in ["March", "April", "May"]:
        return "Autumn"
    elif month in ["June", "July", "August"]:
        return "Winter"
    else:
        return "Spring"
     
season_temperatures = {
    "Summer":[],
    "Autumn":[],
    "Winter":[],
    "Spring": [],
}

station_temperatures = {}

for csv_file in os.listdir(TEMPERATURE_FOLDER_PATH):
    if csv_file.endswith(".csv"):
         path = os.path.join(TEMPERATURE_FOLDER_PATH, csv_file)

         with open(path, "r") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                station_name = row["STATION_NAME"]
                if station_name not in station_temperatures:
                    station_temperatures[station_name] = []

                for month in MONTHS:
                    temperature_str = row[month]

                    if temperature_str == "" or temperature_str.lower() == "nan":
                        continue

                    temperature = float(temperature_str)
                    season = get_season(month)

                    season_temperatures[season].append(temperature)
                    station_temperatures[station_name].append(temperature)
                    
with open("average_temperature.txt", "w", encoding="utf-8") as f:
    for season in season_temperatures:
        temperature = season_temperatures[season]
        average = sum(temperature) / len(temperature)
        f.write(f"{season}: {average:.1f}°C\n")