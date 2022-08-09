# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
import urllib.request

url = 'http://pudim.com.br'

try:
    site = urllib.request.urlopen(url)
except:
    print("Num deu")
else:
    print("Deu bom")
