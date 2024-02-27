import yaml
import ruamel.yaml
from docx import Document
import re
import openpyxl
import os
import textwrap


# Создайте объект YAML
yaml = ruamel.yaml.YAML(typ='rt')
base_folder = 'C:\\Users\\Dima\\YandexDisk\\Школа\\ЕГЭ_1'
open_file_name = base_folder+'\\1_type_1_150.yaml'
write_file_name=base_folder+'\\.yaml'

with open(open_file_name, 'r', encoding='utf-8') as file:
    yaml1 = ruamel.yaml.YAML()
    yaml1.default_style=''
    yaml1.width = 20000
    data = yaml1.load(file)

topic_list=[]
for i in range(0,149):
    print(data[17][i]['number kpolyakov'],data[17][i]['topic'])
    if not data[17][i]['topic'] in topic_list:
        topic_list.append(data[17][i]['topic'])
print(*topic_list,sep='\n')

        
                            



'''
#split_task_and_write(filetotasks(doc),17)
with open(write_file_name, 'w', encoding='utf-8') as file:

    yaml1.dump(data, file)

workbook.close()
'''





'''import ruamel.yaml

# Создайте объект YAML
yaml = ruamel.yaml.YAML(typ='rt')

# Загрузите YAML файл
with open('d:/База/YandexDisk/Школа/ЕГЭ_1/1.yaml', 'r', encoding='utf-8') as file:
    data = yaml.load(file)

# Измените значение "условие" с использованием SingleQuotedScalarString
data['Номер 17'][0]['условие'] = ruamel.yaml.scalarstring.FoldedScalarString('Новое значение условия')

# Сохраните обновленный YAML файл с разрешением использования Unicode, оригинальным порядком ключей
# и с использованием SingleQuotedScalarString для поля "условие"
with open('d:/База/YandexDisk/Школа/ЕГЭ_1/1.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(data, file)
'''


'''print(d)
tmp=[]
for i in d:
    for j in d[i]:
        print(j["номер поляков"]+'\n')
        print(j["подтип"]+'\n')
        if j["подтип"] not in tmp:
            tmp.append(j["подтип"])
        #for k in j["тип"]:
        #    print(k)
            
        #print('\n'+j["условие"]+'\n\n')
print(tmp)'''
