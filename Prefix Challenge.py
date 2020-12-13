# Variables
going = True


# Functions
def c_p(x, y, z, common):
    if len(y) == 0 or len(x) == 0 or len(z) == 0 or x[0] != y[0] or y[0] != z[0] or z[0] != x[0]:
        return common
    return(c_p(x[1:], z[1:], y[1:], common + x[0]))


# Main Loop
while going == True:
    string1 = input("Give me the first word. ")
    string2 = input("Give me the second word. ")
    string3 = input("Give me the third word. ")
    common = ""
    common_prefix = c_p(string1, string2, string3, common)
    print(common_prefix)