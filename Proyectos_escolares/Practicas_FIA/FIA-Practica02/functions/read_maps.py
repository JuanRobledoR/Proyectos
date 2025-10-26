from pathlib import Path

def Rout(name):
    pass

def Read():
    script_location = Path(__file__).resolve()
    project_root = script_location.parent.parent
    map_path = project_root / 'maps' / 'mapa.txt'

    try:
        with open(map_path, 'r') as map_file:
            content = map_file.read()
            print(content)
    except FileNotFoundError:
        print(f"No se encontró un mapa en la ruta: {map_path}")

    return content

def Convert_matrix(content):
    line_list = content.splitlines()
    matrix = []

    for line in line_list:
        row_string = line.split(',')

        row_int = []

        for number in row_string:
            row_int.append(int(number))

        matrix.append(row_int)

    return matrix
        
        

