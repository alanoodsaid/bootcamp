from employee import Employee

def main():
    
    emp1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING"),
    emp2=Employee("JONES", "E7499", 45000, "RESEARCH"),
    emp3=Employee("MARTIN", "E7900", 50000, "SALES"),
    emp4=Employee("SMITH", "E7698", 55000, "OPERATIONS")
    
    print(employee_details())
    print("Calculated Salary:", emp1.calculate_emp_salary(55))  
    emp_department("HR")  
    employee_details()

     
       
    
main()    
    
    
    