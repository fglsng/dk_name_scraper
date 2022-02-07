import csv
import string

class Rule:
    vowels = ['a','e','i','o','u','y','æ','ø','å','á','é','í','ó','ú','ë','ä','ö','ü']

class Name:
    def __init__(self, name: str, marker: str):
        self.name = name
        self.marker = marker

def get_names(path: str):
    names = []
    with open(path) as csv_file:
        rows = csv.reader(csv_file, delimiter=';')

        for row in rows:
            names.append(Name(row[0], row[1]))

    return names


def find_names_with_specific_number_of_vowels(names, vowels:int):
    specific_names = []
    for name in names:
        if len([i for i in name.name if i.lower() in Rule.vowels]) == vowels:
            specific_names.append(name)
            print(name.name)
    
    return specific_names

def find_names_with_vowels_up_to(names, max_vowels:int):
    specific_names = []
    for name in names:
        if len([i for i in name.name if i.lower() in Rule.vowels]) <= max_vowels:
            specific_names.append(name)
            print(name.name)
    
    return specific_names

def find_names_with_specific_length(names, length: int):
    specific_names = []
    for name in names:
        if len(name) == length:
            specific_names.append(name)
            print(name.name)
    
    return specific_names

def find_names_with_length_up_to(names, max_length:int):
    specific_names = []
    for name in names:
        if len(name) <= max_length:
            specific_names.append(name)
            print(name.name)
    
    return specific_names

def find_names_with_specific_marker(names, marker: str):
    specific_names = []
    for name in names:
        if name.marker == marker:
            specific_names.append(name)
            print(name.name)
    
    return specific_names

def save_names(names, file_name:str):
    textfile = open(f"{file_name}.csv", "w")
    for name in names:
        textfile.write(f'{name.name};{name.marker}\n')

names = get_names('names.csv')

names_with_only_one_vowel = find_names_with_specific_number_of_vowels(names, 1)

save_names(names_with_only_one_vowel, "names_with_only_1_vowel")
