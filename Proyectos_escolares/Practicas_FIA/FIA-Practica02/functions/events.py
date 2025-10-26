def advance(current_position, direction, matrix_map):
    
    x = current_position['x']
    y = current_position['y']

    if direction == "Up":
        y = y - 1
    elif direction == "Down":
        y = y + 1
    elif direction == "Left":
        x = x - 1
    elif direction == "Right":
        x = x + 1

    if 0 <= y < len(matrix_map) and 0 <= x < len(matrix_map[0]) and matrix_map[y][x] != 0:
        if matrix_map[y][x] != 0:
            if matrix_map[y][x] == 3:
                print("Salida encontrada")
            return {'x':x, 'y':y}      
    
    return current_position
        