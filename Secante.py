import matplotlib.pyplot as plt
import numpy as np

def f(x):
  f = eval(function)
  return f

print('''
#########################################################
#########################################################
####                                                 ####
####               Método de Secante                 ####
####        Por: Jesús Alfredo Navarro Guzmán        ####
####     https://github.com/JesusAlfred/MetodosNum   ####
####     navarro.jesusalfredo@gmail.com              ####
####                   18/10/2021                    ####
####                Métodos Numéricos                ####
####                                                 ####
#########################################################
#########################################################
''')

print("f(x) =", end=' ')
function = str(input())

print("límiete a =", end=' ')
a = int(input())
print("límiete b =", end=' ')
b = int(input())

print("Xn =", end=' ')
X0 = int(input())
print("Xn+1 =", end=' ')
X1 = int(input())

print("iteraciones =", end=' ')
lim = int(input())

print("decimales =", end=' ')
dec = int(input())

print("n\t Xn\t Xn+1\t f(Xn)\t f(Xn+1)\t Xn+1 - Xn\t B=f(Xn+1)-f(Xn)\t A=f(Xn+1)*(Xn+1-Xn)\t C=A/B\t Xn+2=Xn+1-C")
for i in range(lim):
    
    print(f"{i+1}\t|{round(X0, dec)}\t|{round(X1,dec)}\t|{round(f(X0), dec)}\t|{round(f(X1), dec)}\t\t|{round(X1-X0, dec)}\t\t|{round(f(X1)-f(X0), dec)}\t\t\t|{round(f(X1)*(X1-X0), dec)}\t\t\t|{round((f(X1)*(X1-X0))/(f(X1)-f(X0)), dec)}\t|{X1-((f(X1)*(X1-X0))/(f(X1)-f(X0)))}")
    temp = X1-((f(X1)*(X1-X0))/(f(X1)-f(X0)))
    X0=X1
    X1 = temp
# Muestra la grafica
fun = np.arange(X1-10, X1+10, 0.05)
plt.plot(fun, f(fun))
plt.grid()
texto1 = plt.text(X1, f(X1)+1, f'( {X1:.{dec}f}, {f(X1):.4f} )', fontsize=14)
plt.plot([X1], [f(X1)], 'bo')
plt.show()