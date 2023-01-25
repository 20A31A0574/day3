#multiple inheritance
class OOPS:
    def Learning(self):
        print("learning concepts of python")
class java:
    def Learning(self):
        print("learning concepts of java")
class student(OOPS,java):
    pass
stu=student()
stu.Learning()
