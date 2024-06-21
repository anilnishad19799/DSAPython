from EmployeeFascade import EmployeeFascade

class EmployeeClient:
    def __init__(self) -> None:
        pass

    def getEmployeeDetail(self):
        employeeFascadeobj = EmployeeFascade()
        empdetails = employeeFascadeobj.getEmployeeDetail(1234)