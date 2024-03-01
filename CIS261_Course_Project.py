#James Salinas
#CIS261
#Week 7 CIS261 Course Project- Payrole Phase III

#Adding in lines to create users and loggin information
from datetime import datetime

def CreateUsers():
    print('##### Create users, passwords, and roles #####')
    UserFile = open("Users.txt", "a+")
    while True:
        username = GetUserName()
        if (username.upper() == "END"):
            break
        userpwd = GetUserPassword()
        userrole = GetUserRole()
        
        UserDetail = username + "|" + userpwd + "|" + userrole + "\n"
        UserFile.write(UserDetail)
        
    UserFile.close()
    printuserinfo()
    
def GetUserName():
    username = input("Enter user name or 'End' to quit: ")
    return username

def GetUserPassword():
    pwd = input("Enter password: ")
    return pwd

def GetUserRole():
    userrole = input("Enter role (Admin or User): ")
    while True:
        if (userrole.upper() == "ADMIN" or userrole.upper() == "USER"):
            return userrole
        else:
            userrole = input("Enter role (Admin or User): ")
            
def printuserinfo():
    Userfile = open("User.txt", "r")
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            break
        UserDetail = UserDetail.replace("\n", "")
        UserList = UserDetail.split ("|")
        username = Userlist[0]
        userpassword = UserList [1]
        userrole = UserList [2]
        print("User Name: ", username, " Password: ", userpassword, " Role: ", userrole)
        
#Login Defined

def Login():
    UserFile = open("User.txt", "r")
    UserList = []
    UserName = input("Enter User Name: ")
    UserPwd = input("Enter Password: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.realine()
        if not UserDetail:
            return UserRole, UserName, UserPwd
        UserDetail = UserDetail.replace("\n", "")
        
        UserList == UserDetail,split("|")
        if UserName == UserList [0] and UserPwd == UserList [1]:
            UserRole = UserList [2] # user is valid, return role 
            return UserRole, UserName
    return UserRole, UserName
            
        
    
    
def GetDatesWorked():
    fromdate = input("Please enter start date in the following format MM/DD/YYYY:   ")
    todate = input("Please enter the end date in the following format MM/DD/YYYY:   ")
    return fromdate, todate

#This function will return and get the employee name
def GetEmpName():
    empname = input("Enter employee name:    ")
    return empname

#Enter and get hours
def GetHoursWorked():
    hours = float(input("Enter hours worked:     "))
    return hours

#Enter and get rate of pay
def GetHourlyRate():
    hourlyrate = float(input("Enter Hourly Rate:     "))
    return hourlyrate
 
 
#Enter tax bracket and do the math 
def GetTaxRate():
    taxrate = float(input("Enter tax rate:     "))
    return taxrate
    
#calculate tax net pay
def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

#Function that will display name, hours, pay rate, gross pay, income tax, net pay in a loop
def printinfo(EmpDetailList):
     TotEmployees = 0
     TotHours = 0.00
     TotGrossPay = 0.00
     TotTax = 0.00
     TotNetPay = 0.00 #made it here with my work on Thursday
     for EmpList in EmpDetailList:
         fromdate = EmpList[0]
         todate = EmpList[1]
         empname = EmpList[2]
         hours = EmpList[3]
         hourlyrate = EmpList[4]
         taxrate = EmpList[5]
        
         grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
         print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
        
         TotEmployees += 1
         TotHours += hours
         TotGrossPay += grosspay
         TotTax += incometax
         TotNetPay += netpay

     EmpTotals["TotEmp"] = TotEmployees
     EmpTotals["TotHrs"] = TotHours
     EmpTotals["TotGrossPay"] = TotGrossPay
     EmpTotals["TotTax"] = TotTax
     EmpTotals["TotNetPay"] = TotNetPay
    
#This will print totals of all the information gathered
def PrintTotals(EmpTotals):
     print()
     print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
     print(f"Total Hours Worked: {EmpTotals['TotHrs']}")
     print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:,.2f}")
     print(f"Total Income Tax: {EmpTotals['TotTax']:,.2f}")
     print(f"Total Net Pay: {EmpTotals['TotNetPay']:,.2f}")   
     
def WriteEmployeeInformation (employee):
    file = open("employeeinfo.txt", "a")
    file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
                                                                                                      
def GetFromDate():
    valid = False
    fromdate = ""
    
    while not valid:
        
        fromdate = input("Enter From Date (mm/dd/yyyy):   ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid Date Format:   ")
        else:
            valid = True
            
    return fromdate
 
def ReadEmployeeInformation(fromdate):
    EmpDetailList = []
    
    file = open("employeeinfo.txt", "r")
    data = file.readlines()
    
    conditiion = True
    
    if fromdate.upper() == 'ALL':
        condition = False
        
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        
        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromdate == employee[0]:
                EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList
        
        
if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
            
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        
        print()
        
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        WriteEmployeeInformation(EmpDetail)
        
    print()
    print()
    fromdate = GetFromDate()
    
    EmpDetailList = ReadEmployeeInformation(fromdate)
    
    print()
    print(EmpDetailList)
    
    
    