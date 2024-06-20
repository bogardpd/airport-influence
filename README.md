# airport-influence
Data processing tools for mapping small U.S. airports that only connect through a single hub airport

## Data Sources

This script depends on several data sources which must be set up before running the script.

### Downloaded

#### OurAirports

Most airports data comes from the **airports.csv** file available at [https://ourairports.com/data/](https://ourairports.com/data/). This CSV file must be downloaded to the local computer, and its local path must be provided as the `airport_data_path` argument.

#### FAA Emplanements Data

FAA emplanements data is used for [airport categories](https://www.faa.gov/airports/planning_capacity/categories).

Emplanement data spreadsheets can be downloaded from the FAA [Passenger Boarding &amp; All-Cargo Data](https://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger) page. Select the most recent calendar year of **Emplanements at All Commercial Service Airports (by Rank)**, and download the **cy[YY]-commercial-service-emplanements.xlsx** file to the local computer, where [YY] is a two-digit year. This Excel file's local path must be provided as the `emplanement_data_path` argument.

### API

Airline schedule data is sourced from FlightAware's [AeroAPI](https://www.flightaware.com/commercial/aeroapi/). This script requires an AeroAPI API key to be saved to the local computer's environment variables as `AEROAPI_KEY`.