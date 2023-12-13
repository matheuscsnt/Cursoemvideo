a = input('Digite algo: ')
print(f'''
    É Alpha númerico? {a.isalnum()},
    É alpha? {a.isalpha()},
    É Minuscula? {a.islower()},
    É maiuscula? {a.isupper()},
    Está capitalizada? {a.istitle()},
    É Decimal? {a.isdecimal()},
    É numérica? {a.isnumeric()},
    É espaço? {a.isspace()}.
      ''')