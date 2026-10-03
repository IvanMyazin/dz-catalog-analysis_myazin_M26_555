from math import ceil
from typing import Any

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]}, # noqa: E501
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
# Этап 1

def average_rating(movies: dict):
    rating_list = [x["rating"] for x in movies]
    avg_score = sum(rating_list) / len(rating_list)
    return avg_score


def catalog_age_stats(movies: dict, current_year: int = 2026) -> tuple[Any]:
    film_ages = [current_year-x["year"] for x in movies]
    oldest_film = max(film_ages)
    yangest_film = min(film_ages)
    avg_age = sum(film_ages) / len(film_ages)
    return (oldest_film, yangest_film, ceil(avg_age))


def duration_in_hours(minutes):
    duration_hours = f"{minutes // 60}ч {minutes % 60}м"
    return duration_hours

# Этап 2


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
        case _ if year >= 2020:
            return "новые"
        case _ if 2020 > year >= 2015:
            return "недавние"
        case _:
            return "старые"

# Этап 3
# вариант 1 (длинный)
for x in movies:
    if "comedy" not in x["genres"]:
        print(x["title"])
    else:
        continue 
# вариант 2 (короче и понятнее)
[print(x["title"]) for x in movies if "comedy" not in x["genres"] ]


i = 0
while i < len(movies):
    if movies[i]["rating"] > 9:
        print(f"Найден шедевр: {movies[i]["title"]}")
    i += 1
else:
    "Шедевров не найдено"



def count_long_movies(movies, threshold=120):
    counter = 0
    for movie in movies:
        if movie["duration_min"] > 120:
            counter += 1
    return counter


# Этап 4

def normalize_title(title):
    name_split = title.split(" ")
    upper_name = [x[0].upper() + x[1:] for x in name_split]
    joined_str = " ".join(upper_name)
    return joined_str

print(normalize_title("silent hours"))

def make_slug(title):
    name_split = title.split(" ")
    lower_name = [x[0].lower() + x[1:] for x in name_split]
    joined_str = "-".join(lower_name)
    return joined_str

print(make_slug("Silent Hours"))

def format_report_line(movie):
    title = movie.get("title")
    year = movie.get("year")
    rating = movie.get("rating")
    dur_in_hour = duration_in_hours(movie.get("duration_min"))
    genres = ", ".join(movie.get("genres"))
    format_str = f"{normalize_title(title)} ({year}) - {rating}/10, {dur_in_hour}, жанры: {genres}" # noqa: E501
    return format_str

[print(format_report_line(movie)) for movie in movies]



# Этап 5




# if __name__ == '__main__':