# import sys
# from pprint import pprint

# # pprint(f"main: {sys.path}")
from ast import Module
from klass_7.nemeckiy_yazik import (
    useful_functions_for_nemeckiy_yazik as nemeckiy_yazik_7,
)
from klass_7.informatika import useful_functions_for_informatika as informatika_7
from klass_7.geometria import useful_functions_for_geometria as geometria_7
from klass_7.russkii import useful_functions_for_russkii as russkii_7


from klass_8.geometria import useful_functions_for_geometria as geometria_8
from klass_8.russkii import useful_functions_for_russkii as russkii_8
from klass_8.nemeckiy_yazik import (
    useful_functions_for_nemeckiy_yazik as nemeckiy_yazik_8,
)
from klass_8.informatika import useful_functions_for_informatika as informatika_8

# url_on_dict_book = {"": ""}


def russkii_7_request_task_number_user_send_answer_for():
    quantity_urls = list(russkii_7.RUSSKII.keys())
    print(f"quantity_urls = {quantity_urls}")
    for i in quantity_urls:
        if russkii_7.RUSSKII[str(i)]["url"] != "":
            print(f'{i}) { russkii_7.RUSSKII[str(i)]["about"]}')

    book = str(int(input("enter the appropriate textbook: ")))
    exer = int(input("enter the numbeer of exercise: "))
    ans = russkii_7.download_gdz(russkii_7.RUSSKII[book]["url"], exer)
    print(ans)


def request_task_number_user_send_answer_for_7(
    source_answer: Module, url_on_dict_book: dict[str, dict[str, str]]
):
    quantity_urls = list(url_on_dict_book.keys())
    print(f"quantity_urls = {quantity_urls}")
    for i in quantity_urls:
        if url_on_dict_book[str(i)]["url"] != "":
            print(f'{i}) {url_on_dict_book[str(i)]["about"]}')

    book = str(int(input("enter the appropriate textbook: ")))
    exer = int(input("enter the numbeer of exercise: "))
    ans = source_answer.download_gdz(url_on_dict_book[book]["url"], exer)
    print(ans)


# download_gdz


# def geometria_7_request_task_number_user_send_answer_for():
#     quantity_urls = list(geometria_7.GEOMETRIA.keys())
#     for i in quantity_urls:
#         if geometria_7.GEOMETRIA[str(i)]["url"]:
#             print(f'{i}) {geometria_7.GEOMETRIA[str(i)]["about"]}')

#     book = str(int(input("Enter the appropriate textbook: ")))
#     exer = int(input("Enter the number of exercise: "))
#     ans = geometria_7.download_gdz(geometria_7.GEOMETRIA[book]["url"], exer)
#     print(ans)


# def russkii_8_request_task_number_user_send_answer_for():
#     quantity_urls = list(russkii_8.RUSSKII.keys())
#     print(f"quantity_urls = {quantity_urls}")
#     for i in quantity_urls:
#         if russkii_8.RUSSKII[str(i)]["url"] != "":
#             print(f'{i}) { russkii_8.RUSSKII[str(i)]["about"]}')

#     book = str(int(input("enter the appropriate textbook: ")))
#     exer = int(input("enter the numbeer of exercise: "))
#     ans = russkii_8.download_gdz(russkii_8.RUSSKII[book]["url"], exer)
#     print(ans)


# def geometria_8_request_task_number_user_send_answer_for():
#     quantity_urls = list(geometria_8.GEOMETRIA.keys())
#     for i in quantity_urls:
#         if geometria_8.GEOMETRIA[str(i)]["url"]:
#             print(f'{i}) {geometria_8.GEOMETRIA[str(i)]["about"]}')

#     book = str(int(input("Enter the appropriate textbook: ")))
#     exer = int(input("Enter the number of exercise: "))
#     ans = geometria_8.download_gdz(geometria_8.GEOMETRIA[book]["url"], exer)
#     print(ans)


def class_user_7():
    print("enter the object: ")
    print("1 - геометрия")
    print("2 - русский")
    print("3 - немецкий")
    print("4 - ")
    obj_user = int(input("-> "))
    match obj_user:
        case 1:
            request_task_number_user_send_answer_for_7(russkii_7, russkii_7.RUSSKII)
        case 2:
            request_task_number_user_send_answer_for_7(
                geometria_7, geometria_7.GEOMETRIA
            )
        case 3:
            request_task_number_user_send_answer_for_7(
                nemeckiy_yazik_7, nemeckiy_yazik_7.NEMECKIY_YAZIK
            )
        case 4:
            request_task_number_user_send_answer_for_7(
                informatika_7, informatika_7.INFORMATIKA
            )


def class_user_8():
    print("enter the object: ")
    print("1 - геометрия")
    print("2 - русский")
    print("3 - немецкий")
    print("4 - ")
    obj_user = int(input("-> "))
    match obj_user:
        case 1:
            request_task_number_user_send_answer_for_7(russkii_8, russkii_8.RUSSKII)
        case 2:
            request_task_number_user_send_answer_for_7(
                geometria_8, geometria_8.GEOMETRIA
            )
        case 3:
            request_task_number_user_send_answer_for_7(
                nemeckiy_yazik_8, nemeckiy_yazik_8.NEMECKIY_YAZIK
            )
        case 4:
            request_task_number_user_send_answer_for_7(
                informatika_8, informatika_8.INFORMATIKA
            )


def main():

    class_user = int(input("enter the your class(1-11): "))
    if class_user == 7:
        class_user_7()
    elif class_user == 8:
        class_user_8()
    else:
        print("We are not ready to solve your class assignment yet!!")


if __name__ == "__main__":
    main()
    # pass
