from __future__ import print_function
from __future__ import division
from sys import argv

#esse programa permite selecionar apenas alguns pontos que foram solucionados para ver o valor em tais pontos
#uso: show.py <m> <n>, onde m é a quantidade de pontos (em x) que são escolhidos e a 

dx = 0.1
dt = 0.001

print('#dx=%9.4f'% dx)
print('#dt=%9.4f'% dt)

nx = int(round(1.0/dx,0))     # número de pontos em x
nt = int(round(1.0/dt,0))     # número de pontos em t
print('#nx=%9d'% nx)

m = nx #int(argv[1])              # m saídas
n = nt #int(argv[2])              # a cada n intervalos de  tempo

print('#m=%9d'% m)
print('#n=%9d'% n)

fin = open('difusao1d-exp.potato','rt')                # abre o arquivo com os dados

from numpy import fromfile

u = fromfile(fin,float,nx+1)  # lê a condição inicial
v = [u]                       # inicializa a lista da "transposta"
for it in range(m):           # para <m> instantes:
    for ir in range(n):        # lê <ir> vezes, só guarda a última
        u = fromfile(fin,float,nx+1)
    	v.append(u)                # guarda a última. originalmente esse v tava fora do for mais interno, mas não funciona.


founam ='divisao1d-exp.potato'
fou = open(founam,'wt')       # abre o arquivo de saída
#print(v[1][0])
#print(len(v[1]))


for i in range(nx+1): #xi
    fou.write('%10.6f'% (i*dx))    # escreve o "xi"
    fou.write('%10.6f'% v[0][i])   # escreve a cond inicial
    #fou.write("aaa" + str( i))
    for k in range(1,m+2): #tempo
        #print(k)
        #print(i)
        #print(v[k][i])
        fou.write('%10.6f'% v[k][i])# escreve o k-ésimo
    fou.write('\n')
fou.close()
