from gdz import GDZ

ALGEBRA: dict = {
    "1": {"about": "", "autor": "", "year of manufacture": 201, "url": ""},
    "2": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "3": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "4": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "5": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "6": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "7": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "8": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "9": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "10": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "11": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
    "12": {"about": "", "autor": "", "year of manufacture": 200, "url": ""},
}

for i, book in enumerate(GDZ().books):
    if i > 12:
        break
    if ("Алгебра" in book.title) and ("8" in book.title):
        ALGEBRA[str(i)]["about"] = book.title
        ALGEBRA[str(i)]["url"] = f"https://gdz.ru{book.url}"
        


with open(file="list_obj.txt", mode="w") as file:
    file.write(f"{ALGEBRA}")
