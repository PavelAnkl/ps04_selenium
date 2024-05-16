from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
import random

# Настройка драйвера
browser = webdriver.Chrome()

def search_wikipedia(query):
    # Кодируем запрос для URL
    url = "https://ru.wikipedia.org/wiki/" + quote(query)
    browser.get(url)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input("Нажмите Enter для продолжения...")

def choose_linked_article():
    hatnotes = []
    for element in browser.find_elements(By.CLASS_NAME, "hatnote"):
        if "navigation-not-searchable" in element.get_attribute("class"):
            hatnotes.append(element)
    if not hatnotes:
        print("Связанные статьи отсутствуют.")
        return

    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    browser.get(link)
    print(f"Переход на страницу: {link}")

def main():
    initial_query = input("Введите запрос для поиска на Википедии: ")
    search_wikipedia(initial_query)

    while True:
        print("\nВыберите действие:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            list_paragraphs()
        elif choice == "2":
            choose_linked_article()
            # Предложить снова листать параграфы или перейти на другую связанную страницу
            inner_choice = input("Введите 'p' для просмотра параграфов или 'a' для перехода на другую связанную страницу: ")
            if inner_choice == "p":
                list_paragraphs()
            elif inner_choice == "a":
                choose_linked_article()
            else:
                print("Неизвестная команда, возвращаемся к основному меню.")
        elif choice == "3":
            print("Завершение программы.")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите один из предложенных вариантов.")

    browser.quit()

if __name__ == "__main__":
    main()
