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
def printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay):
    print(empName, f'{hours:,.2f}', f'{hourlyRate:,.2f}', f'{gPay:,.2f}', f'{taxRate:,.1%}', f'{incomeTax:,.2f}', f'{netPay:,.2f}')
    
#This will print totals of all the information gathered
def PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f'\nTotal numbers of employees: {totalEmployees}')
    print(f'Total hours: {totalHours:,.2f}')
    print(f'Total gross pay: {totalGrossPay:,.2f}')
    print(f'Total tax: {totalTax:,.2f}')
    print(f'Total net pay: {totalNetPay:,.2f}')
    
if __name__ == '__main__':
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    
    while True:
        empName = getEmpName()
        if (empName.upper() == "END"):
            break
        hours = getHoursWorked()
        hourlyRate = getHourlyRate()
        taxRate = getTaxRate()
        gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        
        printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay)

        totalEmployees += 1
        totalHours += hours
        totalGrossPay += gPay
        totalTax += incomeTax
        totalNetPay += netPay
    
    PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay)
    
    
    