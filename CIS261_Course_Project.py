#James Salinas
#CIS261
#Week 2 CIS261 Course Project- Payrole



def getDatesWorked():
    fromDate = input('Please enter start date in the following format MM/DD/YYYY:   ')
    endDate = input('Please enter the end date in the following format MM/DD/YYYY:   ')
    return fromDate,  endDate

#This function will return and get the employee name
def getEmpName():
    empName = input('Enter employee name:    ')
    return empName

#Enter and get hours
def getHoursWorked():
    hours = float(input('Enter hours worked:     '))
    return hours

#Enter and get rate of pay
def getHourlyRate():
    hourlyRate = float(input('Enter Hourly Rate:     '))
    return hourlyRate
 
 
#Enter tax bracket and do the math 
def getTaxRate():
    taxRate = float(input('Enter tax rate:     '))
    taxRate = taxRate / 100
    return taxRate
    
#calculate tax net pay
def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

#Function that will display name, hours, pay rate, gross pay, income tax, net pay in a loop
def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f'{hours:,.2f}', f'{hourlyRate:,.2f}', f'{grosspay:,.2f}', f'{taxRate:,.1%}', f'{incometax:,.2f}', f'{netpay:,.2f}')
        
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += grosspay
        totalTax += incometax
        totalNetPay += netpay

        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay
    
#This will print totals of all the information gathered
def printTotals(empTotals):
    print(f'Total numbers of employees: {empTotals["totEmp"]}')
    print(f'Total hours of employees: {empTotals["totHours"]}')
    print(f'Total gross pay of employees: {empTotals["totGross"]}')
    print(f'Total tax of employees: {empTotals["totTax"]}')
    print(f'Total net pay of emplyess: {empTotals["totNet"]}')
    
if __name__ == '__main__':
    empDetailList = []
    empTotals = {}
    
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, endDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetail)
            
               
    printInfo(empDetailList)
    printTotals(empTotals)
    
    
    