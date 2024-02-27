import re

def extract_task_and_topic_numbers(string):
    # Шаблон для поиска номера задачи и номера темы
    pattern = r'(\d+)[^\d]*(\d+)?\.py'
    #pattern = r'(\d+)[\W_]*(\d+)?\.py'
    # Поиск совпадений по шаблону в строке
    match = re.search(pattern, string)

    if match:
        print(match.groups())
        number=match.groups()
        if match.group(2) == None:
            topic_number = None
            task_number = int(match.group(1))
        elif match.group(1) != None and match.group(2) != None:
            topic_number = int(match.group(1))
            task_number = int(match.group(2))
        return task_number, topic_number
    else:
        # Номер задачи не найден
        return None, None

# Примеры использования
examples = ["32.py", "ege17-32.py", "17-32.py", "task32.py","номер_2_17_31.py","zadanie 1 february.py"]

for example in examples:
    task_number, topic_number = extract_task_and_topic_numbers(example)
    print(f"Имя файла: {example}")
    print(f"Номер задачи: {task_number}")
    print(f"Номер темы: {topic_number}")
    print()
