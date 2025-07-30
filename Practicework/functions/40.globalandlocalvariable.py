def gl(x):
    x =20
    return f'Local x: {x}'

x=10
print(f'Global x: {x}')
print(gl(x))