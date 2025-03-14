# class book:
#     def __init__(self,t,a,y,i):
#         self.title=t
#         self.author=a
#         self.year=int (y)
#         self.isbn=i


#     def bookmassage(self):
#         print(f"书名:{self.title}"+f" 作者:{self.author}"+f" 出版年份:{self.year}"+f" ISBN:{self.isbn}")
#         if self.year<=1970:
#             print("这本书是经典书籍.")
#         else:
#             print("这本书不是经典书籍.")
# book1=book("百年孤独","加西亚 马尔克斯","1967","978-3-16-138410-0")
# book2=book("Python编程","迈克尔 多赫提","2015","978-0-13-419044-0")

# book1.bookmassage()
# book2.bookmassage()

# import math
# class shape:
#     def __init__(self,color):
#         self.color=color

# class Circle(shape):
#     def __init__(self, color,radius):
#         super().__init__(color)
#         self.radius=radius

#     def area(self):
#         return math.pi*self.radius*self.radius


# Circle=Circle("red",7)
# print(Circle.color,f'area={Circle.area():.2g}')

class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id

    def display_info(self):
        print("员工信息:")
        print(f'姓名: {self.name}，薪水: {self.salary}，员工编号: {self.employee_id}', end=" ")

class Manager(Employee):
    def __init__(self, name, salary, employee_id, department, bonus):
        super().__init__(name, salary, employee_id)
        self.department = department
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print(f'部门: {self.department}，奖金: {self.bonus}', end=" ")

    def total_compensation(self):
        return self.salary + self.bonus

employee1 = Employee("Alice", 5000, "E001")
manager2 = Manager("Mark", 8000, "E002", "IT", 10000)

employee1.display_info()
print(f"\n年薪: {employee1.salary}")

print()
manager2.display_info()
print(f"\n年薪: {manager2.total_compensation()}")