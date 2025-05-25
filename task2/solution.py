import csv
import sys
from collections import Counter, defaultdict
from sys import flags

import requests
from bs4 import BeautifulSoup

def animal_parse():
    url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'
    alphabet = []
    sorted_alphabet = None
    flag = False

    while url:
        contents = requests.get(url).text
        soup = BeautifulSoup(contents, 'html.parser')
        content_div = soup.find('div', attrs = {'class':'mw-category-columns'})

        for raw in content_div.select('li'):
            first_letter = raw.a.text[0]
            if first_letter == 'A':
                count = Counter(alphabet)
                sorted_alphabet = dict(sorted(count.items()))
                flag = True
            else:
                if first_letter in "ЯЮЭЬЫЪЩШЧЦХФУТСРПОНМЛКЙИЗЖЁЕДГВБА":
                    alphabet.append(first_letter)
        if flag:
            break
        url = "https://ru.wikipedia.org" + soup.find('a', text='Следующая страница').get('href')


    with open("beasts.csv", mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if sorted_alphabet:
            for letter, v in sorted_alphabet.items():
                writer.writerow([letter, v])

animal_parse()