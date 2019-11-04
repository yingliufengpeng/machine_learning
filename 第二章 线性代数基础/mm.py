from collections import defaultdict, namedtuple

print('kk')

d = defaultdict(int)

for i in range(10):

    d[i] = i 


a = '''
    相性相关的模型,我们也是可以获得到的某种不可知的类型!!!
'''

print('d is', d)

print('a is', a)


User = namedtuple('User', ['name', 'age'])

u = User('wangpeng', 30)

print('u is', u)