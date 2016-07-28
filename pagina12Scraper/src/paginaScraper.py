'''
Created on Jul 28, 2016

@author: lucas
'''

from lxml import html
from io import StringIO, BytesIO
from copy import deepcopy
import requests
import re
import pickle

BASE_URL = 'http://www.pagina12.com.ar'

def writeList(list):
        file = open("websScrapeadas.txt", "w")
        for element in list:
            file.write(element + '\n')
        file.close()


if __name__ == '__main__':    
    
    page = requests.get('http://www.pagina12.com.ar')
    
    try:    
        compiledRe = re.compile(r'href=[\'"]?([^\'">]+/20-\d{6}-\d{4}-\d{2}-\d{2}[^\'">]+)')
        # href que arranca así
        #contiene /20-
        # hasta que termina
        matches = compiledRe.findall(str(page.content))
        print(matches)
    except Exception as error:
        print(type(error))
        print(error)
    
    modifiedUrls = [(BASE_URL + url) for url in matches]
    print(modifiedUrls)
    
    pickle.dump(modifiedUrls, open("lista.p", "wb"))
    writeList(modifiedUrls)
    count = 0    
    for url in modifiedUrls:
        try:
            page = requests.get(url)
        except Exception as error:
            print(error)
            continue
        try:
            tree = html.fromstring(page.content)
        except Exception as error:
            print(error)
            continue
        nota = tree.xpath('//div[@id="cuerpo"]//p/text()')
        file = open(str(count)+".txt", "w")
        for parrafo in nota:
            file.write(parrafo)
        file.close()
        count +=1
    count +=1