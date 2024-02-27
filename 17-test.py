import os
print(os.getcwd())
def read_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found:", file_path)
    except Exception as e:
        print("Error occurred:", e)
read_data_from_file('17-test.txt')