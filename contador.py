from collections import Counter

l = [1, 1, 1, 1 , 2, 2 , 3]
c = Counter(l)
print(l)
Counter({1:4,2:2, 3:1})
Counter({"a":3, "r": 2, "s":1, "p": 1, "b": 1})
c = Counter("palabras")
print(c)
animales = "gato perro gato canario perro"
Counter(animales.split())
Counter({"gato": 2, "canario": 1, "perro":2})


animales = "gato perro gato canario perro"
c = Counter(animales.split())

print(c.most_common(1))
print(c.most_common(2))
print(c.most_common(3))

[("perro", 3)]
[("perro", 3), ("gato", 2)]
[("perro", 3), ("gato", 2), ("canario", 1)]

l = [10, 20, 30, 40, 10, 20, 30, 10, 20, 10]
c = Counter(l)
print(c.items())
print(c.keys())
print(c.values())
print(sum(c.values()))

print(dict(c))

