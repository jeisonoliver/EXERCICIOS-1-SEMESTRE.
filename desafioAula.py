x = True
y = True
z = False
w = (x and y and (not z)) or (x and (not y) and z)

print(w)