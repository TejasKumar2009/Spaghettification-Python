import periodictable

print("Spaghettification is the phenomena near black hole in which the objecct gets stretched like a noodle.\nIn this program u have to enter element and radius of the sphere u want and this program will tell upto which length the sphere will be spaghettified !!!\n\n")


try:

    element_symbol = input("Enter the element symbol of which your spherical ball is composed of : ")

    radius = int(input("Enter the radius of the spherical ball (in cm) : "))

    volume_of_sphere = 4/3*22/7*radius*radius


    element = periodictable.elements.symbol(element_symbol)

    mass = (element.mass)*1.67377*10**-24
    density = element.density

    volume_of_atom = mass/density

    diameter_of_atom = (volume_of_atom*3/4*22/7)**3

    no_of_atoms = volume_of_sphere/volume_of_atom


    distance = diameter_of_atom*no_of_atoms
    lightyear_cm = 9.461e+17  # 1 light-year in centimeters
    lightyears = distance / lightyear_cm

    print(f"\nIf this ball is taken near to the event horizon of the black hole this ball will be saghettified to {lightyears} Light Years. AMAZING RIGHT!!!\nBut actually we cannot observe this phenomena and this will not gonna happen that the ball will be spaghettified to {lightyears} Light years because of the limitation of the speed of matter. \n")

    print("NOTE : THIS IS JUST AN ASSUMPTION. ACTUAL SPAGHETTIFICATION CAN BE LESS OR EVEN FURTHER UP TO SUBATOMIC LEVELS.\n\n")







     
except KeyError:
    print("Element symbol not found !")

except:
    print("Invalid input !")