from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import string

names = []

def generate_links(prefix):
    letters = string.ascii_uppercase
    links = []
    for letter in letters:
        links.append(f'http://www.navnebetydning.dk/{prefix}/{letter}.shtml')    
    
    return links


def extract_names(link):
    driver = webdriver.Chrome()
    driver.get(link)
    elements = driver.find_elements_by_tag_name('a')
    
    for element in elements:
        link = element.get_attribute('href')
        name = element.text
        marker = ''
        
        if 'pigenavn' in link:
            marker = 'a'
        
        if 'drengenavn' in link:
            marker = 'b'

        if marker != '' and ((name, 'a') not in names and (name, 'b') not in names):
            names.append((name, marker))
            print(f'Added name: {name} : {marker}')

    driver.close()
    return names


def save_list(names):
    textfile = open("names.csv", "w")
    for element in names:
        textfile.write(f'{element[0]};{element[1]}\n')


links = generate_links("pigenavne")
links += generate_links("drengenavne")

for link in links:
    print(f'Extracting from link: {link}')
    extract_names(link)

save_list(names)

print('Done')
