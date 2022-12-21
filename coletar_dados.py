
# Importar bibliotecas necessárias
import requests
from bs4 import BeautifulSoup
import csv

# Definir a URL da página do OLX
url = "https://www.olx.com.br/imoveis/aluguel/apartamentos/sao-paulo-e-regiao/sao-paulo/?f=p&o=1"

# Enviar uma requisição para a página do OLX
r = requests.get(url)

# Obter o conteúdo da página
conteudo = r.text

# Criar um objeto BeautifulSoup para análise do conteúdo
soup = BeautifulSoup(conteudo, "html.parser")

# Encontrar todos os anúncios na página
anuncios = soup.find_all("li", {"class": "sc-1fcmfeb-2 gXUycw"})

# Criar um arquivo CSV para armazenar os dados
with open("dados_olx.csv", "w", newline="") as arquivo:
    # Criar o objeto de escrita do CSV
    escritor = csv.writer(arquivo)

    # Escrever os títulos das colunas no arquivo CSV
    escritor.writerow(["Título", "Preço", "Link"])

    # Percorrer cada anúncio e escrever os dados no arquivo CSV
    for anuncio in anuncios:
        # Obter o título e o link do anúncio
        titulo = anuncio.find("span", {"class": "sc-16ede01-2 hTtTcT"}).text
        link = anuncio.find("a")["href"]

        # Obter o preço do anúncio
        preco = anuncio.find("p", {"class": "sc-16ede01-5 hDxhSP"}).text
        preco = preco.strip().replace("R$", "").replace(".", "").replace(",", ".")

        # Escrever os dados do anúncio no arquivo CSV
        escritor.writerow([título, preco, link])
