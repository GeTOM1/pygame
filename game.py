dict = {
    "name":"Tom",
    "age":23,
    "city":"London",
    "height":200
}

print(dict.keys())
print(dict.values())

dict["hobby"] = "Coding"
lis = []

for key in dict.keys():
    print(key,dict[key])
    lis.append(key)
print(lis)

if "profile" in dict:
    print(dict["profile"])
else:
    print("Key does not exist.")