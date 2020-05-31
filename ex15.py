from sys import argv

# script, filename = argv

txt = open("ex15_example.txt", 'a+')
txt.write("hello")
# print(txt.read())

lines = txt.readlines()

txt.close()

def f1(a1, a2):
    print(f"{a1}, {a2}")

f1("hello ", "world")