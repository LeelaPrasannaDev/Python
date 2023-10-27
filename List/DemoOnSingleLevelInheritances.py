# parent class or base class
class College:

    def college_info(self):
        self.name = "SRIT"
        self.address = "Proddutur"
        self.age = "10 years"


class Department(College):
    def dep(self):
        self.dep1 = "CIVIL"
        self.dep2 = "MEC"
        self.dep3 = "CSC"
        self.dep4 = "ECE"
        self.dep5 = "EEE"


clg_info = Department()
clg_info.college_info()
clg_info.dep()
print("Name of the college = ",clg_info.name)
print("Address of the college = ",clg_info.address)
print("Age of the college = ",clg_info.age)
print("Department1 in the college = ",clg_info.dep1)
print("Department2 in the college = ",clg_info.dep2)
print("Department3 in the college = ",clg_info.dep3)
print("Department4 in the college = ",clg_info.dep4)
print("Department5 in the college = ",clg_info.dep5)