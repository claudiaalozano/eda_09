from collections import Counter

l = [1, 1, 1, ,1 , 2, ,2 , 3]
c = Counter(l)
print(l)
Counter({1:4,2:2, 3:1})
Counter({"a":3, "r": 2, "s":1, "p": 1, "b": 1})
c = Counter("palabras")
print(c)
animales = "gato perro gato canario perro"
Counter(animales.split())
Counter({"gato": 2, "canario": 1, "perro":2})


