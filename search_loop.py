def search(list1,n):
    for i in range(len(list1)):
        if list1[i]==n:
            return True
            return False

list1 = ['1','2',"kushal",'4',"python",'5.6']

n = "python"
if search(list1,n):
    print("found")
else:
    print("not found")