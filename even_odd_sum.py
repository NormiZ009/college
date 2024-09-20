minimum = int(input("enter min value:"))
maximum = int(input("enter max value:"))
even_total = 0
odd_total = 0
for num in range(minimum,maximum+1):
    if num%2==0:
        even_total = even_total + num
    else:
        odd_total = odd_total + num

print(f"the sum of even number from {minimum} to {maximum} = {even_total}")
print(f"the sum of even number from {minimum} to {maximum} = {odd_total}")