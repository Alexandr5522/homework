#dictionaries
my_dict = {'Alexandr':1990,'Julia':1993,'Demyan':2011,'Vsevolod':2012,'Denis':2014}
print(my_dict)
print(my_dict['Julia'])
print(my_dict.get('Maximm'))
my_dict.update({'Maxim':2002,'Claus':2019})
print(my_dict)
name = my_dict.pop('Maxim')
print(name)
del my_dict['Julia']
print(my_dict)
#sets
my_set = {1,2,3,1,4,2,3,5,6, (1,4,2,), '5,7,6'}
print(set(my_set))
my_set.update({'Alexandr:2000','Den'})
print(my_set)
my_set.add(1993)
my_set.discard('Alexandr:2000')
print(my_set)