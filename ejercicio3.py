h = int(input('introduzca las horas  '))
m = int(input('introduzca los minutos   '))
s = int(input('introduzca los segundos  '))
if(s>=0 and s<=58):
    print('horas {} - minutos {} - segundos {}'.format(h,m,s+1))
elif(s==59) and  (m == 59):
    print('horas {} - minutos {} - segundos {}'.format(h+1,0,0))
elif(s == 59):
    print('horas {} - minutos {} - segundos {}'.format(h,m+1,0))
else:
    print('Error en la entradad de datos')