import ruamel.yaml

# Создайте объект YAML
yaml = ruamel.yaml.YAML(typ='rt')
write_file_name='C:\\Users\\Dima\\YandexDisk\\Школа\\ЕГЭ_1\\1.yaml'
# Загрузите YAML файл
with open(write_file_name, 'r', encoding='utf-8') as file:
    data = yaml.load(file)

# Измените значение "условие" с использованием SingleQuotedScalarString
#data['17'][0]['условие'] = ruamel.yaml.scalarstring.FoldedScalarString('Новое значение условия')
print(data[17][0])
#data[17].append({})
def write(data,number_kpolyakov):
        ege_type=17
        try:
             l = len(data[17])
        except:            
            data[17].append({'ege type':'',
                    'type':'',
                    'author':'',
                    'number kpolyakov':'',
                    'task description': '',
                    'input data':'',
                    'input file':'',
                    'ansver':'',
                    'solve text Python':'',
                    'solve file Python':'',
                    'solve text Pascal':'',
                    'solve file Pascal':'',                               
                    'solve youtube':''
                    })
        if number_kpolyakov < l:
            data[ege_type][number_kpolyakov-1]['type'] = ruamel.yaml.scalarstring.PlainScalarString('1')
            data[ege_type][number_kpolyakov-1]['author'] = ruamel.yaml.scalarstring.PlainScalarString('2')
            data[ege_type][number_kpolyakov-1]['number kpolyakov'] = ruamel.yaml.scalarstring.PlainScalarString(number_kpolyakov)
            data[ege_type][number_kpolyakov-1]['task description'] = ruamel.yaml.scalarstring.FoldedScalarString('task')
            data[ege_type][number_kpolyakov-1]['ege type'] = ruamel.yaml.scalarstring.PlainScalarString('name')
            data[ege_type][number_kpolyakov-1]['input data'] = ruamel.yaml.scalarstring.PlainScalarString('input_data')
            data[ege_type][number_kpolyakov-1]['input file'] = ruamel.yaml.scalarstring.PlainScalarString('input_file')
            data[ege_type][number_kpolyakov-1]['answer'] = ruamel.yaml.scalarstring.PlainScalarString('input_file')
            data[ege_type][number_kpolyakov-1]['solve text Python'] = ruamel.yaml.scalarstring.PlainScalarString('solve_text_python')
            data[ege_type][number_kpolyakov-1]['solve file Python'] = ruamel.yaml.scalarstring.PlainScalarString('solve_file_python')
            data[ege_type][number_kpolyakov-1]['solve text Pascal'] = ruamel.yaml.scalarstring.PlainScalarString('solve_text_pascal')
            data[ege_type][number_kpolyakov-1]['solve file Pascal'] = ruamel.yaml.scalarstring.PlainScalarString('solve_file_pascal')
            data[ege_type][number_kpolyakov-1]['solve youtube'] = ruamel.yaml.scalarstring.PlainScalarString('solve_youtube')
        else:
            data[17].append({'ege type':'',
                    'type':'',
                    'author':'',
                    'number kpolyakov':'',
                    'task description': '',
                    'input data':'',
                    'input file':'',
                    'answer':'',
                    'solve text Python':'',
                    'solve file Python':'',
                    'solve text Pascal':'',
                    'solve file Pascal':'',                               
                    'solve youtube':''
                    })

tmp = [(17, '', 255, 'В файле 17-205.txt. содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно. Определите количество пар чисел, в которых хотя бы один из двух элементов больше, чем наибольшее из всех чисел в файле, делящихся на 173, и в троичной записи хотя бы одного элемента из двух содержится сочетание цифр 22. В ответе запишите два числа: сначала количество найденных пар, а затем – минимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.', '4525\n6347\n5361\n1163\n-5880', '17-205.txt', '184 10920', '', '', '', '', 'https://youtu.be/rImSNXOO3sc')]
print('\n\n')
print(*tmp[0])
for i in tmp:
     write(data,*i)
# Сохраните обновленный YAML файл с разрешением использования Unicode, оригинальным порядком ключей
# и с использованием SingleQuotedScalarString для поля "условие"
with open(write_file_name, 'w', encoding='utf-8') as file:
    yaml.dump(data, file)
'''
        print("number",number_kpolyakov-1)
        # Измените значение "условие" с использованием SingleQuotedScalarString
        data[ege_type][number_kpolyakov-1]['type'] = ruamel.yaml.scalarstring.PlainScalarString(type)
        data[ege_type][number_kpolyakov-1]['aythor'] = ruamel.yaml.scalarstring.PlainScalarString(author)
        data[ege_type][number_kpolyakov-1]['number kpolyakov'] = ruamel.yaml.scalarstring.PlainScalarString(number_kpolyakov)
        data[ege_type][number_kpolyakov-1]['task description'] = ruamel.yaml.scalarstring.FoldedScalarString(task)
        data[ege_type][number_kpolyakov-1]['ege type'] = ruamel.yaml.scalarstring.PlainScalarString(name)
        data[ege_type][number_kpolyakov-1]['input data'] = ruamel.yaml.scalarstring.PlainScalarString(input_data)
        data[ege_type][number_kpolyakov-1]['input file'] = ruamel.yaml.scalarstring.PlainScalarString(input_file)
        data[ege_type][number_kpolyakov-1]['answer'] = ruamel.yaml.scalarstring.PlainScalarString(input_file)
        data[ege_type][number_kpolyakov-1]['solve text Python'] = ruamel.yaml.scalarstring.PlainScalarString(solve_text_python)
        data[ege_type][number_kpolyakov-1]['solve tile Python'] = ruamel.yaml.scalarstring.PlainScalarString(solve_file_python)
        data[ege_type][number_kpolyakov-1]['solve text Pascal'] = ruamel.yaml.scalarstring.PlainScalarString(solve_text_pascal)
        data[ege_type][number_kpolyakov-1]['solve tile Pascal'] = ruamel.yaml.scalarstring.PlainScalarString(solve_file_pascal)
        data[ege_type][number_kpolyakov-1]['solve youtube'] = ruamel.yaml.scalarstring.PlainScalarString(solve_youtube)
        yaml.dump(data, file)
    else:
        data[ege_type].append({'ege type':ege_type,
                               'type':type,
                               'author':author,
                               'number kpolyakov':number_kpolyakov,
                               'task description': task,
                               'input data':input_data,
                               'input file':input_file,
                               'ansver':answer,
                               'solve text Python':solve_text_python,
                               'solve file Python':solve_file_python,
                               'solve text Pascal':solve_text_pascal,
                               'solve file Pascal':solve_file_pascal,                               
                               'solve youtube':solve_youtube
                                })
        yaml.dump(data, file)
    return data
'''