import urllib.request


HEADERS: dict = {
    "Accept": "*/*",
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.83 Safari/537.36",
    "DNT": "1",
}
# task__button js-task-button
url = "https://gdz.ru/class-8/geometria/atanasyan-8/"
# req = Request(url, headers=HEADERS)
with urllib.request.urlopen(url) as response:
    html = response.read().decode("utf-8")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(f"{html}")
