engineering_dept = {'Bibek': 'Manager', 'Tamang' : 'Jr.Engineer', 'Rajesh': 'Sr. Engineer',
                    'Raj': 'Sr. Manager','Dheeraj': 'Tech. Lead', 'Golden': 'Jr. Engineer'}

employee_tenure = {
    "Bibek" : 5,
    "Tamang" : 4,
    "Rajesh" : 2,
    "Raj" : 6,
    "Dheeraj" : 1,
    "Golden" : 4,
    "Jack": 3,
    "Charlie": 2    
}

experienced_engineer = {(employee, role) for (employee, role) in engineering_dept.items()
 if employee_tenure[employee] >=4 if "Manager" in role}
print(experienced_engineer)