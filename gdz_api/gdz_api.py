import bs4
import requests
def get_answer_url(question_url: str = '') -> list:
    soup = bs4.BeautifulSoup(requests.get(question_url).text, "lxml")

    result = []
    div_tasks = soup.find_all("div", {"class": "task-img-container"})
    for div_task in div_tasks:
        img_s = div_task.find_all("img")
        for i in img_s:
            form = (f'https:{i.get("src")}'.split("/"))[-1][-3::1]
            if form in ["jpg", "png"]:
                result.append(f'https:{i.get("src")}')

    return result


def get_number_url(book_url: str = '', title_sections: str = '', title_num: str = '') -> list:
    result: list = []
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(requests.get(book_url).text, "lxml")

    task_list = soup.find("div", class_="task__list")
    sections = task_list.find_all("section")
    for section in sections:
        if title_sections in str(section.find(class_="heading").text):
            questions = section.find_next("div").find_all("a", {"class": "task__button js-task-button"})
            for question in questions:
                if title_num in question.get("title") and type(question) is bs4.element.Tag:
                    result.append(f"https://gdz.ru{question.get("href")}")

    return result


def get_sections(book_url: str = '') -> list:
    result: list = []
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(requests.get(book_url).text, "lxml")

    task_list = soup.find("div", class_="task__list")
    sections = task_list.find_all("section")
    for section in sections:
        result.append(section.find(class_="heading").text)

    return result


def get_numbers(book_url: str = '', title_sections: str = '') -> list:
    result: list = []
    soup: bs4.BeautifulSoup = bs4.BeautifulSoup(requests.get(book_url).text, "lxml")

    task_list = soup.find("div", class_="task__list")
    sections = task_list.find_all("section")
    for section in sections:
        if title_sections in str(section.find(class_="heading").text):
            questions = section.find_next("div").find_all("a", {"class": "task__button js-task-button"})
            for question in questions:
                result.append(question.text)

    return result

def check_url_on_existence(url: str) -> bool:
    try:
        chec = str(requests.get(url).reason).lower()
        

        return True if chec=="ok" else False
    except Exception:
        return False

