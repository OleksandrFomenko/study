d = {"alice": 35, "mark": 25, "april": 45, "john": 19}
d_pop = {}
for name, age in d.items():
    if name[0] == "a":
        d_pop[name] = age
for name, age in d_pop.items():
    d.pop(name)
print(d)
