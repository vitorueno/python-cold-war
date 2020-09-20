# import requests
# import json

# r = requests.get('http://localhost:3333/missions/1')

# print(r.json()['title'])

frase = 'alalalalalalalalalalalalalalalalalalalalalalalalalalal'

n = 20

chunks = [frase[i:i+n] for i in range(0, len(frase), n)]


# print(chunks)

# nova_frase = ''
# for chunk in chunks:
#     nova_frase += chunk + '\n' 
    
# print(nova_frase)