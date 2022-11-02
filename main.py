from bs4 import BeautifulSoup as bs
import re
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
import time

from Livro import Livro

# navegador = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
navegador = webdriver.Chrome(r"C:\Users\PC\Documents\chromedriver.exe")

dic_livros = [];
count = 0

def navegadorScroll(url):
    navegador.get(url)
    navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    last_height = navegador.execute_script('return document.body.scrollHeight')
    for contador in range(5):
        navegador.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        new_height = navegador.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

for i in range(1, 3):
    url_pag = f'https://www.amazon.com.br/gp/bestsellers/books/ref=zg_bs_pg_{i}?ie=UTF8&pg={i}'
    navegadorScroll(url_pag)
    soup = bs(navegador.page_source, 'html.parser')
    produtos = soup.find_all('div', id=re.compile("p13n-asin-index"))

    for produto in produtos:
        count = count + 1
        divsObraAutor = produto.find_all(class_="_cDEzb_p13n-sc-css-line-clamp-2_EWgCb") + produto.find_all(
            class_="_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y")

        Obra = divsObraAutor[0].getText()
        Autor = divsObraAutor[1].getText()
        Preco = produto.find('span', class_="_cDEzb_p13n-sc-price_3mJ9Z").getText()

        Star = ''
        if (produto.find('i', class_="a-icon a-icon-star-small a-star-small-4-5 aok-align-top")):
            Star = produto\
                .find('i', class_="a-icon a-icon-star-small a-star-small-4-5 aok-align-top")\
                .find('span', class_="a-icon-alt").getText()
        elif (produto.find('i', class_="a-icon a-icon-star-small a-star-small-5 aok-align-top")):
            Star = produto\
                .find('i', class_="a-icon a-icon-star-small a-star-small-5 aok-align-top")\
                .find('span', class_="a-icon-alt").getText()

        livro = Livro(count, Obra, Autor, Star, Preco)
        dic_livros.append(livro)

for livro in dic_livros:
    print(livro)

navegador.close()
