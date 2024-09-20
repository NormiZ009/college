def positional(ram,shyam,harish):
    print("ram","shyam","harish")
a="ram"
b="shyam"
c="harish"
positional(a,b,c)
def keyword(ram,shyam,harish):
    print("ram","shyam","harish")
a="ram"
b="shyam"
c="harish"
keyword(ram=a,shyam=b,harish=c)
def default(ram,shyam,harish="harish"):
    print(ram,shyam,harish)
a="ram"
b='shyam'
c='harish'
default(ram=a,shyam=b)