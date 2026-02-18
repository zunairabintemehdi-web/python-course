setc1 = {"5", "6"}
setc2 = {"6", "7"}
print("Original sets:")
print(setc1)
print(setc2)
setc = setc1.union(setc2)
print("\nUnion of above sets:")
print(setc)
setx = {"8", "9"}
sety = {"6", "8"}
print("Original set elements:")
print(setx)
print(sety)
print("\nIntersection of two said sets:")
setz = setx.intersection(sety)
print(setz)