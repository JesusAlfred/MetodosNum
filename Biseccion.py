import matplotlib.pyplot as plt
import numpy as np

def f(x):
  f = eval(function)
  return f

print('''
#########################################################
#########################################################
####                                                 ####
####               Método de Bisección               ####
####        Por: Jesús Alfredo Navarro Guzmán        ####
####     https://github.com/JesusAlfred/MetodosNum   ####
####     navarro.jesusalfredo@gmail.com              ####
####                   21/09/2021                    ####
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

print("iteraciones =", end=' ')
lim = int(input())

print("decimales =", end=' ')
dec = int(input())

fun = np.arange(a, b, 0.05)
if ((f(a) * f(b)) < 0):
  print("n\t An\t Bn\t Xn\t f(Xn)\t f(An)")
  for i in range(lim):
      m = round((a+b)/2, dec)
      #print("n: ", i + 1, "\tf(", m, ") = ", round(f(m), dec), sep='')
      print(f"{i+1}\t|{a}\t|{b}\t|{m}\t|{round(f(m), dec)}\t|{round(f(a), dec)}\t|{f'- (B(n+1)={m})' if (f(m) * f(a)) < 0 else f'+ (A(n+1)={m})'}")
      if (round(f(m), dec)==0):
        print("La raíz está en x =", m)
        break
      else:
        if (f(m) * f(a) < 0):
          b = m
        else:
          a = m
# Muestra la grafica
  plt.plot(fun, f(fun))
  plt.grid()
  texto1 = plt.text(m, f(m)+1, f'( {m:.{dec}f}, {f(m):.4f} )', fontsize=14)
  plt.plot([m], [f(m)], 'bo')
  plt.show()
else:
  print(f"No existe raíz en el rango [{a} ,{b}]")