# Перемены для поиска подходящих учебников
name_textbook = "история"  # Имя предмета которого вы ищете
klass = "7"  # Класс по которым вы ищете этого предмета
structure_class_for_finding_all_exer = {
    "class": "task__button js-task-button"
}  # Название класса по которому будут происходить поиск ссылки на разные задания, по возможности не менять
# variable_first_exercise_starts = 8


# переменные для записи учебников в файл
maximum_number_books = 10  # Напишите Сколько максимум учебников вы бы хотели найти и записывать их в файл. по возможности не менять
name_file_in_which_textbooks_will_be_recorded = "list_obj_istoriya.py"  # Напишите название файлa в котором будут сохраняться найденные учебники
dictionary_that_stores_links_to_textbooks = "ISTORIYA"
# istoriya

# другие переменные
gdz_web = "https://gdz.ru"  # Название главного сайта
HEADERS: dict[str:str] = {  # Заголовок, по возможности не менять
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.2470 Safari/537.36",
}
