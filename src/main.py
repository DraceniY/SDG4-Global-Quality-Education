from pathlib import Path, PosixPath

import pandas as pd
import plotly.express as px
import plotly.offline as po


def create_map(sdg4_file: pd.DataFrame) -> px.choropleth:
    """
    Function creates map from SDG4 data.
    Args:
        sdg4_file: Path of SDG4.
    Results:
        figure: figure ojbect map.

    """
    sdg4_data = pd.read_csv(sdg4_file)

    figure = px.choropleth(
        sdg4_data,
        locations="Code",
        color="Percentage (%)",
        hover_name="Country",
        range_color=(0, 15),
        projection="natural earth",
        animation_frame="Year",
        title="Government expenditure on education as a percentage of GDP (%) per year",
    )
    return figure


def main():
    """
    Main function of the SDG4 program. In this function, we do the following tasks:
        1. Parses csv file.
        2. Creates map object
        3. Saves it in html format.
    """
    # Parse CSV file
    current_directory: Path = Path.cwd()
    data_directory = current_directory / ".." / "data"
    sdg4_file: Path = data_directory / "Global_gov_education.csv"

    # Create map object
    figure: px.choropleth = create_map(sdg4_file)

    # Save it in html
    po.plot(figure, filename="../data/Global_GDP_educationtest.html")


if __name__ == "__main__":
    # Call main function
    main()
