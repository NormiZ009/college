print("Enter two complex numbers in the form a+bj, separated by a comma:")
n1, n2 = input().split(",")

n1 = complex(n1.strip())
n2 = complex(n2.strip())

print("Sum:", n1 + n2)