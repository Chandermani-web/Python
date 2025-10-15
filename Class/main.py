class Student:
    def __init__(self, name, rollno, course, branch):   #dunder method which is automatically called
          print("Dunder method(__init__) is called")
          self.name = name
          self.rollno = rollno
          self.course = course
          self.branch = branch
          
    def Display(self):
         print(f"Student Name = {self.name}\nStudent RollNo = {self.rollno}\nCourse = {self.course}\nBranch = {self.branch}\n")
        
    def Insert_Data_In_File(self):
        with open("Student.txt","a") as file:
            file.write(f"Student Name = {self.name}\nStudent RollNo = {self.rollno}\nCourse = {self.course}\nBranch = {self.branch}\n{'-'*40}\n") 
        self.Display()
            
    @staticmethod
    def Done():
         print("Work Done✅")
         


s1 = Student("Chandermani",20123002,"B.Tech","CSE")
s1.Insert_Data_In_File()
Student.Done() 