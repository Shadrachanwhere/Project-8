import csv
import re
import requests
from keys import api_key

OMDB_URL = "http://www.omdbapi.com/"


def fetch_movie_data(csv_path="oscar_winners.csv"):
    results = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            imdb_id = row["IMDB"]
            response = requests.get(OMDB_URL, params={"i": imdb_id, "apikey": api_key})
            response.raise_for_status()
            results.append(response.json())
    return results


def _parse_runtime(value):
    match = re.search(r"\d+", value or "")
    return int(match.group()) if match else None


def _parse_awards(value):
    wins = re.search(r"(\d+)\s+win", value or "", re.IGNORECASE)
    noms = re.search(r"(\d+)\s+nomination", value or "", re.IGNORECASE)
    return (
        int(wins.group(1)) if wins else None,
        int(noms.group(1)) if noms else None,
    )


def _parse_box_office(value):
    digits = re.sub(r"[^\d]", "", value or "")
    return int(digits) if digits else None


def save_movies_csv(movies, output_path="movies.csv"):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Runtime", "Genre", "Wins", "Nominations", "BoxOffice"])
        for movie in movies:
            wins, noms = _parse_awards(movie.get("Awards", ""))
            writer.writerow([
                movie.get("Title"),
                _parse_runtime(movie.get("Runtime", "")),
                movie.get("Genre"),
                wins,
                noms,
                _parse_box_office(movie.get("BoxOffice", "")),
            ])


if __name__ == "__main__":
    movies = fetch_movie_data()
    save_movies_csv(movies)
