# Flight Delay Analytics

**Project 1 of 4 — Aviation Data Science Portfolio**

## Business Objective

What factors best predict operational flight delays? An integrated exploratory analysis of U.S. commercial flights, combining operational data with historical weather to identify delay patterns by airline, airport, season, and time of day.

## Data Sources

- **[BTS On-Time Performance](https://www.transtats.bts.gov/DL_SelectFields.aspx)** — Bureau of Transportation Statistics. Year: **2024**.
- **NOAA / IEM ASOS** — historical weather data by station/airport and date.

### Scope

- **Period:** full 2024 calendar year (to capture real seasonality).
- **Airports:** the 30 highest-traffic airports in the U.S.
- **Filtering:** flights departing from a top-30 airport (regardless of destination), since delay is measured at origin. Destination weather is available for 55.8% of rows (see `data/README.md` and notebook Section 1.2–1.3 for full rationale).
- **BTS columns used:**
  - Time: `FlightDate`, `Year`, `Month`, `DayofMonth`, `DayOfWeek`
  - Airline: `Reporting_Airline`
  - Origin: `Origin`, `OriginCityName`, `OriginState`
  - Destination: `Dest`, `DestCityName`, `DestState`
  - Departure: `CRSDepTime`, `DepTime`, `DepDelay`, `DepDelayMinutes`, `DepDel15`
  - Arrival: `CRSArrTime`, `ArrTime`, `ArrDelay`, `ArrDelayMinutes`, `ArrDel15`
  - Cancellations/Diversions: `Cancelled`, `CancellationCode`, `Diverted`
  - Distance: `Distance`
  - Delay causes: `CarrierDelay`, `WeatherDelay`, `NASDelay`, `SecurityDelay`, `LateAircraftDelay`

## Repository Structure

```
flight-delay-analytics/
├── README.md
├── RUBRIC.md              ← quality standard / self-assessment for this project
├── requirements.txt
├── .gitignore
├── data/
│   ├── raw/                (original, unprocessed data — not tracked in git)
│   └── processed/          (cleaned/merged data, ready for analysis)
├── notebooks/
│   └── 01_eda.ipynb        (main exploratory analysis notebook)
├── dashboard/
│   └── app.py              (interactive Streamlit dashboard)
└── outputs/
    └── figures/             (exported charts for the case study/README)
```

## Running This Project Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the notebook
jupyter notebook notebooks/01_eda.ipynb

# Run the dashboard
streamlit run dashboard/app.py
```

## Project Status

- [x] Week 1 — Data acquisition and integration (BTS + NOAA)
- [x] Week 2 — Integrated exploratory data analysis (EDA)
- [ ] Week 3 — Deployed dashboard + case study

## Case Study

*(To be added at the end of Week 3: problem → data → findings → impact)*

## Live Dashboard

*(Link to be added once deployed)*
