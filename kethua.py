class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"Sinh viên {self.name} (ID: {self.student_id}) đang chạy DL sấp mặt.")


student1 = Student("Lê Đức Anh", 20, "23110145")
print(f"Thông tin: Tên: {student1.name}, Tuổi: {student1.age}")
student1.study()