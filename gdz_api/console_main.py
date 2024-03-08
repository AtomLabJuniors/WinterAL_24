import gdz_api as g
from time import time
from all_books1 import all_books


def main():
    # это образец использования: как функции вызывать, архитектура диалога и т.п.

    user_book_class: str = input(
        "Класс: "
    ).strip()  # Возвращает копию строки с удаленными начальными и конечными пробелами.

    user_book_subject: str = input("Предмет: ").strip()
    books: dict = {}
    url_books: dict = {}
    i = 0
    st = time()
    print("the search for a suitable book is underway...")
    for book in all_books[user_book_class]:
        if user_book_subject in book.title.lower():
            i += 1
            books[f"{i}"] = book.title
            url_books[f"{i}"] = f"https://gdz.ru{book.url}"
    if not books:
        return print("Такой книги нет")

    print(f"\nIt took {time()-st} s to find the right book\n")
    print(f"Выбери книгу и перешли её номер -> {books}")
    book_num = input("url книги: ")
    url: str = url_books[str(book_num)]
    print(g.get_sections(url))
    section = input("Название интересующей секции: ").strip()
    print(g.get_numbers(url, section))
    num = input("Номер: ").strip()
    num_url: list = g.get_number_url(url, section, num)
    if not num_url:
        return print("Такого номера не нашлось")
    answers = g.get_answer_url(num_url[0])
    print("Ответы:")
    for index in range(len(answers)):
        print(answers[index])


if __name__ == "__main__":
    main()
