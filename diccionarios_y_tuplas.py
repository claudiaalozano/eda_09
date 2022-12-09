from collections import defaultdict
from collections import OrderedDict
from collections import 
d = defaultdict(float)

print(d["uno"])
print(d)

defaultdict(float, {uno: 0.0})
d = defaultdict(str)
print(d["uno"])
print(d)

d = defaultdict(str, {uno: ""})
d = defaultdict(object)
print(d["uno"])
print(d)

n = OrderedDict()
n["uno"] = 1
n["dos"] = 2
n["tres"] = 3

print(n)
OrderedDict([("uno", 1), ("dos", 2), ("tres", 3)])
n1 = {}
n1["uno"] = 1
n1["dos"] = 2

n2 ={}
n2["dos"] = 2
n2["uno"] = 1

print(n1 == n2)

