import requests
from bs4 import BeautifulSoup


HEADERS: dict[str:str] = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
}


bad_url: str = "https://gdz.ru/po-algebre/8-klass/dorofeev"


def bad_to_good_URL(bad_url: str) -> str:
    """проверяет: cуществует ли такой url и можно ли с него парсить ответы"""
    b_url_split = bad_url.split("/")
    if len(b_url_split) > 4:
        good_url = f"https://gdz.ru/class-8/algebra/{b_url_split[5]}/"
        # print(f"good url = {good_url}\n")
        if chec_url_on_existence(obj_url=good_url):
            return good_url
    return ""


def chec_url_on_existence(us_exers: int = 77, obj_url: str = "") -> bool:
    """проверяет можно ли с этого url парсить ответы"""
    req = requests.get(f"{obj_url}{us_exers}-nom/", headers=HEADERS)
    soup = BeautifulSoup(req.text, "lxml")
    ls_url_img = []
    div_tasks = soup.find_all("div", {"class": "task-img-container"})
    for div_task in div_tasks:
        img_s = div_task.find_all("img")
        for i in img_s:
            form = (f'https:{i.get("src")}'.split("/"))[-1][-3::1]
            if form in ["jpg", "png"]:
                ls_url_img.append(f'https:{i.get("src")}')

    if len(ls_url_img) != 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print(bad_to_good_URL(bad_url))
