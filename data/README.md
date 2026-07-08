# Data

This folder does not track raw or large processed data (see `.gitignore`).

## `raw/`
Original data, exactly as downloaded from the source:

- **BTS On-Time Performance 2024:** download from [transtats.bts.gov](https://www.transtats.bts.gov/DL_SelectFields.aspx), selecting the columns listed in the main README.
- **NOAA / IEM ASOS:** historical weather data by station, obtained from the [Iowa Environmental Mesonet](https://mesonet.agron.iastate.edu/request/download.phtml).

## `processed/`
Clean, merged data, ready for the analysis notebook and dashboard:

- Result of merging BTS + NOAA by airport + date (and time, if applicable).
- Document here (or in the notebook) any cleaning decisions: dropped rows, airports without weather coverage, timezone handling.

## Airports Included (top 30 by traffic, U.S.)

_(Fill in with the final list of airport codes once defined — e.g. ATL, LAX, ORD, DFW, DEN, JFK...)_
