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

ATL, DFW, DEN, ORD, CLT, LAX, PHX, LAS, SEA, LGA, MCO, BOS, DCA, SFO, DTW,
EWR, MSP, JFK, IAH, SLC, MIA, PHL, BNA, BWI, SAN, FLL, AUS, MDW, TPA, DAL

Selected by real traffic volume (origin + dest operations) from the BTS 2024
dataset itself — not from an external ranking. See `processed/top30_airports.csv`.

## Scope decision: origin-only filtering

Flights are filtered to those **departing** from a top-30 airport, regardless
of destination. Delay is measured at origin, so a flight like ATL→small-airport
is still valid signal for origin-delay analysis. Consequence: `dest_*` weather
columns are null whenever the destination isn't one of the 30 (see notebook
Section 1.2 for the exact coverage percentage).

## Known data quality findings from integration

- ASOS occasionally issues corrective/retransmitted reports within the same
  hour; deduplicated by keeping the earliest observation per (station, hour)
  before merging, to avoid row fan-out.
- ~1,044 BTS records show duplicate flight identifiers with differing delay
  values (likely schedule changes) — flagged for investigation in Section 2,
  not treated as a merge artifact.
