import os
import re
import fnmatch

def find_files_and_data(folder, letter, types):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if fnmatch.fnmatch(file, f'{letter}*#*.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    data = f.read()
                    for data_type in types:
                        if data_type == 'time':
                            times = re.findall(r'\b([01]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?\b', data)
                            print(f'Times found in {file}: {times}')
                        elif data_type == 'email':
                            emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', data)
                            print(f'Email addresses found in {file}: {emails}')

folder = 'task 2'
letter = 'A'
types = ['time', 'email']  

find_files_and_data(folder, letter, types)