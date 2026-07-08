# Self-Assessment Rubric — Project 1: Flight Delay Analytics

**Adapted from:** ADY1100 (Data Preprocessing) course rubric — EA1 Integrated Exploratory Analysis
**Purpose:** a personal quality standard for Month 1 of the aviation portfolio, oriented toward a professional portfolio deliverable (GitHub + dashboard + case study), not academic grading.

**Business objective:** What factors best predict operational flight delays?

---

## Key Differences from the Original Rubric

- **Removed** the no-generative-AI restriction — this project uses AI as a working tool.
- **Removed** the 2-hour individual exam context with a pre-assigned dataset.
- **Added** a Data Acquisition and Integration section (BTS + NOAA), absent from the original since that dataset arrived already clean.
- **Transformed** the correlation analysis into Correlation + Temporal Patterns, since flight data has seasonality a static heatmap won't capture.
- **Added** a Product Layer (repo + dashboard + case study), since the real deliverable is for a recruiter, not a professor.
- **Redefined** outlier treatment: in flight data, an extreme delay is usually a real signal (storm, mechanical failure), not noise — the original rubric assumes outliers are always removed.

---

## 1. Data Acquisition and Integration — 15 pts

| Sub-criterion | Pts | What solid work demonstrates |
|---|---|---|
| 1.1 BTS dataset download and scope | 4 | Justifies the scope used (month, year, or sample) based on actual volume, not arbitrarily. Documents original vs. used rows/columns. |
| 1.2 Integration with NOAA/IEM ASOS data | 6 | Correctly merges by airport + date (and time, if applicable). Explicitly resolves timezone mismatches and stations without coverage. |
| 1.3 Documentation of the merge process | 5 | Explains in Markdown the decisions made during integration (what was discarded, what was approximated, why) — this is itself a portfolio finding, not an invisible step. |

---

## 2. Descriptive Statistics — 20 pts

| Sub-criterion | Pts | What solid work demonstrates |
|---|---|---|
| 2.1 Central tendency, dispersion, and position metrics | 8 | Calculated for relevant variables (`dep_delay`, `arr_delay`, etc.), **broken down** by airline, airport, and time block — not just on the full dataset. |
| 2.2 Business-context interpretation | 12 | Each metric is translated into an actionable statement (e.g. "75% of Airline X's flights are delayed less than Y minutes, but the long tail concentrates multi-hour delays — this affects connection planning"). |

---

## 3. Outliers: Detection and Critical Analysis — 15 pts

| Sub-criterion | Pts | What solid work demonstrates |
|---|---|---|
| 3.1 Method application (IQR or Z-score) | 5 | Method correctly applied with documented thresholds, on the relevant delay variables. |
| 3.2 Quantification and visualization | 4 | Boxplots with titles/labels; a table of how many outliers exist per variable and what % they represent. |
| 3.3 Critical judgment: noise or signal? | 6 | **The most important criterion in this section.** Outliers are not removed by default: investigate whether they correspond to real events (extreme weather, maintenance) and decide whether to analyze them separately instead of discarding them. Document the reasoning. |

---

## 4. Correlation and Temporal Patterns — 20 pts

| Sub-criterion | Pts | What solid work demonstrates |
|---|---|---|
| 4.1 Delay–weather correlation | 6 | Correlation matrix (Pearson/Spearman) between delay and weather variables (wind, precipitation, visibility), with a readable heatmap. |
| 4.2 Temporal and seasonal patterns | 8 | Analysis by time of day, day of week, and season using `groupby` aggregations and time series — not just a static matrix, since seasonality is central to the business problem. |
| 4.3 Identification of "bottleneck airports" | 6 | Combines delay, volume, and weather to identify which airports concentrate the problem, with business justification (not just the numeric ranking). |

---

## 5. Product Layer (Repo + Dashboard + Case Study) — 20 pts

| Sub-criterion | Pts | What solid work demonstrates |
|---|---|---|
| 5.1 Repository structure | 5 | Clear README, `requirements.txt`, organized folder structure (data/notebooks/dashboard separated). |
| 5.2 Deployed, functional dashboard | 10 | Live Streamlit/Plotly Dash (not just local), with real filters by route/airline/date that a non-technical person can explore on their own. |
| 5.3 Business case study | 5 | Problem → data → findings → impact, readable in under 3 minutes, in non-technical language — distinct from the notebook's internal conclusions. |

---

## 6. Documentation, Findings, and Reflection — 10 pts

| Sub-criterion | Pts | What solid work demonstrates |
|---|---|---|
| 6.1 Concrete findings | 4 | At least 3 specific, non-obvious findings, tied to the technique that revealed them. |
| 6.2 Limitations and business applications | 4 | At least 2 concrete limitations (e.g. BTS geographic coverage, inconsistent delay-cause reporting) and 2 real applications (airlines, airports, travelers). |
| 6.3 Ethical reflection | 2 | Considers possible biases (e.g. if different airlines report delay causes inconsistently). |

---

## Quick Checklist Before Closing Out Month 1

- [ ] The BTS + NOAA integration process is documented as part of the narrative, not hidden in an unexplained code cell.
- [ ] Outliers were critically investigated before deciding what to do with them — not removed by default.
- [ ] There's analysis of temporal/seasonal patterns, not just a static correlation matrix.
- [ ] The dashboard is publicly deployed and usable by someone without technical context.
- [ ] The case study reads in under 3 minutes and is in business language, not academic language.

---

**Total: 100 points** (Acquisition: 15 | Descriptive Statistics: 20 | Outliers: 15 | Correlation/Temporal: 20 | Product: 20 | Documentation: 10)
