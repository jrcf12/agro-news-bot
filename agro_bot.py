import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

# Credenciais do Twilio
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH")
twilio_number = 'whatsapp:+14155238886'
my_number = os.getenv("MY_WHATSAPP")

client = Client(account_sid, auth_token)

def buscar_noticias_agro():
    url = 'https://www.canalrural.com.br/'
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    noticias = soup.find_all('h3')[:3]

    mensagem = "📰 *Notícias do Agro - Rural Agrícola*\n\n"
    for noticia in noticias:
        titulo = noticia.text.strip()
        link_tag = noticia.find('a')
        link = link_tag['href'] if link_tag else "Link não encontrado"
        mensagem += f"• {titulo}\n👉 {link}\n\n"

    enviar_whatsapp(mensagem)

def enviar_whatsapp(texto):
    message = client.messages.create(
        from_=twilio_number,
        body=texto,
        to=my_number
    )
    print("✅ Mensagem enviada:", message.sid)

if __name__ == "__main__":
    buscar_noticias_agro()
