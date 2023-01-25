#polymorphism : many forms
#method overriding is also called runtime polymorphism
class A:
    def method_1(self,a,b):
        print("sum of two numbers:",a+b)
class B(A):
    def method_1(self,a,b):             #method overriding: as it is also being used in classA
        print("mul of a and b : ",a*b)
    def method_1(self,abc):             #method overlkoading 
        print("value is",abc)
obj=B()
obj.method_1(10)
