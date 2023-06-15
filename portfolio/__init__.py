import os
from threading import Thread
from time import sleep

from bs4 import BeautifulSoup
import requests

from matplotlib import pyplot as plot


def scrape():
    sleep(5)

    from .models import PrevisaoMetereologica

    while True:
        scraper = BeautifulSoup(requests.get('https://www.tempo.pt/lisboa.htm').text, features='html.parser')

        temp_min = [t.text[:-1] for t in scraper.find_all(class_='minima')[:7]]
        temp_max = [t.text[:-1] for t in scraper.find_all(class_='maxima')[:7]]

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

        labels = [str(n) for n in range(1, len(temps) + 1)]

        plot.plot(labels, temp_min)
        plot.plot(labels, temp_max)

        dirname = os.path.dirname(__file__)
        plot.savefig(os.path.join(dirname, '../static/portfolio/img/tempo.png'))

        sleep(3600)


Thread(target=scrape, daemon=True).start()
