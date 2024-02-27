import requests
from bs4 import BeautifulSoup
import yaml

import requests
from bs4 import BeautifulSoup

import requests

import requests

def save_html_page(url, filename):
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.content.decode('windows-1251'))

        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"HTML страница сохранена в файл: {filename}")
        body_onload_content = soup.find('body', {'onload': True}).text.strip()
        h1_content = soup.find('h1').text.strip()
        h2_content = soup.find('h2').text.strip()
        print(h1_content)
        print(h2_content)

        h1_input_data = soup.find('h1', text=h1_content)
        if h1_input_data:
            h1_input_data_text = h1_input_data.find_next('p', class_='text').text.strip()
        else:
            h1_input_data_text = None

        h2_input_data = soup.find('h2', text='Входные данные')
        if h2_input_data:
            h2_input_data_text = h2_input_data.find_next('p', class_='text').text.strip()
        else:
            h2_input_data_text = None

        h3_input_data = soup.find('h2', text='Выходные данные')
        if h3_input_data:
            h3_input_data_text = h3_input_data.find_next('p', class_='text').text.strip()
        else:
            h3_input_data_text = None
        print(h1_input_data)
        print(h1_input_data_text)
        print(h2_input_data)
        print(h2_input_data_text)
        print(h3_input_data)
        print(h3_input_data_text)

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Замените ссылку и имя файла по вашему выбору
url = 'https://acmp.ru/index.asp?main=task&id_task=4'
filename = 'C:\\Users\\Dima\\YandexDisk\\Школа\\ЕГЭ_1\\acmp_page.html'

# Сохраняем HTML-страницу в файл
save_html_page(url, filename)






