import urllib.request
import bs4

BeautifulSoup = bs4.BeautifulSoup
gdz_web = "https://gdz.ru"
HEADERS: dict = {
    "Accept": "*/*",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Safari/537.36",
    "DNT": "1",
}


def get_url_gdz_list(
    us_exers: int = 77, c_url: str = "https://gdz.ru/class-8/algebra/makarche-8/"
) -> list:
    """вернет список url ответов по какой-то номер епражнение"""
    #  = f"{obj_url}{us_exers}-nom/"
    with urllib.request.urlopen(c_url) as response:
        req = response.read().decode("utf-8")
    soup = BeautifulSoup(str(req), "lxml")

    ls_url_img = []
    div_tasks = soup.find_all("div", {"class": "task-img-container"})
    for div_task in div_tasks:
        img_s = div_task.find_all("img")
        # print((img_s))

        for i in img_s:
            form = (f'https:{i.get("src")}'.split("/"))[-1][-3::1]
            if form in ["jpg", "png"]:
                ls_url_img.append(f'https:{i.get("src")}')
                url_img = f'https:{i.get("src")}'
                # print(url_img)

                # install_jpg(url_img)

    return ls_url_img


# task__button js-task-button
try:
    url = "https://gdz.ru/class-8/geometria/merzlak/"
    # req = Request(url, headers=HEADERS)
    with urllib.request.urlopen(url) as response:
        html = response.read().decode("utf-8")
except urllib.error.HTTPError as e:
    print("nety")
    html = ""
soup = BeautifulSoup(str(html), "lxml")

all_exer_list: list[bs4.element.Tag] = soup.find_all(
    "a", {"class": "task__button js-task-button"}
)
# print(f"len = {len(t)}")
# print(f'title = {t[78].get("title")}\n url = {gdz_web}{t[78].get("href")}')
exer = int(input("enter num of exer: ")) - 1
url_exer = f'{gdz_web}{all_exer_list[exer].get("href")}'
ans = get_url_gdz_list(c_url=url_exer)
print(ans)
