import urllib.request
from bs4 import BeautifulSoup
from customization import structure_class_for_finding_all_exer, gdz_web

# russkii
def check_url_on_existence(url: str) -> bool:
    try:
        with urllib.request.urlopen(url) as response:
            req = response.read().decode("utf-8")

        soup = BeautifulSoup(req, "lxml")
        ls_url_img = [
            f'https:{i["src"]}'
            for i in soup.select("div.task-img-container img")
            if i["src"].split("/")[-1][-3:] in ["jpg", "png"]
        ]

        return len(ls_url_img) > 0
    except Exception:
        return False


def get_url_if_url_is_true(url):
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode("utf-8")

        soup = BeautifulSoup(html, "lxml")
        exer_url = f'{gdz_web}{soup.find(
        "a", {"class": "task__button js-task-button", "title":f"{78}"}).get("href")}'

        if check_url_on_existence(url=exer_url):
            return url
        return ""
    except Exception:
        return ""


if __name__ == "__main__":
    print(get_url_if_url_is_true("https://gdz.ru/58043"))
