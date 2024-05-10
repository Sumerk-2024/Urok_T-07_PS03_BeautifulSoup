import requests  # Импорт модуля requests для выполнения HTTP запросов
from bs4 import BeautifulSoup  # Импорт BeautifulSoup из bs4 для парсинга HTML
from googletrans import Translator  # Импорт Translator для перевода текста

def get_english_words():
    url = "https://randomword.com/"  # URL-адрес сайта для получения случайных слов
    try:
        response = requests.get(url)  # Выполнение GET-запроса к указанному URL
        if response.status_code == 200:  # Проверка, что запрос выполнен успешно (код 200)
            soup = BeautifulSoup(response.content, "html.parser")  # Создание объекта BeautifulSoup для парсинга полученного HTML
            english_word = soup.find("div", id="random_word").text.strip()  # Поиск и извлечение текста из элемента div с id "random_word"
            word_definition = soup.find("div", id="random_word_definition").text.strip()  # Поиск и извлечение текста из элемента div с id "random_word_definition"
            return {
                "english_word": english_word,
                "word_definition": word_definition
            }  # Возвращение словаря с английским словом и его определением
        else:
            print("Не удалось получить данные с сайта")  # Сообщение об ошибке при неудачном статусе ответа
            return None
    except Exception as e:
        print(f"Произошла ошибка: {e}")  # Вывод сообщения об исключении, если оно произошло
        return None

def word_game(translator):
    print("Добро пожаловать в игру")  # Приветственное сообщение игры
    while True:  # Бесконечный цикл для продолжения игры
        word_dict = get_english_words()  # Получение слова и его определения
        if not word_dict:
            continue  # Продолжение цикла, если слово не было получено
        word = word_dict.get("english_word")  # Получение английского слова из словаря
        word_definition = word_dict.get("word_definition")  # Получение определения слова

        # Перевод слова и его определения на русский язык
        translated_word = translator.translate(word, dest='ru').text  # Перевод слова
        translated_definition = translator.translate(word_definition, dest='ru').text  # Перевод определения
        print(f"Значение слова - {translated_definition}")  # Вывод переведенного определения

        user = input("Что это за слово? ")  # Запрос пользователю угадать слово
        if user.lower() == translated_word.lower():
            print("Все верно!")  # Вывод сообщения, если пользователь угадал
        else:
            print(f"Ответ неверный, было загадано слово - {translated_word}")  # Сообщение о неверном ответе

        play_again = input("Хотите сыграть еще раз? да/нет ")  # Запрос на продолжение игры
        if play_again.lower() != "да":
            print("Спасибо за игру!")  # Прощальное сообщение, если пользователь не хочет продолжать
            break  # Выход из цикла

if __name__ == "__main__":  # Стандартная проверка в Python для определения, был ли модуль запущен как главный или импортирован
    translator = Translator()  # Создание объекта переводчика
    word_game(translator)  # Запуск игры
