"""Rules of thumb for plane design"""

multiplier = 0
root_chord = 0
wingspan = 0
wingspan_to_root_chord_ratio = 0
wing_thickness = 0
aileron_area = 0
wing_half_surface_area = 0
fuselage_length = 0
horizontal_stabilzer = 0
elevator = 0
vertical_stabilzer = 0
rudder = 0
cg = 0

#The Wingspan should be 5 or 6 times the Root Chord
def set_root_chord(wingspan, size):
    global root_chord
    global wingspan_to_root_chord_ratio

    if (size == "small"):
        root_chord = round(wingspan/5)
        wingspan_to_root_chord_ratio = 5

    if (size == "big"):
        root_chord = wingspan/6
        wingspan_to_root_chord_ratio = 6
    return str(root_chord)

#Wing thickness should be 12-14% of the wing Root Chord
def set_wing_thickness(size,root_chord):
    global wing_thickness
    if (size == "small"):
        wing_thickness = root_chord * .12
    if (size == "big"):
        wing_thickness = root_chord * .14
    return str(wing_thickness)

#set the aileron surface area
def set_aileron_surface_area(wing_type, size, base):
    global wingspan
    global root_chord
    global aileron_area
    global multiplier
    global wing_half_surface_area

    if (size == "small"):
        multiplier = .10
    if (size == "big"):
        multiplier = .12

    if (wing_type.lower() == "rectangle"):
        wing_half_surface_area = (wing_half_surface_area/2) * root_chord
        aileron_area = wing_half_surface_area * multiplier
    #if (wing_type == "swept f or b"):
    #    aileron_area = 0
    if (wing_type.lower() == "tapered leading and trailing edge"):
        wing_half_surface_area = (.5 * ((wingspan/2) * (base + root_chord)))
        aileron_area = wing_half_surface_area * multiplier
    if (wing_type.lower() == "tapered leading or trailing edge"):
        wing_half_surface_area = (.5 * (root_chord * (base + (wingspan / 2))))
        aileron_area = wing_half_surface_area * multiplier
    return str(aileron_area)

#set the fuselage length
def set_fuselage_length(size):
    global wingspan
    global multiplier
    global fuselage_length

    if (size == "small"):
        multiplier = .70
    if (size == "big"):
        multiplier = .75

    fuselage_length = wingspan * multiplier
    return str(fuselage_length)

#Distance from Leading(l) Edge(e) to back of the prop
def set_l_e_to_back_of_prop_distance():
    global wingspan
    distance = wingspan * .15

    return str(distance)

#Distance from Leading(l) Edge(e) to the stabilzer
def set_l_e_to_stabilzer_distance():
    global root_chord
    distance = root_chord * 3
    return str(distance)

#Horizontal stabilzer size
def set_horizontal_stabilzer():
    global wing_half_surface_area
    global horizontal_stabilzer

    horizontal_stabilzer = (wing_half_surface_area * 2) * .25
    return str(horizontal_stabilzer)

#Set Elevator size
def set_elevator():
    global horizontal_stabilzer
    global elevator

    elevator = horizontal_stabilzer * .25
    return str(elevator)

#Vertical stabilzer size
def set_vertical_stabilzer():
    global wing_half_surface_area
    global vertical_stabilzer

    vertical_stabilzer = (wing_half_surface_area * 2) * .10
    return str(vertical_stabilzer)

#Set Rudder size
def set_rudder():
    global vertical_stabilzer
    global rudder

    rudder = vertical_stabilzer * .25
    return str(rudder)

#Set CG location
def set_cg(size):
    global root_chord
    global cg
    if (size == "small"):
        multiplier = .25
    if (size == "big"):
        multiplier = .33

    cg = root_chord * multiplier
    return str(cg)

#Set edf tube length
def edf():
    global edf_size
    thrust_tube = (edf_size * 0.0394) * 4
    return str(thrust_tube)

#sets edf trust tube exit diameter
def edf_thrust_tube():
    global edf_size
    global character
    if (character == "speed"):
        #16% smaller then entry diameter
        tube_exit = (edf_size * 0.0394) * .84
    if (character == "power"):
        #5% smaller then entry Diameter
        tube_exit = (edf_size * 0.0394) * .95
    if (character == "both"):
        #10.5% smaller the entry diameter
        tube_exit = (edf_size * 0.0394) * .895
    return str(tube_exit)


""" Main Menu """
print("Welcome to Project Plane Maker (PPM)!!!\nYour measurements will be output as a text file.")
name = input("Please enter the name of your plane: ")
name = str(name) + " Measurements"

"""creates file object and adds the name variable and a new line"""
file = open("%s.txt" % (name), "w")
file.write(name + ":\n\n")

"""Wingspan info needed here"""
print("\nTo Start designing your plane form the ground up, I will need two things: "
      "\nThe desired wingspan and the size of the airplane.")
wingspan = int(input("Wingspan: "))
while True:
    size = input("Is this a 'big' or 'small' airplane? ")
    if (size.lower() == 'big' or size.lower() == 'small'):
        break
"""Write available data to file"""
file.write("The Wingspan is "+ str(wingspan) + " inches.\n")
file.write("The Root Chord is "+ set_root_chord(wingspan, size) + " inches.\n")
file.write("The Wingspan to Root Chord Ratio is "+ str(wingspan_to_root_chord_ratio) + ".\n")
file.write("The Wing Thickness is "+ set_wing_thickness(size,root_chord) + " inches.\n")

"""wing type info needed here"""
print("***A Tapered wing will require you to enter the length of the tapered edge (Leading or Trailing)***")
print("\nNow I need some more information on the wing type you want to use. Please type one of the following.")
while True:
    wing_type = str(input('"Rectangle", "Tapered Leading or Trailing edge", or "Tapered Leading and Trailing edge": '))
    if (wing_type.lower() == "rectangle"):
        break
    if (wing_type.lower() == "tapered leading and trailing edge"):
        break
    if (wing_type.lower() == "tapered leading or trailing edge"):
        break

"""Use if statements to determine what to print to file"""
if (wing_type.lower() == "rectangle"):
    file.write("The Aileron Surface Area is " + set_aileron_surface_area(wing_type, size, 0) + " inches squared.\n")
if (wing_type.lower() == "tapered leading or trailing edge"):
    base = float(input("Please enter the tapered edge length: "))
    base= round(base)
    file.write("The Aileron Surface Area is " + set_aileron_surface_area(wing_type, size, base) + " inches squared.\n")
if (wing_type.lower() == "tapered leading and trailing edge"):
    base = input("Please enter the tapered edge length: ")
    file.write("The Aileron Surface Area is " + set_aileron_surface_area(wing_type, size, base) + " inches squared.\n")

"""Write available data to file"""
file.write("The Fuselage Length is "+ set_fuselage_length(size) + " inches.\n")
file.write("The distance from the Leading Edge to the Back of the Prop is "
           + set_l_e_to_back_of_prop_distance() + " inches.\n")
file.write("The distance from the Leading Edge to the stabilizer is "+ set_l_e_to_stabilzer_distance()
           + " inches.\n")
file.write("The Horizontal Stabilizer is "+ set_horizontal_stabilzer() + " inches squared.\n")
file.write("Note: If you have split horizontal stabilizers divide the above value by 2.")
file.write("The Elevator is "+ set_elevator() + " inches squared\n")
file.write("The Vertical Stabilizer is "+ set_vertical_stabilzer() + " inches squared.\n")
file.write("The Rudder is "+ set_rudder() + " inches squared.\n")
file.write("The CG is approximately "+ set_cg(size) + " inches from the leading edge.\n")

#special add on
print("\n")
using_edf = input("Are you using an edf?(yes or no)")
while True:
    if (using_edf.lower() == "yes"): break
    if (using_edf.lower() == "no"): break

edf_size = int(input("Enter the edf size, only the number portion in mm (like 64): "))
character = input("Do you want a plane with speed, power, or both? ")
while True:
    if (character == "speed"): break
    if (character == "power"): break
    if (character == "both"): break

file.write("The EDF size is "+ str(edf_size) + " mm.\n")
file.write("The EDF Thrust Tube is "+ edf() + " inches.\n")
file.write("The EDF Thrust Tube Exit Diameter is " + edf_thrust_tube() + " inches.\n")

file.write("\nAll measurements were calculated in \"Project Plane Maker\".")
file.close()

print("\nI have finished calculating the basic measurement for your new airplane."
      "\nPlease check the folder of this program for \"%s.txt\"" % (name))
print("\nThanks for using Project Plane Maker!!! Till next time.")
