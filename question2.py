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

for csv_filename in os.listdir(TEMPERATURE_FOLDER_PATH):
    if csv_filename.endswith(".csv"):
         path = os.path.join(TEMPERATURE_FOLDER_PATH, csv_filename)

         with open(path, "r") as file:
            reader = csv.DictReader(file)

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
    for season, temperature in season_temperatures.items():
        # temperature = season_temperatures[season]
        average = sum(temperature) / len(temperature)
        f.write(f"{season}: {average:.1f}°C\n")

max_range = 0
station_ranges = {}

for station in station_temperatures:
    temps = station_temperatures[station]
    if not temps:
        continue

    max_temp = max(temps)
    min_temp = min(temps)
    temp_range = max_temp - min_temp

    station_ranges[station] = (temp_range, max_temp, min_temp)

    if temp_range > max_range:
        max_range = temp_range

with open("largest_temp_range_station.txt","w", encoding="utf-8") as f:
    for station, (range_val ,range_max_temp, range_min_temp) in station_ranges.items():
        if range_val == max_range:
            f.write(
                f"{station}: Range {range_val:.1f}°C (Max: {range_max_temp:.1f}°C, Min: {range_min_temp:.1f}°C)\n"
            )
            