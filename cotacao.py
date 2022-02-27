import requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_bitcoin = cotacoes['BTCBRL']['bid']
print('A cotação do Dolar hoje é R$ {}' .format(cotacao_dolar))
print('A cotação do Euro hoje é R$ {}' .format(cotacao_euro))
print('A cotação do Bitcoin hoje é R$ {}' .format(cotacao_bitcoin))




