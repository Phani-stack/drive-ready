'''
Dunk Typing
Operator Overloading
Method overriding
'''

# Duck Typing
class Robot:
    def work(slef):
        print("Robot coding")


class Teacher:
    def work(self):
        print("Teacher coding")


class Student:
    def work(self):
        print("Student coding")


def code(person):
    person.work()




def main():
    code(Robot())

main()
