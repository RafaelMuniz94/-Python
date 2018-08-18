import urllib.request
import time

#print(urllib.request.urlopen('https://www.google.com').read())

def craw():
    urlDolar = 'https://www.melhorcambio.com/cotacao/compra/dolar-turismo/sao-paulo'
    urlEuro = 'https://www.melhorcambio.com/cotacao/compra/euro/sao-paulo'
    climaTempo = 'https://www.climatempo.com.br/'
    googleTempo = 'https://www.google.com.br/search?q=google+tempo&oq=google+tempo&aqs=chrome.0.0l6.2679j0j7&sourceid=chrome&ie=UTF-8'

    conteudoDolar = str(urllib.request.urlopen(urlDolar).read())
    conteudoEuro = str(urllib.request.urlopen(urlEuro).read())
    conteudoClimaTempo = str(urllib.request.urlopen(climaTempo).read())
    #conteudoGoogleTempo = str(urllib.request.urlopen(googleTempo).read())

    buscaDolarEuro  = '<span itemprop="price" content="'
    buscaClimaTempo = '<h3 id="momento-temperatura">'
    #buscaGoogleClima = '<span class="wob_t" id="wob_tm" style="">'

    posicaoDolar = int(conteudoDolar.index(buscaDolarEuro) + len(buscaDolarEuro))
    dolar = conteudoDolar[posicaoDolar: posicaoDolar + 4]

    print(dolar)

    posicaoEuro = int(conteudoEuro.index(buscaDolarEuro) + len(buscaDolarEuro))
    euro  = conteudoEuro[posicaoEuro: posicaoEuro + 4]

    print(euro)

    posicaoClimaTempo = int(conteudoClimaTempo.index(buscaClimaTempo))
    climaTempo  = conteudoClimaTempo[posicaoClimaTempo : posicaoClimaTempo  + len(buscaClimaTempo)+10]

    print(climaTempo)

    #posicaoGoogleTempo = int(conteudoGoogleTempo.index(buscaGoogleTempo) + len(buscaGoogleTempo))
    #googleTempo = conteudoGoogleTempo[posicaoGoogleTempo: posicaoGoogleTempo + 2]    
   
    
   # print(googleTempo)

craw()
