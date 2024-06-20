import argparse
from pathlib import Path

def airport_influence(
    airport_data_path: Path,
    enplanement_data_path: Path,
    output_gpkg_path: Path,
):
    print(f"airport_data_path: {airport_data_path}")
    print(f"enplanement_data_path: {enplanement_data_path}")
    print(f"output_gpkg_path: {output_gpkg_path}")

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