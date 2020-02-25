import cmath 
def get_y_operator(formatted):
    for index in range(0, len(formatted)):
        if formatted[index] == "+" or formatted[index] == "-": 
            return (index + 1)
        else: 
            pass

def get_coords():
    global complex_num
    formatted = complex_num[0: (len(complex_num) - 1)]
    operator_index = get_y_operator(formatted[1: len(formatted)])
    return (int(formatted[0: operator_index]), int(formatted[(operator_index ): len(formatted)]))

complex_num = input()

x_coord, y_coord  = get_coords()

print(abs(complex(x_coord, y_coord)))
print(cmath.phase(complex(x_coord, y_coord)))
