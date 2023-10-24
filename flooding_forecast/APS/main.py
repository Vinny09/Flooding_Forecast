from kivy.app import App
from kivy.lang import Builder
import requests

gui = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return gui
    # Função para sempre inicializar com cotação das moedas automaticamente
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"
    # Função para pegar a cotação das moedas utilizando request
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


MeuAplicativo().run()