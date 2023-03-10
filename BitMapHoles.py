BitMap = ['11111','10001','10101','10001','11111','00000']

def bitmap(strArr): # Function which counts the number of 'holes' in a bitmap ( 2D Array )
    holes = 0
    number_of_zeros_in_line = 0 # Keeps track of holes horizontally
    y_track = 0 
    for line in strArr:
        x_track = 0
        for number in line:
            if number == '0':
                if y_track > 0:
                    if  strArr[y_track-1][x_track] == '0': # keeps track of holes vertically
                        pass
                    else:
                        if number_of_zeros_in_line == 0:
                            holes += 1
                else:
                    if number_of_zeros_in_line > 0:
                        pass
                    else:
                        holes += 1
                number_of_zeros_in_line += 1
            else:
                number_of_zeros_in_line = 0
            x_track += 1
        number_of_zeros_in_line = 0
        y_track += 1
    return holes

x = bitmap(BitMap)
print("Number of holes", x)

                    
