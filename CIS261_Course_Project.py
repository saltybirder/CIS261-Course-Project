#James Salinas
#CIS261
#Week 2 CIS261 Course Project- Payrole

#This function will return and get the employee name
def getEmpName():
    empName = input('Enter employee name:    ')
    return empName

#Enter and get hours
def getHoursWorked():
    hours = float(input('Enter hours worked:     '))
    return hours

#Enter and get rate of pay
def getPayRate():
    payRate = float(input('Enter rate of pay:     '))
    return payRate

#Enter tax bracket and do the math 
def getTaxRate():
    taxRate = float(input('Enter tax rate:     '))
    taxRate = taxRate / 100
    return taxRate
    
#calculate tax net pay
def CalcTaxAndNetPay(hours, payRate,taxRate):
    gPay = hours * payRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

