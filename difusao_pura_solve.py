#resolve por um método explicito de diferenças finitas a segunte equação:
#du/dt = c * du/dx2 com u(0,t) = u(1,t) = 0 e u(x,0) = 2*x*(1-x)
#com os valores de delta x e delta t, temos que o sistema é instavel ( não estabiliza, pois c*dt/dx^2 = 2000
#um exemplo onde esse sistema converge écom c = 2, delta t = 0,00001 e delta x = 0,001 onde c*dt/dx^2 = 0.2 < 0.5
#nesse caso, uma execução leva cerca de 8 minutos, por avaliar os pontos em 100000 pontos em t diferentes
#os dados da resolução dos problemas são salvos e são lidos pelo show.py
#puxar o crack nicolson
#http://www.lemma.ufpr.br/wiki/images/c/c0/Ma-edp.pdf


from __future__ import print_function
from __future__ import division

fou = open('difusao1d-exp.potato','wt')

dx = 0.1
dt = 0.001

print('#dx=%9.4f'% dx)

print('#dy=%9.4f'% dt)

from numpy import zeros

nx = int(round(1.0/dx,0))     # número de pontos em x
nt = int(round(1.0/dt,0))     # número de pontos em t

print('#nx=%9d'% nx)
print('#nt=%9d'% nt)

u = zeros((2,nx+1),float)     # apenas 2 posições no tempo # são necessárias!

def CI(x):                    # define a condição inicial (u(x,0))
    if(0 <= x <= 1.0):
        return 2.0*x*(1.0-x)
    else:
        return 0.0
    
for i in range(nx+1):         # monta a condição inicial
    xi = i*dx
    u[0,i] = CI(xi)

u[0].tofile(fou)              # imprime a condição inicial
old = 0 #isso pode estar bugando... (old era = False e new = True)
new = 1
C = 2.0                      # constante c
psi = C*dt/((dx)**2)            # psi
print("c*Deltat/Deltax %10.6f" % psi)

for n in range(nt):          # loop no tempo
    #print(n)		      #número de espaços de tempo avaliados
    for i in range(1,nx):     # loop no espaço
        u[new,i] = u[new,i] = u[old,i] + psi*(u[old,i+1] - 2*u[old,i] + u[old,i-1]) #uk+1 i = uk i + psi* (uk i+1 -2uk i + uk i-1)
    u[new,0] = 0.0            # condição de contorno, x = 0
    u[new,nx] = 0.0           # condição de contorno, x = 1
    u[new].tofile(fou)        # imprime uma linha com os novos dados
    (old,new) = (new,old)     # troca os índices
fou.close()
