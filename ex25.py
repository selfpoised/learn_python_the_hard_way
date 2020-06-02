def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)

arr = []
fruits = ['apple', 'orange' , 'pear']
for f in fruits:
    arr.append(f)
    print(f"f {f}")
print(len(arr))

count = [1, 2, 3, 4, 5]
for n in count:
    print(f"n {n}")

if 2 > 1:
    print("hello world")
elif 2 < 1:
    print("hello not")
else:
    print("no")
