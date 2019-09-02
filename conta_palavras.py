import string

texto = ''

with open('alice.txt', 'r') as file:
	for linha in file:
		texto += linha



novo_texto = ''

for caracter in texto:
	if caracter not in string.punctuation + '\n':
		novo_texto += caracter

# print(novo_texto)




texto_sep = texto.split(' ')

print(texto_sep)

dici_palavras = {}

for palavra in texto_sep:
	if palavra not in dici_palavras:
		dici_palavras[palavra.lower()] = 1
	else:
		dici_palavras[palavra.lower()] += 1


print(dici_palavras)