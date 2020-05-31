from sys import argv

# script, filename = argv

txt = open("ex15_example.txt", 'a+')
txt.write("hello")
# print(txt.read())

lines = txt.readlines()

txt.close()