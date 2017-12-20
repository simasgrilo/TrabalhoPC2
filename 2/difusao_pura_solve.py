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
from itertools import cycle
import numpy as np, matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Calculator:
    def careless_whispers(QDT_TIME = 10, C = 2.0, dx = 0.1, dt = 0.001):
        fou = open('difusao1d-exp.potato','wt')

        L_BOUND = 0.
        U_BOUND = 1.
        LEGEND_PATCHES = []        
        
        color = cycle('bgrcmy')

        X_AXIS = np.arange(L_BOUND,U_BOUND+dx,dx)

        print('#dx=%9.4f'% dx)

        print('#dy=%9.4f'% dt)


        nx = int(round(1.0/dx,0))     # número de pontos em x
        nt = int(round(1.0/dt,0))     # número de pontos em t
        
        time_interval = int(nt/QDT_TIME)

        print('#nx=%9d'% nx)
        print('#nt=%9d'% nt)

        u = np.zeros((2,nx+1),float)     # apenas 2 posições no tempo # são necessárias!

        def CI(x):                    # define a condição inicial (u(x,0))
            if(0 <= x <= 1.0):
                return 2.0*x*(1.0-x)
            else:
                return 0.0
            
        for i in range(nx+1):         # monta a condição inicial
            xi = i*dx
            u[0,i] = CI(xi)

        u[0].tofile(fou)              # imprime a condição inicial
        #fou.write(u[0])
        print(u[0])
        print(u[0].shape, X_AXIS.shape)
        plt.plot(X_AXIS, u[0], 'ko')
        LEGEND_PATCHES.append(mpatches.Patch(color='black', label="CI"))
        plt.title("Difusão Pura")
        plt.ylabel('u(x,t)')
        plt.xlabel('x')
        old = 0 #isso pode estar bugando... (old era = False e new = True)
        new = 1
        psi = C*dt/((dx)**2)            # psi
        print("c*Deltat/Deltax %10.6f" % psi)

        ten2ten = 0
        for n in range(nt):          # loop no tempo
            #print(n)		      #número de espaços de tempo avaliados
            for i in range(1,nx):     # loop no espaço
                u[new,i] = u[old,i] + psi*(u[old,i+1] - 2*u[old,i] + u[old,i-1]) #uk+1 i = uk i + psi* (uk i+1 -2uk i + uk i-1)
            u[new,0] = 0.0            # condição de contorno, x = 0
            u[new,nx] = 0.0           # condição de contorno, x = 1
            u[new].tofile(fou)        # imprime uma linha com os novos dados
            if(ten2ten%time_interval == 0):
                print(u[new])
                c = next(color)
                plt.plot(X_AXIS, u[new], c+'-')
                LEGEND_PATCHES.append(mpatches.Patch(color=c, label="t = " + str(round(n*dt, 2))))
            ten2ten += 1
            (old,new) = (new,old)     # troca os índices
        

        #from numpy import fromfile

        #u = fromfile(fou,float,nx+1)  # lê a condição inicial
        #fou.close()
        #v = [u]                       # inicializa a lista da "transposta"
        #for it in range(nx):           # para <m> instantes:
        #   for ir in range(nt):        # lê <ir> vezes, só guarda a última
        #        u = fromfile(fou,float,nx+1)
        #        v.append(u)                # guarda a última. originalmente esse v tava fora do for mais interno, mas não funciona.
        #founam ='divisao1d-exp.txt'
        #out = open(founam,'wt')       # abre o arquivo de saída
     #print(v[1][0])
     #print(len(v[1]))


        #for i in range(nx+1): #xi
        #   out.write('%10.6f'% (i*dx))    # escreve o "xi"
        #   out.write('%10.6f'% v[0][i])   # escreve a cond inicial
        #fou.write("aaa" + str( i))
        #   for k in range(1,m+2): #tempo
               #print(k)
               #print(i)
               #print(v[k][i])
        #       out.write('%10.6f'% v[k][i])# escreve o k-ésimo
        #   out.write('\n')
        #out.close()

        
        plt.legend(handles=LEGEND_PATCHES)
        plt.show()
    
#careless_whispers()
