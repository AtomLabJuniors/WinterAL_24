# import chec_url_geometria_on_existence
from list_obj_geometria import GEOMETRIA
import urllib, bs4

BeautifulSoup = bs4.BeautifulSoup
gdz_web = "https://gdz.ru"


def dowload_gdz(url_book: str, exer: int = 77) -> list:
    try:
        url_on_task = get_exer_url(url_book)
        with urllib.request.urlopen(url_on_task) as response:
            req = response.read().decode("utf-8")
        soup = BeautifulSoup(str(req), "lxml")

        ls_url_img = []
        div_tasks = soup.find_all("div", {"class": "task-img-container"})
        for div_task in div_tasks:
            img_s = div_task.find_all("img")
            for i in img_s:
                form = (f'https:{i.get("src")}'.split("/"))[-1][-3::1]
                if form in ["jpg", "png"]:
                    ls_url_img.append(f'https:{i.get("src")}')
        return ls_url_img
    except Exception:
        return []


def get_exer_url(url_book: str, exer: int = 77) -> str:
    """проверяет: cуществует ли такой url и можно ли с него парсить ответы"""
    exer -= 1
    exer_url = ""
    try:
        with urllib.request.urlopen(url_book) as response:
            html = response.read().decode("utf-8")
        soup = BeautifulSoup(str(html), "lxml")

        all_exer_list: list[bs4.element.Tag] = soup.find_all(
            "a", {"class": "task__button js-task-button"}
        )
        # print(f'title = {t[78].get("title")}\n url = {gdz_web}{t[78].get("href")}')
        exer_url = f'{gdz_web}{all_exer_list[exer].get("href")}'
        return exer_url
    except Exception:
        return ""


if __name__ == "__main__":
    for i in range(1, 7):
        if GEOMETRIA[str(i)]["url"] != "":
            print(f'{i}) { GEOMETRIA[str(i)]["about"]}')

    book = str(int(input("enter the appropriate textbook: ")))
    exer = int(input("enter the numbeer of exercise: "))
    ans = dowload_gdz(GEOMETRIA[book]["url"], exer)
    print(ans)
