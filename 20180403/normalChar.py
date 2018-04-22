def normalize(name):
    return name[:1].upper() + name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = map(normalize, L1)
print(L2)
