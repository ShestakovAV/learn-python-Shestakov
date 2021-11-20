#name = input('введите Ваше имя: ')
#print(f'Привет, {name}! как дела?')

my_list = [3, 5, 7, 9, 10.5]
#print(my_list)
#my_list.append('Python')
#print(len(my_list))
#print(my_list[0])
#print(my_list[-1])
#print(my_list[1:4])
#my_list.remove('Python')
#print(my_list)


geo_dict = {'city':'Moscow', 'temperature':'20'}
print(geo_dict['city'])
geo_dict['temperature'] = str(int(geo_dict['temperature']) - 5)
print(geo_dict)
print(geo_dict.get('country', 'Россия'))
geo_dict['date'] = '27.05.2019'
print(len(geo_dict))
