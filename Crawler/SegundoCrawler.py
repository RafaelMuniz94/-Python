from bs4 import BeautifulSoup
import requests
import webbrowser
import time

def BuscaTitulo(conteudo):
    soup = BeautifulSoup(conteudo,"lxml") # o lxml é o parser
    tag = soup.find("title",text=True) # procura desde que haja algum texto dentro da tag
    #Se não for nulo retorna o conteudo, sem espaço
    if not tag:
        return None
    return tag.string.strip() # strip é semelhante ao TRIM


def RetornaLinks(conteudo):
    soup = BeautifulSoup(conteudo,"lxml")
    links = set() # semelhante a um array, porém não permite duplicatas

    for tag in soup.find_all("a",href=True):
        if tag["href"].startswith("http"):
            links.add(tag["href"])

    return links


def crawl(url_inicial):
    urls_vistas = set([url_inicial])
    urls_disponiveis = set([url_inicial])

    while urls_disponiveis:
        time.sleep(5)
        url = urls_disponiveis.pop()

        try:
            content = requests.get(url, timeout=3).text
        except Exception:
            continue

        title = BuscaTitulo(content)

        if title:
            print(title," - ",url)
            print()

        for link in RetornaLinks(content):
            if link not in urls_vistas:
                urls_vistas.add(link)
                urls_disponiveis.add(link)


url = "https://forum.macmagazine.com.br/forum/36-classificados/"
pagina = requests.get(url)

title = BuscaTitulo(pagina.text)
links = RetornaLinks(pagina.text)

try:
    crawl(url)
except KeyboardInterrupt:
    print("Fim")

'''
print(title)
print("Foram encontrados: ",len(links)," resultados")
#time.sleep(2)
for l in links:
    print(l)

'''

