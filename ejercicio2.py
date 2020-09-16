a = int(input("Introduzca el coeficiente a  "))
b = int(input("Introduzca el coeficiente b  "))
c = int(input("Introduzca la constante  "))
X = (b*b) -4*a*c
if (X>0):
    print('Las raices son reales y distintas')
elif(X==0):
    print('Las raices son reales e iguales')
else:
    print('Las raices son complejas o conjugadas')
    