"""
Analyzes flight schedules to generate a GeoPackage of small airports
which only connect to or through a single hub airport.
"""
import argparse
import numpy as np
import pandas as pd
from pathlib import Path


def airport_influence(
    airport_data_path: Path,
    enplanement_data_path: Path,
    output_gpkg_path: Path,
):
    airports = merge_airport_data(airport_data_path, enplanement_data_path)
    print(airports)


def merge_airport_data(
    airport_data_path: Path,
    enplanement_data_path: Path,
) -> pd.DataFrame:
    """
    Merges FAA enplanement airport categories into airport data. 
    """
    CATEGORIES = {
        'P': { # Primary
            'L': "PL", # Large Hub
            'M': "PM", # Medium Hub
            'S': "PS", # Small Hub
            'N': "PN", # Nonhub
        },
        'CS': { # Nonprimary Commercial Service
            'None': "NN", # Nonhub
        }
    }

    # Load datasets:
    airports = pd.read_csv(airport_data_path)
    enplanements = pd.read_excel(
        enplanement_data_path,
        engine='openpyxl',
        keep_default_na=False,
        na_values=[""], # Parse 'None' as string
    )
    
    # Filter datasets:
    airports = airports[airports['iso_country'] == "US"]
    enplanements = enplanements[enplanements['RO'].notnull()]
    enplanements['Hub'] = enplanements.apply(
        lambda x: CATEGORIES[x['S/L']][x['Hub']],
        axis=1,
    )
    
    # Join datasets:
    merged = enplanements.join(airports.set_index('local_code'), on='Locid')

    # Rename and select columns:
    OUTPUT_COLS = {
        'gps_code': "ICAOCode",
        'iata_code': "IATACode",
        'Locid': "FAALocID",
        'name': "Name",
        'hub': "Hub",
        'latitude_deg': "Lat",
        'longitude_deg': "Lon",
    }
    merged = merged.rename(columns=OUTPUT_COLS)[[*OUTPUT_COLS.values()]]

    return merged

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Airport Influence",
        description=(
            "Data processing tool for mapping small U.S. airports that only "
            "connect through a single hub airport"
        ),
    )
    parser.add_argument(
        "airport_data_path",
        type=Path,
        help='Local path for OurAirports airports.csv data'
    )
    parser.add_argument(
        "enplanement_data_path",
        type=Path,
        help='Local path for FAA enplanements Excel spreadsheet'
    )
    parser.add_argument(
        "output_gpkg_path",
        type=Path,
        help='Path to save an output GeoPackage file'
    )
    args = parser.parse_args()
    airport_influence(
        args.airport_data_path,
        args.enplanement_data_path,
        args.output_gpkg_path,
    )