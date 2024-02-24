from gdz import *

gdz = GDZ()

gdzList = [
    {
        "grade": 1,
        "Математика": [{"author": "Моро", "url": "https://gdz.ru/class-1/matematika/uchebnik-moro-volkova/"}, {"author": "Дорофеев", "url": "https://gdz.ru/class-1/matematika/dorofeev-g-v-mirakov-t-n-2011/"}],
        "Русский язык": [{"author": "Канакина", "url": "https://gdz.ru/class-1/russkii_yazik/reshebnik-kanakina-v-p-goreckiy-v-g/"}]
    },
    {
        "grade": 2,
        "Математика": [{"author": "Моро", "url": "https://gdz.ru/class-2/matematika/uchebnik-moro/"}, {"author": "Дорофеев", "url": "https://gdz.ru/class-2/matematika/dorofeev/"}],
        "Русский язык": [{"author": "Канакина", "url": "https://gdz.ru/class-2/russkii_yazik/kanakina-2/"}]
    },
    {
        "grade": 3,
        "Математика": [{"author": "Моро", "url": "https://gdz.ru/class-3/matematika/moro-i-bantova/"}, {"author": "Дорофеев", "url": "https://gdz.ru/class-3/matematika/dorofeev-3/"}],
        "Русский язык": [{"author": "Канакина", "url": "https://gdz.ru/class-3/russkii_yazik/kanakina-3/"}]
    },
    {
        "grade": 4,
        "Математика": [{"author": "Моро", "url": "https://gdz.ru/class-4/matematika/moro-i-bantova/"}, {"author": "Дорофеев", "url": "https://gdz.ru/class-4/matematika/dorofeev-4/"}],
        "Русский язык": [{"author": "Канакина", "url": "https://gdz.ru/class-4/russkii_yazik/kanakina-4/"}]
    },
    {
        "grade": 5,
        "Математика": [{ "author": "Виленкин", "url": "https://gdz.ru/class-5/matematika/vilenkin-shvacburd/"}, {"author": "Мерзляк", "url": "https://gdz.ru/class-5/matematika/merzlyak-polonskiy/"}],
        "Русский язык": [{"author": "Ладыженская", "url": "https://gdz.ru/class-5/russkii_yazik/ladyzhenskaya-t-a/"}]
    },
    {
        "grade": 6,
        "Математика": [{ "author": "Виленкин", "url": "https://gdz.ru/class-6/matematika/vilenkin-shvacburd/"}, {"author": "Мерзляк", "url": "https://gdz.ru/class-6/matematika/a-g-merzlyak/"}],
        "Русский язык": [{"author": "Ладыженская", "url": "https://gdz.ru/class-6/russkii_yazik/baranov-2008/"}]
    },
    {
        "grade": 7,
        "Алгебра": [{ "author": "Макарычев", "url": "https://gdz.ru/class-7/algebra/makarichev-18/"}, {"author": "Мерзляк", "url": "https://gdz.ru/class-7/algebra/merzlyak-polonskij/"}],
        "Геометрия": [{ "author": "Атанасян", "url": "https://gdz.ru/class-7/geometria/atanasyan-7-9/"}], 
        "Русский язык": [{"author": "Ладыженская", "url": "https://gdz.ru/class-7/russkii_yazik/baranova/"}]
    },
    {
        "grade": 8,
        "Алгебра": [{ "author": "Макарычев", "url": "https://gdz.ru/class-8/algebra/makarychev-8/"}, {"author": "Мерзляк", "url": "https://gdz.ru/class-8/algebra/merzlyak/"}],
        "Геометрия": [{ "author": "Атанасян", "url": "https://gdz.ru/class-8/geometria/atanasyan-8/"}],
        "Русский язык": [{"author": "Ладыженская", "url": "https://gdz.ru/class-8/russkii_yazik/trostencova-8/"}]
    },
    {
        "grade": 9,
        "Алгебра": [{ "author": "Макарычев", "url": "https://gdz.ru/class-9/algebra/makarichev-14/"}, {"author": "Мерзляк", "url": "https://gdz.ru/class-9/algebra/merzlyak/"}],
        "Геометрия": [{ "author": "Атанасян", "url": "https://gdz.ru/class-7/geometria/atanasyan-7-9/"}],
        "Русский язык": [{"author": "Ладыженская", "url": "https://gdz.ru/class-9/russkii_yazik/trostnecova-9/"}]
    },
    {
        "grade": 10,
        "Алгебра": [{ "author": "Мордкович", "url": "https://gdz.ru/class-10/algebra/reshebnik-mordkovich-a-g/"}],
        "Геометрия": [{ "author": "Атанасян", "url": "https://gdz.ru/class-10/geometria/atanasyan-10-11/"}],
        "Русский язык": [{"author": "Львова", "url": "https://gdz.ru/class-10/russkii_yazik/"}]
    },
    {
        "grade": 11,
        "Алгебра": [{ "author": "Мордкович", "url": "https://gdz.ru/class-10/algebra/reshebnik-mordkovich-a-g/"}],
        "Геометрия": [{ "author": "Атанасян", "url": "https://gdz.ru/class-10/geometria/atanasyan-10-11/"}],
        "Русский язык": [{"author": "Львова", "url": "https://gdz.ru/class-11/russkii_yazik/"}]
    }
]