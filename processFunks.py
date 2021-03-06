# -*- coding: utf-8 -*-
from res.classifiers.MainCl import classify
from PyQt5 import QtCore
from time import sleep
import sqlite3
from random import choice
import requests
import pymorphy2
import subprocess
from res.classifiers.talk import pipe

morph = pymorphy2.MorphAnalyzer()
db = sqlite3.connect('base.db')
sql = db.cursor()
last_song = None
sql.execute(f"""SELECT genre FROM music""")
music_genres = list(set([str(i)[2:-3].lower() for i in sql.fetchall()]))


def transliteration(text):
    """
    Транслитерация
    :param text:
    :return text:
    """
    sites = {'москва': 'moscow', 'погода': 'barnaul'}
    if text in sites.keys():
        return sites[text]
    letters = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh',
               'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o',
               'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'ts',
               'ч': 'ch', 'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'y',
               'я': 'ya'}
    return ''.join([letters[i] for i in text])


class NumsGenForAnim(QtCore.QThread):
    """
    Класс для независимой генерации и передачи чисел
    для анимации кнопки отправки сообщения
    """
    my_sig = QtCore.pyqtSignal(list)

    def run(self):
        for num in range(1, 20):
            self.my_sig.emit([str(num), True])
            sleep(0.03)
        # sleep(1)
        for num in range(1, 20):
            self.my_sig.emit([str(num), False])
            sleep(0.03)


class MusicTime(QtCore.QThread):
    """
    Класс для генерации чисел в обратном отсчете
    """
    my_sig = QtCore.pyqtSignal(str)

    def __init__(self, num):
        super(MusicTime, self).__init__()
        self.minutes, self.seconds = (int(i) for i in num.split(':'))

    def run(self):
        while True:
            with open('res/Music/pause.txt') as file:
                n = int(file.read())
            if n == 1:
                sleep(1)
                continue
            sleep(1)
            if self.seconds != 0:
                self.seconds -= 1
            else:
                self.minutes -= 1
                self.seconds = 59
            if self.seconds == 0 and self.minutes == 0:
                self.my_sig.emit(f"Ещё?")
                break
            sec = self.seconds if self.seconds > 9 else f"0{self.seconds}"
            self.my_sig.emit(f"{self.minutes}:{sec}")


def text_progress(text):
    """
    Функция обработки входного текста
    принимает входной текст
    возвращает текст разбитый на строки
    подходящей для вывода длинны + ширину + высоту лейбла с текстом
    :param text:
    :return list:
    """
    res = []
    pres = ''
    for word in text.split():
        if len(pres + word) >= 25:
            if len(pres) >= 8:
                if len(word) >= 12:
                    word = word[:18 - len(pres)]
                res.append(f"{pres}{word}")
                pres = ''
            else:
                res.append(f"{pres}\n{word[:4]}")
                pres = word[4:] + ' '
                if len(pres) > 12:
                    pres = '...'
        else:
            pres += word + ' '
    res.append(pres)
    width = int((max([len(i) for i in res])) * 7.5) + 25
    height = (len(res) * 15) + 32
    return ('\n'.join(res)).strip(), width, height


def get_music(genre=None):
    """
    Функция находит случайную песню по жанру и возвращает ее
    в формате (ссылка, название, группа, длительность, жанр)
    :param genre:
    :return text:
    """
    global last_song
    if not genre:
        genre = choice(music_genres)
    print(genre)
    sql.execute(f"""SELECT * FROM music WHERE genre = '{morph.parse(genre.split()[-1])[0].normal_form.title()}'""")
    # sql.execute(f"""SELECT * FROM music WHERE path = 'res\Music\The Beatles - Yesterday.mp3'""")
    songs = sql.fetchall()
    if songs:
        song = choice(songs)
        while song == last_song:
            song = choice(songs)
        last_song = song
        return song


def get_genre(text):
    """
    Проверяем есть ли в тексте упоминание одного из жанров
    :param text:
    :return test:
    """
    i = [i for i in text.split() if morph.parse(i)[0].normal_form in music_genres]
    return i[0] if i else None


def get_weather(date=0, s_city="barnaul"):
    print(s_city)
    """
    Получаем погоду
    :param date:
    :param s_city:
    :return list:
    """
    res = requests.get(f"https://world-weather.ru/pogoda/russia/{s_city}/")
    s = res.text[res.text.find('<span class="dw-into">') + 22:res.text.find(
        '<span id="close-desc-weather">Скрыть</span>')].split(
        '<span id="open-desc-weather">Подробнее</span><br class="wwbr">')
    if 'облачно и дождь' in s[0].lower():
        se = 'res/weather/rain.gif'
    elif 'снег' in s[0].lower():
        se = 'res/weather/snow.gif'
    elif 'облачно' in s[0].lower():
        se = 'res/weather/cloud.gif'
    elif 'ясно' in s[0].lower():
        se = 'res/weather/sun.gif'
    else:
        se = 'res/weather/electro.gif'
    print(date, s_city)
    return s[date].strip(), se


def normalize_text(text):
    if 'FakeDictionary' in str(morph.parse(text.split()[0])[0].methods_stack):
        return 'False'
    elif str(morph.parse(text.split()[0])[0].tag) == 'LATN':
        return 'Latin'
    print(str(morph.parse(text.split()[0])[0].tag))
    command = f'pyaspeller "{text}"'
    res = subprocess.check_output(command)
    return res.decode('cp1251').strip()


def return_answer(text):
    """
    Создание ответа
    :param text:
    :return text:
    """
    if text == 'False':
        return 'я вас не понял'
    elif text == 'Latin':
        return 'я знаю только русский язык'

    res = classify(text)
    print(res)
    if res == 'False':
        res = pipe.predict([text])[0]
    elif 'погода' in res:
        print(1)
        city = 'barnaul'
        if 'в городе' in res:
            city = str(text).split(' в ')[-1].split()[0]
            city = morph.parse(city)[0].normal_form
            city = transliteration(city)
        time = 1 if '1' in res else 0
        return f'weather!{time}!{city}'
    elif 'музыка' in res:
        return 'music'
    return res

