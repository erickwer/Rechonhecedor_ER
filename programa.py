import json
import re
with open('bd.json') as json_data:
   bancoProdutos = json.load(json_data)

with open('bdAcoes.json') as json_data:
   bancoAcoes = json.load(json_data)

string1=''
string2=''
for i in bancoAcoes['acoes']:
   string1+=i+"|"
lista_prod= []
for i in bancoProdutos['produtos']:
   string2+=i['nome']+"|"
   lista_prod.append( i['nome']+':'+i['preco'])





padrao_nome = re.compile(r"[A-Z][a-z]*")
padrao_acao =  re.compile(r"{0}".format(string1[:-1]))
ref = open('texto.txt', 'r')



padrao_produto = re.compile(r"{0}".format(string2[:-1]))
compra_note = 0
compra_desktop =0
compra_carro=0
compra_moto=0
compra_livro=0
compra_celular=0
dic ={}
for linha in ref:
   acao = re.findall(padrao_acao,linha)
   produto = re.findall(padrao_produto,linha)
   while acao.__contains__('comprar') or acao.__contains__('adquirir'):
        if produto.__contains__('notebook'):
            compra_note+=1
        elif produto.__contains__('desktop'):
            compra_desktop+=1
        elif produto.__contains__('carro'):
            compra_carro+=1
        elif produto.__contains__('moto'):
            compra_moto=+1
        elif produto.__contains__('livro'):
            compra_livro+=1
        elif produto.__contains__('celular'):
            compra_celular+=1
        break

    
total = 0
def saber_preco(produto):
    for i in lista_prod:
        preco = i.split(':')
        if preco[0]== produto:
            return int(preco[1])
       
dic['notebook']= compra_note
notebook = saber_preco('notebook')*int(dic['notebook'])
dic['desktop']=compra_desktop
desktop = saber_preco('desktop')*int(dic['desktop'])
dic['carro']=compra_carro
carro = saber_preco('carro')*int(dic['carro'])
dic['moto']=compra_moto
moto = saber_preco('moto')*int(dic['moto'])
dic['livro']=compra_livro
livro = saber_preco('livro')*int(dic['livro'])
dic['celular']=compra_celular
celular = saber_preco('celular')*int(dic['celular'])
print("Preço total de Notebooks vendidos: "+ str(notebook)+"\nPreço total de Desktops vendidos: "+ str(desktop)+"\nPreço total dos Carros vendidos: "+ str(carro)+"\nPreço total das Motos vendidas: "+ str(moto)+"\nPreço total dos Livros vendidos: "+ str(livro)+"\nPreço total dos Celulares vendidos: "+str(celular)+"\n Total Arecadado: "+str(notebook+celular+carro+moto+livro+desktop))
