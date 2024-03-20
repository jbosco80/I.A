import funcoes_auxiliares as fa
import busca_sem_pesos_FATEC as bs
from sys import exit

sol = bs.busca()
caminho = []

# Busca em Grade de Ocupação
mapa = fa.Gera_Problema_Grade("mapa.txt")
dim_x = len(mapa)
dim_y = len(mapa[0])
origem  = [0,0]
destino = [4,2]
print(mapa)
print(dim_x,dim_y)

if origem[0]<0  or origem[0]>dim_x-1  or origem[1]<0  or origem[1]>dim_y-1  or destino[0]<0 or destino[0]>dim_x-1 or origem[1]<0  or origem[1]>dim_y-1:
       print("Coordenada Inválida")
       exit()
"""
# Busca em Grafo
nos, grafo = fa.Gera_Problema_Grafo("romenia.txt")

origem  = input("Origem..: ").upper()
destino = input("Destino.: ").upper()

if origem not in nos or destino not in nos:
    print("Cidade não está na lista")
    exit()
"""
#caminho = sol.amplitude(origem,destino,nos,grafo)
caminho = sol.amplitude(origem,destino,mapa,dim_x,dim_y)
print("\n===> AMPLITUDE:",caminho)
print("===> Custo do Caminho:",len(caminho)-1)


#caminho = sol.profundidade(origem,destino,nos,grafo)
caminho = sol.profundidade(origem,destino,mapa,dim_x,dim_y)
print("\n*****PROFUNDIDADE*****\n",caminho)    
print("===> Custo do Caminho:",len(caminho)-1)

"""
limite = 2
caminho = sol.prof_limitada(origem,destino,nos,grafo,limite)
# caminho = sol.prof_limitada(origem,destino,mapa,dim_x,dim_y,limite)
print("\n***** PROFUNDIDADE LIMITADA ( L =",limite,")*****\n",caminho)
if caminho[0]!="caminho não encontrado":
    print("===> Custo do Caminho:",len(caminho)-1)

limite = 3
caminho = sol.prof_limitada(origem,destino,nos,grafo,limite)
# caminho = sol.prof_limitada(origem,destino,mapa,dim_x,dim_y,limite)
print("\n***** PROFUNDIDADE LIMITADA ( L =",limite,")*****\n",caminho)
if caminho[0]!="caminho não encontrado":
    print("===> Custo do Caminho:",len(caminho)-1)

limite = 4
caminho = sol.prof_limitada(origem,destino,nos,grafo,limite)
# caminho = sol.prof_limitada(origem,destino,mapa,dim_x,dim_y,limite)
print("\n***** PROFUNDIDADE LIMITADA ( L =",limite,")*****\n",caminho)
if caminho[0]!="caminho não encontrado":
    print("===> Custo do Caminho:",len(caminho)-1)

lim_max = len(nos)
caminho, limite = sol.aprof_iterativo(origem,destino,nos,grafo,lim_max)
# caminho = sol.prof_limitada(origem,destino,mapa,dim_x,dim_y,lim_max)
print("\n*****APROFUNDAMENTO ITERATIVO ( L =",limite,")*****\n",caminho)
print("===> Custo do Caminho:",len(caminho)-1)

caminho = sol.bidirecional(origem,destino)
print("\n*****BIDIRECIONAL*****\n",caminho)
"""
