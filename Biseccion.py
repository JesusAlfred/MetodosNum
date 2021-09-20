import matplotlib.pyplot as plt
import numpy as np

def f(x):
  f = eval(function)
  return f

print("f(x) =", end=' ')
function = str(input())

print("límiete a =", end=' ')
a = int(input())
print("límiete b =", end=' ')
b = int(input())

print("iteraciones =", end=' ')
lim = int(input())

fun = np.arange(a, b, 0.05)
if ((f(a) * f(b)) < 0):
  for i in range(lim):
      m = (a+b)/2
      print("f(", m, ") = ",f(m), sep='')
      if (f(m)==0):
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
  texto1 = plt.text(m, f(m)+1, f'( {m:.4f}, {f(m):.4f} )', fontsize=14)
  plt.plot([m], [f(m)], 'bo')
  plt.show()
else:
  print(f"No existe raíz en el rango [{a} ,{b}]")