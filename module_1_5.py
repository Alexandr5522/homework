immutable_var='table','chair','laptop','book',22,33,44
print(type(immutable_var))
print(immutable_var)
#immutable_var[0]='picture' # кортежи не позволяют производить замену
mutable_list=[22,33,44,'table','chair','laptop','book']
print(type(mutable_list))
print(mutable_list)
mutable_list[0]=99
print(mutable_list)
mutable_list.remove('book')
print(mutable_list)
mutable_list.extend(['laptop',88])
print(mutable_list)