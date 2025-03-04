data = {
    1: "line one",
    "two": "this is line number second",
    "array": ["first", "second", "third"],
    "obj": {1: True, 2: False}
}
for key in data:
    print(key, data[key])

data["two"] = "this is new line"
data["three"] = "this is new line three"
data.pop("obj")

for key in data:
    print(key, data[key])
print(data["array"][2])

data = {}