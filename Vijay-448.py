print("================Program 1======================")
'''
# Palindrome in python using for loop
palindrome is phrase if we write reverse of  that word it becomes same 
as  it gives same word 
Ex:Level,Malayalam etc.,
'''

val = input('Enter input: ')

i = 0
for i in range(len(val)):
    if val[i] == val[-1 - i]:
        print(val, 'is  a Palindrome')
        break
    else:
        print(val, 'is not a Palindrome')
        break

print("================Program 2======================")
# get input from user

n1 = int(input("enter num1:"))
n2 = int(input("enter num2:"))

output = 0

if len(str(n1)) == len(str(n2)):
    for i in range(len(str(n1))):
        x = str(n1)
        y = str(n2)

        output += (int(x[i]) + int(y[i]))

print(output)

print("================Program 3======================")

st = "ab@#cd!ef"


def reverseString(text):
    index = -1
    for ind in range(len(text) - 1, int(len(text) / 2), -1):

        if text[ind].isalpha():
            temp = text[ind]
            while True:
                index += 1
                if text[index].isalpha():
                    text[ind] = text[index]
                    text[index] = temp
                    break
    return text


ans = reverseString(list(st))

print("Output : ", "".join(ans))

print("================Program 4======================")
li = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]

# to create empty dictionaries
d = {}
s = {}
count = 0

for i in li:

    if i not in d:
        count = 1

        d[i] = count
    else:
        d[i] += 1

print("dictionary format of list :", d)

for i, j in d.items():
    if d[i] > 1:
        s[i] = j

print("only with duplicate counts:", s)

print("================Program 5======================")

t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
lis1 = []
lis2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in lis2 and isinstance(i, int):
                lis2.append(i)
                lis1.append((t + i))
                break
    else:
        for i in t2:
            if i not in lis2 and isinstance(i, str):
                lis2.append(i)
                lis1.append((t + i))
                break

print(lis1)

print("================Program 6======================")

inp = "216.08.094.196"
out = []
x = inp.split(".")  # split the input by "."

for i in x:

    if i[0] == '0':
        i = i[1:]
        out.append(i)
    else:
        out.append(i)

result = ".".join(out)
print(result)

print("================ Program 7 ======================")

lis = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]


def rec(l):
    l1 = []
    for it in l:
        if isinstance(it, int):
            l1.append(it)
        elif isinstance(it, list):
            ex = rec(it)
            l1.extend(ex)
    return l1


print(rec(lis))
