from yfinance import Ticker
from send_email import send_email

ticker = 'petr4.sa' #input('Informe o código da ação desejada: ')
dados = Ticker(ticker)

tabela = dados.history('6mo')

fechamento = tabela.Close

maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

print(send_email('email@gmail.com', 'análise de cotação', ticker, maxima, minima, atual))