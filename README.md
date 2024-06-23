# Airport Influence
Data processing tools for mapping small U.S. airports that only connect through a single hub airport.

<mark>NOTE: this project is still under development, and is not yet fully implemented as described.</mark>

## Usage

`airport_influence.py airport_data_path enplanement_data_path output_gpkg_path [--force]`

- `airport_data_path`: OurAirports airports.csv file (see [Data Sources](#data-sources) below)
- `enplanement_data_path`: FAA enplanement spreadsheet (see [Data Sources](#data-sources) below)
- `output_gpkg_path`: Location to export a GeoPackage file (see [Output](#output) below). A cache file will also be created at the same location with the same name but a .sqlite3 extension.
- `--force` Overwrite existing output GeoPackage file without asking

## Output

This script creates a [GeoPackage](https://www.geopackage.org/) file with two layer tables: `Airports` and `Routes`.

### Airports (Point)

The Airports layer contains airport features for labeling points on a map. Only airports associated with Routes (e.g. hub airports and the airports that singularly connect through them) are included in this layer table.

| Field | Type | Purpose |
|-------|------|---------|
| fid | Integer64 | Feature ID |
| IATACode | String (3) | IATA code of the airport feature |
| IsHub | Boolean | True if this feature is a hub airport, false if this is an airport that only connects through a single hub airport |
| HubIATACode | String (3) | IATA code of the hub airport this airport feature connects through. If this feature *is* a hub airport, then its own IATA code should be used here. Used to allow styling categorization between different hubs and their influenced airports.

### Routes (LineString)

The Routes layer contains routes between hub airports and their singularly-connected airports, or route loops that singularly connect through a single hub. Only airports are vertices on these lines, so these routes are _not_ great circle routes.

| Field | Type | Purpose |
|-------|------|---------|
| fid | Integer64 | Feature ID |
| Name | String | A string of IATA codes describing the route, separated by hyphens. If this is a single airport paired with a hub, the hub shall be listed first (i.e. `DEN-GCC`). If this route is a loop that only connects through a single hub, the hub shall be listed first and last (i.e. `DEN-DVL-JMS-DEN`). |
| HubIATACode | String (3) | IATA code of the hub airport this route connects through. Used to allow styling categorization between routes influenced by each hub.

## Data Sources

This script depends on several data sources which must be set up before running the script.

### Downloaded

#### OurAirports

Most airports data comes from the **airports.csv** file available at [https://ourairports.com/data/](https://ourairports.com/data/). This CSV file must be downloaded to the local computer, and its local path must be provided as the `airport_data_path` argument.

#### FAA Enplanement Data

FAA enplanement data is used for [airport categories](https://www.faa.gov/airports/planning_capacity/categories).

Enplanement data spreadsheets can be downloaded from the FAA [Passenger Boarding &amp; All-Cargo Data](https://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger) page. Select the most recent calendar year of **Enplanements at All Commercial Service Airports (by Rank)**, and download the **cy[YY]-commercial-service-enplanements.xlsx** file to the local computer, where [YY] is a two-digit year. This Excel file's local path must be provided as the `enplanement_data_path` argument.

### API

Airline schedule data is sourced from FlightAware's [AeroAPI](https://www.flightaware.com/commercial/aeroapi/). This script requires an AeroAPI API key to be saved to the local computer's environment variables as `AEROAPI_KEY`.