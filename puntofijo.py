--------------------------------------------------------------------

# Implementación del método del punto fijo y algunos casos de salida.
from math import *
B.1. BÚSQUEDA DE RAÍCES 149

def pote(x):
 """Función de prueba"""
return pow(2, -x) # retorna pote(x) = 2−x

def pol(x):
 """Función de prueba"""
 return (x**2 - 1)/3 # retorna pol(x) = x2−1



 def puntofijo(f, p0, tol, n):

 Implementación método de punto fijo
 Entradas:
 f -- función
 p0 -- aproximación inicial
 tol -- tolerancia
 n -- número máximo de iteraciones

 Salida:
p aproximación a punto fijo de f
       None en caso de iteraciones agotadas
 """
  i = 1
  while i <= n:
 p = f(p0)
 print("Iter = {0:<2}, p = {1:.12f}".format(i, p))
 if abs(p - p0) < tol:
 return p
 p0 = p
 i += 1
 print("Iteraciones agotadas: Error!")
 return None

 # pol(x), p0 = 0.9, T OL = 10−8, N0 = 100
 print("Punto fijo función pol(x):")
 puntofijo(pol, 0.9, 1e-8, 100)

 # pote(x), p0 = 0.5, T OL = 10−8, N0 = 100
  print("Punto fijo función pote(x):")
