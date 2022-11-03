from math import pi
def circle_area(r):
    if type(r) not in [int,float]:
        raise TypeError("The radius must be a non-negative real number.")
    if r<=0:
        raise ValueError("The radius cannot be negative")
    return pi*r**2

# radius=[5,0,-3,2+3j,True,"Chennai"]
#
# for r in radius:
#     A=circle_area(r)
#     print(f"Area of circle with r={r} is {A}")