import ruamel.yaml
import sys

write_file_name = 'D:\\База\\YandexDisk\\Школа\\ЕГЭ_1\\1.yaml'
import ruamel.yaml

data = {
    'description': 'This is a long \n description that will be folded in YAML.',
}

yaml = ruamel.yaml.YAML()
yaml.indent(offset=2)  # Устанавливаем отступ на 2 пробела

# Используем параметр default_style с ruamel.yaml.Dumper(), чтобы избежать добавления двух переводов строки
yaml.dump(data, sys.stdout)
