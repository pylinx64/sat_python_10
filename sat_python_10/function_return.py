def sayHello():
	print('Hello world')
	
# процедура
sayHello()

def sum2(a, b):
	s = a + b
	return s

z = sum2(1, 2)
print(z)

print(sum2(1, 2))

def proz(a, b, c):
	s = a ** b * c
	return s
	
z = proz(1, 2, 3)
print(z)

import time
def test_1(a, b, c):
	print('-------#test1-----')
	et = time.time()
	res = proz(a, b, c)
	st = time.time()
	dt = st - et
	print('#test1 time - ', dt)
	print('#test1 res - ', res)

#test_1(100000, 100000, 1000000000000)

try:
	a = 10; b = 0
	x = a / b
	print(x)
except:
	print('На ноль делить нельзя!')
	

