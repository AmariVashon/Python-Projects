names = ["    ryan", "PAUL", "kevin connors     "]
converted_names = list(map(lambda n : n.strip().title(), names))
print(converted_names)

print("\n")

names = ["Amanda", "Frank", "abby", "Ripal", "Adam"]
converted_names = list(filter(lambda n : True if n[0].lower() != "a" else False, names))
print(converted_names)
