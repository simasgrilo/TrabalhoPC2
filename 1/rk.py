import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

'''
Implementação do método de Runge Kutta até ordem 4 para resolução do 'Forced Van der Pol oscillator':

Grupo:
Erick Simas
Max Fratane
Vítor Lourenço
Vitor Araujo

ref:
[1] https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods
[2] https://en.wikipedia.org/wiki/Van_der_Pol_oscillator
[3] http://mathworld.wolfram.com/vanderPolEquation.html
[4] http://www.cs.cornell.edu/~bindel/class/cs3220-s12/notes/lec26.pdf
[5] http://hadron.physics.fsu.edu/~eugenio/comphy/python/vanderpol.py
'''

class Runge_Kutta:

    def solver(order, l_bound, u_bound, p, r, f, *args):
        '''
        f = function; n = upper bound; p = partition
        '''
        h = (u_bound - l_bound) / p
        t_points = np.arange(l_bound, u_bound, h)
        if(str(order) == '1'):
            return Runge_Kutta.__rk1__(r, t_points, h, f, *args)
        elif(str(order) == '2'):
            return Runge_Kutta.__rk2__(r, t_points, h, f, *args)
        elif(str(order) == '3'):
            return Runge_Kutta.__rk3__(r, t_points, h, f, *args)
        else:
            return Runge_Kutta.__rk4__(r, t_points, h, f, *args)

    def __rk1__(r, t_points, h, f, *args):
        x_points = np.array([])
        v_points = np.array([])
        for t in t_points:
            x_points = np.append(x_points, r[0])
            v_points = np.append(v_points, r[1])
            k1 = h * f(r, t, *args)

            r = r + k1

        return t_points, x_points, v_points

    def __rk2__(r, t_points, h, f, *args):
        x_points = np.array([])
        v_points = np.array([])
        for t in t_points:
            x_points = np.append(x_points, r[0])
            v_points = np.append(v_points, r[1])
            k1 = h * f(r, t, *args)
            k2 = h * f(r + 0.5 * k1, t + 0.5 * h, *args)

            r = r + k2

        return t_points, x_points, v_points

    def __rk3__(r, t_points, h, f, *args):
        x_points = np.array([])
        v_points = np.array([])
        for t in t_points:
            x_points = np.append(x_points, r[0])
            v_points = np.append(v_points, r[1])
            k1 = h * f(r, t, *args)
            k2 = h * f(r + 0.5 * k1, t + 0.5 * h, *args)
            k3 = h * f(r + 0.5 * k2, t + 0.5 * h, *args)

            r = r + (k1 + 4 * k2 + k3) / 6

        return t_points, x_points, v_points

    def __rk4__(r, t_points, h, f, *args):
        x_points = np.array([])
        v_points = np.array([])
        for t in t_points:
            x_points = np.append(x_points, r[0])
            v_points = np.append(v_points, r[1])
            k1 = h * f(r, t, *args)
            k2 = h * f(r + 0.5 * k1, t + 0.5 * h, *args)
            k3 = h * f(r + 0.5 * k2, t + 0.5 * h, *args)
            k4 = h * f(r + k3, t + h, *args)

            r = r + (k1 + 2 * k2 + 2 * k3 + k4) / 6

        return t_points, x_points, v_points

class Calculator:

    def calculate(orders, partition, t_variation, initial_condition, mu, amplitude, omega):
        results = []
        t_min, t_max = t_variation[0], t_variation[1]
        x0, v0 = initial_condition[0], initial_condition[1]
        r = np.array([x0, v0])
        for order in orders:
            rk = Runge_Kutta.solver(order, t_min, t_max, partition, r, \
            Calculator.__vdp_osccilation__, mu, amplitude, omega)
            results.append(rk)
            #out = open("results-rk-order"+str(order)+".txt",'wt')
            #out.write("Condição Inicial em x")
            #for i in len(x0):
            #    out.write("x" + str(i) + x0[i])
            #out.close()		
                
       # print(len(results))
        Calculator.__plot__(len(results), *results)

    def __plot__(qtd, *args):
        '''
        args[i][0] = t_points; args[i][1] = x_points; args[i][2] = v_points
        '''
        color = {1: 'red', 2: 'blue', 3: 'green', 4: 'yellow', 5: 'black'}
        patches = []
        t_min = x_min = v_min = np.inf
        t_max = x_max = v_max = -np.inf
        try:
            ptl.close(1)
            ptl.close(2)
        except:
            pass
        for i in range(qtd):

            t_min = min(np.amin(args[i][0]), t_min)
            t_max = max(np.amax(args[i][0]), t_max)

            x_min = min(np.amin(args[i][1]), x_min)
            x_max = max(np.amax(args[i][1]), x_max)

            v_min = min(np.amin(args[i][2]), v_min)
            v_max = max(np.amax(args[i][2]), v_max)
            #existe um bug na linha abaixo:
            patches.append(mpatches.Patch(color=color[i + 1], label= 'Runge-Kutta de ' + str(i+1) + 'ª ordem' ))
            
            # plot displacement vs time
            plt.figure(1)
            plt.plot(args[i][0], args[i][1], color[i + 1])

            # plot the phase space
            plt.figure(2)
            plt.plot(args[i][1], args[i][2], color[i + 1])

        plt.figure(1)
        plt.legend(handles=patches)
        plt.xlabel("t")
        plt.ylabel("x")
        plt.title("Oscilação de Van der Pol")
        plt.axis([t_min, t_max, x_min, x_max])

        plt.figure(2)
        plt.legend(handles=patches)
        plt.xlabel("x")
        plt.ylabel("dx/dt")
        plt.title("Fase de Espaço da Oscilação de Van der Pol")
        plt.axis([x_min, x_max, v_min, v_max])

        plt.show()

    def __vdp_osccilation__(r, t, mu, A, omega):
        '''
            x'' - mu * (1 - x²) * x' - A * sin(omega * t)
            mu = 0: x(t) = x(0) * cos(t) + x'(0) * sin(t)
        '''
        x = r[0]
        v = r[1]
        fx = v
        fv = -x  +  mu*(1 - x ** 2) * v - A * np.sin(omega * t)
        return np.array([fx,fv])
