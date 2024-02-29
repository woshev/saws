import requests


def list_files(access_token):
    headers = {"Authorization": f"OAuth {access_token}"}
    url = "https://cloud-api.yandex.net/v1/disk/resources/files"

    # Первый запрос, чтобы получить список файлов на диске
    response = requests.get(url, headers=headers)

    # Проверка успешности запроса
    if response.status_code == 200:
        response_json = response.json()

        # Проверка наличия ключа "_embedded"
        if (
            "_embedded" in response_json
            and "items" in response_json["_embedded"]
        ):
            files_data = response_json["_embedded"]["items"]

            # Вывод имен файлов построчно
            for file_data in files_data:
                print(file_data["name"])
        else:
            print("На диске нет файлов.")
    else:
        print("Ошибка при получении списка файлов.")


# Ваш токен доступа к Яндекс.Диску
access_token = "y0_AgAAAABlD3sVAAtehQAAAAD8isw-AACzAeLFb2BI540PlN6EEGlYaHCUAw"

list_files(access_token)
