from gdz import GDZ
from chec_url_istoriya_on_existence import get_url_if_url_is_true
from customization import (
    name_file_in_which_textbooks_will_be_recorded,
    maximum_number_books,
    name_textbook,
    klass,
    dictionary_that_stores_links_to_textbooks,
)

BOOKS = {}

i = 1
n = 0
j = 2564

for book in GDZ().books:
    print(f"\r{n}/{j}", end="")
    n += 1
    if (name_textbook in book.title.lower()) and (klass in book.title):

        url_book = get_url_if_url_is_true(f"https://gdz.ru{book.url}")

        if url_book:
            if i > maximum_number_books:
                break

            BOOKS[str(i)] = {"about": book.title, "url": url_book}
            print(f"\nloading... {i}/{maximum_number_books}\n")
            i += 1


# This portion should be extracted to a separate function if needed for reuse
def write_books_to_file(file_name, data):
    with open(file=file_name, mode="w") as file:
        file.write(
            f"{dictionary_that_stores_links_to_textbooks}: dict[str, dict[str, str]] = {data}"
        )


write_books_to_file(name_file_in_which_textbooks_will_be_recorded, BOOKS)
