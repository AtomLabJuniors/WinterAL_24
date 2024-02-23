import requests
from bs4 import BeautifulSoup
from config import HEADERS, ALGEBRA



def install_jpg(url: str) -> str:
    response = requests.get(url)
    name = (url.split("/"))[-1]
    with open(name, "wb") as file:
        file.write(response.content)
    return name


def main(us_exers: int, obj_url: str = "https://gdz.ru/class-8/algebra/makarychev-8/"):
    # https://gdz.ru/class-8/algebra/makarychev-8/6-nom/, https://gdz.ru/class-8/algebra/makarychev-8/6-nom/
    # print(f"conkrekt_url = {conkrekt_url}")
    req = requests.get(f"{obj_url}{us_exers}-nom/", headers=HEADERS)
    soup = BeautifulSoup(req.text, "lxml")

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


if __name__ == "__main__":
    print("выбирайте предмет")
    for i in range(1, 9):
        print(f'{i}: {ALGEBRA[str(i)]["about"]}')
    num_choose = str(input("выбирайте предмет: "))
    url = ALGEBRA[num_choose]["url"]
    a = main(us_exers=int(input("вводите номер упражнений:")), obj_url=url)
    print(a)
