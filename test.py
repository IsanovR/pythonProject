# #a = int(input('ведите число'))
# print("{:.20f}".format(5.0/3))
# a = 12345
# b = 540
# #print({:x<4d} format (a))
# print("{:x<4d}".format(1))
# t = int(input('sec'))
# # th = t/3600
# # tm = th*60
# # t = t/1000
# #
# # print('час', th, 'мин:', tm, 'секунд:', t)
# sec = int( input('Enter seconds: ') )
# h = ((sec//3600))%24
# m = (sec//60)%60
# s = sec%60
#
# print( '%d:%02d:%02d'% (h, m, s) )
# OR
# print( '{0}:{1:=02}:{2:=02}'.format(h, m, s) )
#
# intervals = (
#     ('weeks', 604800),  # 60 * 60 * 24 * 7
#     ('days', 86400),    # 60 * 60 * 24
#     ('hours', 3600),    # 60 * 60
#     ('minutes', 60),
#     ('seconds', 1),
# )
#
# def display_time(seconds, granularity=2):
#     result = []
#
# for name, count in intervals:
#     value = seconds // count
# if value:
#     seconds -= value * count
# if value == 1:
#     name = name.rstrip('s')
# result.append("{} {}".format(value, name))
# return ', '.join(result[:granularity])
# a = int(input('введите сколько бегал спортсмен за один день'))
# b = int(input('введите сколько км пробежал спортсмен'))
# c = 1
# print('1 -й день: ', a)
# while a < b:
#     a = a * 0.1+a
#     c = c+1
#     print(c,'-й день: ', '%.2f' % (a))
# print(c,'-й день: ', a)
a = int(input('введите выручку: '))
b = int(input('введите издержки: '))

if a >= b:
    print('фирма в прибыле')
    c = int(input('введите численность сотрудников: '))
    if a/b > a:
        print('Фирма рентабельность с численностью сотрудников: ', c, 'прибыль на одного сотрудника: ', a/b)
    else:
        print('Фирма убыточна с численностью сотрудников: ', c)

elif a<b:
    print('Фирма в убытке (')