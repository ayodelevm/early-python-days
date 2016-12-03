def printnames(lst_names):
    for name in lst_names:
        print (name)
names = ["bayo","Tade"]
new_names = ["John", "Ade"]
printnames(names)
printnames(new_names)
names[0] = "Bayo"
names.append(new_names)
dictionary = {"Bayo": 12}
print(names)