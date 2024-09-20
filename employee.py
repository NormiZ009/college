import employee

print("Salary Program")
name = str(input("Enter name of employee: "))
basic = float(input("Enter basic salary: "))
netpay = employee.netpay(basic)
print(f"Net salary is: {netpay}")
grospay = employee.grospay(basic, netpay)
print(f"Gross salary is: {grospay}")