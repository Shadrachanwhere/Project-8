# 🎬 Movie Analysis

An exploratory data analysis of Best Picture Oscar winners, examining movie runtimes, award wins, and nominations using Python, jupyterlab and google slides

## Overview

This project analyses a dataset of notable films to answer three key questions:

- What was the runtime for each movie?
- Is there a relationship between runtime and the number of awards won?
- How many awards and nominations did each movie receive?

## Key Findings

| Finding | Result |
|---|---|
| Longest runtime | *12 Years a Slave* (~134 min) |
| Runtime–Awards correlation | 0.11 (negligible) |
| Most nominated film | *The Shape of water* (350 nominations) |
| Most awarded film | *Parasite* (309 wins) |

## Project Structure

```
├── movie_analysis.ipynb   # Main analysis notebook
├── movies.csv             # movies_request.py
└── README.md
```

## Requirements

- Python 3.8+
- pandas
- matplotlib
- seaborn

Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

## Usage

```bash
jupyter notebook movie_analysis.ipynb
```

## Analysis

### Runtime by Movie
A horizontal bar chart ranking all films by runtime in descending order. *12 Years a Slave* leads at approximately 140 minutes.

### Runtime vs. Awards Won
A regression plot exploring whether longer films win more awards. The correlation coefficient of **0.11** indicates a negligible linear relationship — runtime alone is not a meaningful predictor of award success.

### Awards vs. Nominations
A grouped bar chart comparing wins and nominations side by side for each film.  Parasit being the most awarded movie and The shape of water being 
the most nominated movie.
## Dataset

The dataset (`movies.csv`) includes the following columns:

- `Title` — Film title
- `Runtime` — Runtime in minutes
- `Wins` — Number of awards won
- `Nominations` — Number of award nominations
 
 Here is link to my  goolge slide presentation : https://docs.google.com/presentation/d/1bDeoK5ekdbFE-Y60M08H8LmRpMrbqhpECikpgXD6C8E/edit?usp=drive_link
 Here is the link  to the website where the movie api and details was retrieved : https://www.omdbapi.com/
