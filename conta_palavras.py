import string

texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Massa sapien faucibus et molestie. Urna nec tincidunt praesent semper feugiat. A diam maecenas sed enim ut. Quis eleifend quam adipiscing vitae. Mauris pellentesque pulvinar pellentesque habitant morbi tristique senectus et. Lectus urna duis convallis convallis tellus. Accumsan sit amet nulla facilisi morbi tempus. Sagittis id consectetur purus ut faucibus pulvinar. Faucibus turpis in eu mi bibendum neque egestas. Eget arcu dictum varius duis at. Nisl suscipit adipiscing bibendum est. Sagittis vitae et leo duis ut diam. Felis imperdiet proin fermentum leo. Mattis rhoncus urna neque viverra. Duis tristique sollicitudin nibh sit amet commodo nulla facilisi. Quis lectus nulla at volutpat.

Arcu risus quis varius quam quisque id diam vel. Pretium lectus quam id leo in vitae turpis. Mattis aliquam faucibus purus in massa tempor. Arcu cursus euismod quis viverra nibh cras pulvinar mattis. Porttitor leo a diam sollicitudin tempor id eu nisl nunc. Egestas maecenas pharetra convallis posuere morbi leo urna molestie. Elementum curabitur vitae nunc sed velit dignissim sodales ut. Malesuada pellentesque elit eget gravida cum sociis. Consequat mauris nunc congue nisi vitae suscipit tellus mauris a. Vel elit scelerisque mauris pellentesque pulvinar pellentesque habitant morbi tristique.'''

novo_texto = ''

for caracter in texto:
	if caracter not in string.punctuation + '\n':
		novo_texto += caracter

# print(novo_texto)

texto_sep = novo_texto.split(' ')

dici_palavras = {}

for palavra in texto_sep:
	if palavra not in dici_palavras:
		dici_palavras[palavra] = 1
	else:
		dici_palavras[palavra] += 1

print(dici_palavras)


# texto_sep = texto.split(' ')

# print(texto_sep)

# dici_palavras = {}

# for palavra in texto_sep:
# 	if palavra not in dici_palavras:
# 		dici_palavras[palavra] = 1
# 	else:
# 		dici_palavras[palavra] += 1


# print(dici_palavras)