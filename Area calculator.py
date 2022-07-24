import math

shape = input('Which shape are you interested in?:\n')

if shape == 'sphere':
    r = int(input('Please enter the radius of the sphere:\n'))
    area = 4*(math.pi)*r**2
    print('The area of a sphere of radius', r, 'is', area)

elif shape == 'triangle':
    h = int(input('Please enter the height of the triangle:\n'))
    b = int(input('Please enter the base of the triangle:\n'))
    area = 0.5*h*b
    print('The area of a triangle of height', h, 'and base', b, 'is', area)

elif shape == 'rectangle':
    l = int(input('Please enter the length of the rectangle:\n'))
    h = int(input('Please enter the height of the rectangle:\n'))
    area = l*h
    print('The area of a rectangle of length', l, 'and height', h, 'is', area)

elif shape == 'circle':
    r = int(input('Please enter the radius of the circle:\n'))
    area = (math.pi)*r**2
    print('The area of a circle of radius', r, 'is', area)
    
else:
    print('You have entered an invalid shape name. Only the following shapes are supported: sphere, triangle, rectangle or circle')