from gdz import GDZ
from chec_url_algebra_on_existence import bad_to_good_URL


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

# проверяет url и добовляет его в файл
i = 1
while i < 12:
    for book in GDZ().books:
        if ("Алгебра" in book.title) and ("8" in book.title):
            url_book = bad_to_good_URL(f"https://gdz.ru{book.url}")
            if url_book != "":
                ALGEBRA[str(i)]["about"] = book.title
                ALGEBRA[str(i)]["url"] = url_book
                i += 1
                # print(f"loading... {i}/12")
                if i > 12:
                    break


with open(file="list_obj.txt", mode="w") as file:
    file.write(f"{ALGEBRA}")
