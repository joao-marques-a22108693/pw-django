from threading import Thread
from time import sleep

from bs4 import BeautifulSoup
import requests


def scrape():
    sleep(1)

    from .models import PrevisaoMetereologica

    while True:
        scraper = BeautifulSoup(requests.get('https://www.tempo.pt/lisboa.htm').text, features='html.parser')

        temp_min = [t.text[:-1] for t in scraper.find_all(class_='minima')[:7]]
        temp_max = [t.text[:-1] for t in scraper.find_all(class_='maxima')[:7]]

        print(temp_min)
        print(temp_max)

        temps = list(zip(temp_min, temp_max))

        objs = PrevisaoMetereologica.objects.all()

        for temp in range(len(temps)):
            if len(objs) < temp + 1:
                p = PrevisaoMetereologica()
                p.temp_min = temps[temp][0]
                p.temp_max = temps[temp][1]
                p.save()
            else:
                objs[temp].temp_min = temps[temp][0]
                objs[temp].temp_max = temps[temp][0]
                objs[temp].save()

        sleep(3600)


# Thread(target=scrape).start()
