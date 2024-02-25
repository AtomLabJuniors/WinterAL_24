import sys

sys.path.append("d:\\\\gdz_bot\\\\WinterAL_24\\\\mini_projekt")
from klass_7.istoriya.list_obj_istoriya import ISTORIYA
import urllib.request, bs4

BeautifulSoup = bs4.BeautifulSoup
gdz_web = "https://gdz.ru"


def download_gdz(url_book: str, exer: int = 77) -> list:
    try:
        url_on_task = get_exer_url(url_book, exer)
        with urllib.request.urlopen(url_on_task) as response:
            req = response.read().decode("utf-8")
        soup = BeautifulSoup(req, "lxml")

        ls_url_img = [
            f'https:{i["src"]}'
            for div_task in soup.find_all("div", class_="task-img-container")
            for i in div_task.find_all("img")
            if i["src"].split("/")[-1][-3:] in ["jpg", "png"]
        ]

        return ls_url_img
    except Exception:
        return []


def get_exer_url(url_book: str, exer: int = 77) -> str:
    exer_url = ""
    try:
        with urllib.request.urlopen(url_book) as response:
            html = response.read().decode("utf-8")
        soup = BeautifulSoup(html, "lxml")
        exer_url = f'{gdz_web}{soup.find(
        "a", {"class": "task__button js-task-button", "title":f"{exer}"}).get("href")}'

        return exer_url
    except Exception:
        return ""


if __name__ == "__main__":
    quantity_urls = list(ISTORIYA.keys())
    for i in quantity_urls:
        if ISTORIYA[str(i)]["url"]:
            print(f'{i}) {ISTORIYA[str(i)]["about"]}')

    book = str(int(input("Enter the appropriate textbook: ")))
    exer = int(input("Enter the number of exercise: "))
    ans = download_gdz(ISTORIYA[book]["url"], exer)
    print(ans)
