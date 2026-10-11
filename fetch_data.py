import csv
import json
import requests

# Request animated movie data.
url = "https://api.sampleapis.com/movies/animation"

response = requests.get(url, timeout=10)
response.raise_for_status()

# Convert the response into Python data.
movies = response.json()

print("Number of movies:", len(movies))

if movies:
    print("First movie:")
    print(json.dumps(movies[0], indent=4))

# Save as JSON.
with open("movies.json", "w", encoding="utf-8") as file:
    json.dump(movies, file, indent=4, ensure_ascii=False)

print("Data saved to movies.json")

# Save as CSV.
if movies:
    columns = list(dict.fromkeys(
        key for movie in movies for key in movie
    ))

    with open("movies.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(movies)

    print("Data saved to movies.csv")
else:
    print("No movies available to save as CSV.")