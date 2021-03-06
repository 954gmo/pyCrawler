# -*- encoding:utf-8 -*-
import os
from pathlib import Path
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    file = os.path.join(Path(__file__).parent, 'pge_meter_details.html')
    with open(file, 'r', encoding='utf8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        service_addr = soup.find('div', {'class': 'module-body sa-info'}).find('ul').find_all('li')[:2]
        service_addr = re.sub(r'\s+', ' ', service_addr[0].string) + "," + re.sub(r'\s+', ' ', service_addr[1].string)
        rate_name = soup.find('div', {'class': 'module module-grad my-rate-plan'}).find('h3').string
        rate_name = re.sub(r'\s+', ' ', rate_name)
        print(f'service address: {service_addr}')
        print(f'rate name: {rate_name}')
