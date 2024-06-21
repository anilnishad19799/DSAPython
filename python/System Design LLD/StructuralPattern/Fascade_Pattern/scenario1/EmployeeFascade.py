from EmployeeDAO import EmployeeDAO

class EmployeeFascade:
    def __init__(self):
        self.employeefascadeobj = EmployeeDAO()
        
    def insert(self):
        self.employeefascadeobj.insert()
    
    def getEmployeeDetail(self, empid):
        return self.employeefascadeobj.GetEmployeeDetail(empid)
