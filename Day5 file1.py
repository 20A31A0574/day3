#single inheritance
class A:
    name='pavani'
    age=21
class B(A):
    name='baby'
    age=4
obj=B()
print(obj.age)
print(obj.name)
