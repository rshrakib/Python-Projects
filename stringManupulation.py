from operator import concat

x = "Hello word"
print(x)

# multiline
m = """Hello
hi
hello
rakib"""
print(m)

# slice a stirng
print(x[1:6])
print(x[:6])
print(x[1:])

# upper lower
print(x.upper())
print(x.lower())

#remove whitespaces
print(x.strip())

#replace
print(x.replace("H", "@"))

# concatenation
b = "Rakib"
s = concat(x,b)
#list
a = ["apple", "banana", "oragne", 1 , "cherry"]
print(a)
print(len(a))
a.pop(1)
print(a)
a.append("mango")
print(a)
a.remove("cherry")
print(a)
c = a.copy()
print(c)
a.clear()
print(a)


#tuples
t = ("apple", 5, "banana")
print(t)
print(t.count("apple"))
print(t.index(5))

#sets
sets = {1,"apple", False,"apple"}
print(sets)
sets.add(5)
print(sets)
sets.discard("apple")
print(sets)

#dictionary
dic = {"Name": "Rakib", "Age": 24, "Education": "CSE in BRUR"}
print(dic)
print(dic.keys())
print(dic.values())
print(dic["Name"])
print(dic["Education"])
for value in dic:
    print(f"{value}: {dic[value]}")
print(dic.clear())

