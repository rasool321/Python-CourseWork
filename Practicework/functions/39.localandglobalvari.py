def gl():
    x ='Local'
    return f'Inside function: {x}'

y='Global'
print(f'Outside function: {y}')
print(gl())