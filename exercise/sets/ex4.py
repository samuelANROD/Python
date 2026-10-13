convidados_1 = {'fulano_01', 'fulano_02', 'fulano_03', 'fulano_04'}
convidados_2 = {'fulano_01', 'fulano_02', 'fulano_04', 'fulano_05'}

#quem esta nas duas
print(convidados_1.intersection(convidados_2))
#print(convidados_1 & convidados_2) tambem funciona

#só no set 1
print(convidados_1.difference(convidados_2))

#só no set 2
print(convidados_2.difference(convidados_1))