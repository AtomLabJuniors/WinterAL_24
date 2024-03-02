import gdz as t
import gdz_api as g

res_sourt: dict[str, list[t.Book]] = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
    "5": [],
    "6": [],
    "7": [],
    "8": [],
    "9": [],
    "10": [],
    "11": [],
}
gdz: t.GDZ = t.GDZ()
ls_books = list(gdz.books)
# while j < 11:
j =0
for b in ls_books:
    
    if  g.check_url_on_existence(f"https://gdz.ru{b.url}"):
        b.description = ''
        j += 1
        print(f"\r{j}/2564", end='')
        
        for clas in b.classes:
            res_sourt[f"{clas}"].append(b)
with open("all_books1.py", "w")as f:
    f.write(f'from gdz_api import * \nall_books = {res_sourt} ')