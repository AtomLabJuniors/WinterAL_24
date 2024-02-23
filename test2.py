import requests
import bs4
from gdz import GDZ


def get_answer_img_url(url: str = "") -> list:
    if url == "" or type(url) is not str:
        return list()

    result: list = []
    head: dict = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
    }
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(
        requests.get(url, headers=head).text, "lxml"
    )
    img_s: bs4.element.ResultSet = (
        soup.find("div", {"class": "entry-content", "itemprop": "articleBody"})
    ).find_all("img", {"decoding": "async"})
    for i in img_s:
        form = (f'https://gdz.red{i.get("src")}'.split("/"))[-1][-3::1]
        if form == "jpg":
            result.append(f'https://gdz.red{i.get("src")}')

    return result


if __name__ == "__main__":
    gdz = GDZ()
    # print(get_answer_img_url("https://gdz.red/8-klass/8-algebra/algebra-8-klass-uchebnik-makarychev/8-algebra-makarychev-upr-5.html"))

    for book in gdz.books:
        if "Алгебра" in book.title:
            if "8" in book.title:
                print(book.title, f" https://gdz.ru./{book.url}")
