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
# Этап 1. Разминка: переменные, числа, math

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

# Этап 2. Условия и match


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

# Этап 3. Циклы

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


# Этап 4. Строки

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



# Этап 5. Списки

def titles_sorted_by_rating(movies):
    # list_tuples = [(movie["rating"], movie["title"]) for movie in movies]
    # list_tuples_sorted = sorted(list_tuples, reverse=True)
    # titles = [title for rating, title in list_tuples_sorted]
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    list_sorted_titles = [(movie["title"], movie["rating"]) for movie in sorted_movies]
    return [list_sorted_titles, sorted_movies]

print(titles_sorted_by_rating(movies)[0])


def top_n_by_rating(movies, n=3):
    top = titles_sorted_by_rating(movies)
    return top[:n]

print(top_n_by_rating(movies, n=3))


# Этап 6. Словари

def count_by_genre(movies):
    result = {}
    for movie in movies:
        for genre in movie["genres"]:
            result[genre] = result.get(genre, 0) + 1
    return result


print(count_by_genre(movies))


def actor_filmography(movies):
    result = {}
    for movie in movies:
        for actor in movie["actors"]:
            result[actor] = result.get(actor, []) + [movie["title"]]
    return result


print(actor_filmography(movies))


avg = average_rating(movies)
above_average = {
    movie["title"]: movie["rating"] for movie in movies if movie["rating"] > avg
}

print(above_average)


# Этап 7. Множества

def all_genres(movies):
    return {genre for movie in movies for genre in movie["genres"]}

print(all_genres(movies))

def common_actors(movie1, movie2):
    common_actors_set = set(movie1["actors"]) & set(movie2["actors"])
    return common_actors_set

print(common_actors(movies[0], movies[3]))


def genres_only_in_one(movies_a, movies_b):
    movies_a_genres = set(all_genres(movies_a)) - set(all_genres(movies_b))
    return movies_a_genres

print(genres_only_in_one(movies[5:6], movies[:5]))


# Этап 8. Итераторы и генераторы

def iter_high_rated(movies, min_rating=8.0):
    return (movie for movie in movies if movie["rating"] >= min_rating) # можно альтернативно через явный цикл и yield


for movie in iter_high_rated(movies):
    print(format_report_line(movie))


print(sum((m["duration_min"] for m in movies if m["rating"] > 7)))   # 713 


# Этап 9. Итоговый отчет

def build_report(movies):
    print(f"ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {catalog_age_stats(movies)[2]} лет \n\n")
    print("ТОП-3 фильма:")
    for movie in titles_sorted_by_rating(movies)[1][0:3]:
        print(f"{format_report_line(movie)}")
    print("\n\nФильмов по жанрам:\n")
    for genre, count in count_by_genre(movies).items():
        print(f"\t{genre}: {count}")
    print(f"Все жанры каталога: {", ".join(all_genres(movies))}")
build_report(movies)
                                             

if __name__ == '__main__':
    build_report(movies)