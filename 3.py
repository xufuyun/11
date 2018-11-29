#!/usr/bin/python3
#-*- coding:UTF-8 -*-
class Student():
    pass
#定义一个空类，此处pass必须有
minyue=Student()
#再定义一个类，用来描叙Python的学生
class PythonStudent():
    name = None
    age = 18
    course = "python"
    def doHomework(self):
        print("正在做笔记")
        return 
#实例化
mingyue = PythonStudent()
print(mingyue.name)
print(mingyue.age)
mingyue.doHomework()
