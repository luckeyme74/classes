class Student(object):
    """This class will define students by student i.d., first name, last name and email."""

student_a = Student()
student_a.studentid = "001"
student_a.firstname = "Rose"
student_a.lastname = "Murphy"
student_a.email = "rosie22@yahoo.com"

student_b = Student()
student_b.studentid = "002"
student_b.firstname = "Gavin"
student_b.lastname = "Murphy"
student_b.email = "gman12705@hotmail.com"

student_c = Student()
student_c.studentid = "003"
student_c.firstname = "Grace"
student_c.lastname = "Murphy"
student_c.email = "firstbasegrace@yahoo.com"

print student_a.studentid + "     " + student_a.lastname + ", " + student_a.firstname + "      " + student_a.email
print student_b.studentid + "     " + student_b.lastname + ", " + student_b.firstname + "     " + student_b.email
print student_c.studentid + "     " + student_c.lastname + ", " + student_c.firstname + "     " + student_c.email
