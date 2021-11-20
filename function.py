def get_summ(one, two, delimer='&'):
    in_def_one = str(one)
    in_def_two = str(two)
    union = in_def_one + str(delimer) + in_def_two 
    return union
l_p = get_summ('Learn', 'python')
print(l_p.upper())

a = 's'
b = 'f'
c = f'{a} {b}'
's f'