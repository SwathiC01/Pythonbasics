import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus
from typing_extensions import TypedDict

def get_websites(path: str) -> list[str]:
    websites: list = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
        return websites
    
print(get_websites('websites.csv'))