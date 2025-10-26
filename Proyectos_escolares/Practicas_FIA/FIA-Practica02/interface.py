import tkinter as tk
import functions
from collections import deque

class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Ventana")
        self.geometry("1200x700")

        maptxt = functions.Read()
        self.matrix_map = functions.Convert_matrix(maptxt)
        self.blind_matrix_map = self.blind_matrix()
        self.height = len(self.matrix_map)
        self.width = len(self.matrix_map[0]) if self.height > 0 else 0

        #MAP CONFIG
        self.CELL_SIZE = 40
        self.COLORS = {
            0: 'black',
            1: 'white',
            2: 'red',
            3: 'blue',
            4: 'green',
            9: 'purple'
        }

        self.canvas_map = tk.Canvas(self, width=600, height=600, bg='grey')
        self.canvas_map.pack(side=tk.LEFT, padx=10, pady=10)

        self.canvas_tree = tk.Canvas(self, width=600, height=600, bg='grey')
        self.canvas_tree.pack(side=tk.RIGHT, padx=10, pady=10)

        # -------------------------------------------------------------- #
        self.start_tuple, self.end_tuple = self.priority()

        if self.start_tuple is None or self.end_tuple is None:
            print("Error: No se encontró un punto de inicio (2) o de fin (3).")
            return

        start_x, start_y = self.start_tuple
        self.blind_matrix_map[start_y][start_x] = 2

        # ---------------------------------- #
        self.stack = [(self.start_tuple, [])]
        self.queue = deque([(self.start_tuple, [])])
        self.visited = {self.start_tuple}
        self.last_position = None
        # ---------------------------------- #
        
        self.parent_map = {self.start_tuple: (None, None)} 
        self.NODE_RADIUS = 12

        self.algorithm = 2
        self.animation()
        
    def draw_map(self):
        self.canvas_map.delete("all")

        for y, row in enumerate(self.blind_matrix_map):
            for x, cell in enumerate(row):
                x0 = x * self.CELL_SIZE
                y0 = y * self.CELL_SIZE
                x1 = x0 + self.CELL_SIZE
                y1 = y0 + self.CELL_SIZE

                color = self.COLORS.get(cell, 'red')
                self.canvas_map.create_rectangle(x0,y0,x1,y1, fill=color, outline='grey')


    def blind_matrix(self):
        height = len(self.matrix_map)
        width = len(self.matrix_map[0]) if height > 0 else 0
        blind_matrix_map = [[9] * width for _ in range(height)]
        return blind_matrix_map
                
    def priority(self):
        start_node = None
        end_node = None
        for y, row in enumerate(self.matrix_map):
            for x, cell in enumerate(row):
                if cell == 2:
                    start_node = (x, y)
                elif cell == 3:
                    end_node = (x, y)
        return start_node, end_node


    def _get_node_label(self, node_coords):
        if node_coords is None:
            return ""
        x, y = node_coords
        letter = chr(ord('A') + x)
        row = y + 1
        return f"{row}{letter}"

    def draw_tree(self):
        self.canvas_tree.delete("all")
        if not self.parent_map:
            return

        children_map = {node: [] for node in self.visited}
        for child, (parent, action) in self.parent_map.items():
            if parent is not None:
                children_map[parent].append((child, action))

        node_positions = {}
        queue = deque([(self.start_tuple, 0)]) #nodo,profundidad
        
        nodes_at_depth = {0: [self.start_tuple]}
        
        visited_for_drawing = {self.start_tuple}

        while queue:
            current_node, depth = queue.popleft()
            
            sorted_children = sorted(children_map.get(current_node, []), key=lambda item: item[0])
            
            for child, action in sorted_children: 
                if child not in visited_for_drawing:
                    visited_for_drawing.add(child)
                    
                    new_depth = depth + 1
                    if new_depth not in nodes_at_depth:
                        nodes_at_depth[new_depth] = []
                    nodes_at_depth[new_depth].append(child)
                    
                    queue.append((child, new_depth))
        
        canvas_w = self.canvas_tree.winfo_width()
        canvas_h = self.canvas_tree.winfo_height()
        
        max_depth = max(nodes_at_depth.keys()) if nodes_at_depth else 0
        y_spacing = canvas_h / (max_depth + 2.5) if max_depth > 0 else canvas_h / 2

        for depth, nodes in nodes_at_depth.items():
            x_spacing = canvas_w / (len(nodes) + 1)
            for i, node in enumerate(nodes):
                x_pos = (i + 1) * x_spacing
                y_pos = (depth + 1) * y_spacing
                node_positions[node] = (x_pos, y_pos)

        for node, children_with_actions in children_map.items():
            if node not in node_positions: continue
            x1, y1 = node_positions[node]
            
            for child, action in children_with_actions:
                if child not in node_positions: continue
                x2, y2 = node_positions[child]
                
                self.canvas_tree.create_line(x1, y1, x2, y2, fill='black')
                
                x_mid = (x1 + x2) / 2
                y_mid = (y1 + y2) / 2
        
                self.canvas_tree.create_text(x_mid, y_mid - 10, text=action, 
                                             fill='blue', font=("Arial", 9, "bold"))

        for node, pos in node_positions.items():
            x, y = pos
            fill_color = 'skyblue'
            if node == self.last_position: fill_color = 'red'
            if node == self.end_tuple: fill_color = 'green'
            
            self.canvas_tree.create_oval(x - self.NODE_RADIUS, y - self.NODE_RADIUS,
                                         x + self.NODE_RADIUS, y + self.NODE_RADIUS,
                                         fill=fill_color, outline='black')
            
            label = self._get_node_label(node)
            self.canvas_tree.create_text(x, y, text=label, font=("Arial", 8, "bold"))


    def animation(self):
        # -------------------------------------------------------------- #

        if self.algorithm == 1:
            if not self.stack:
                print("Búsqueda terminada (DFS). No se encontró el objetivo.")
                self.draw_tree()
                return

            (current_x, current_y), path = self.stack.pop()

        elif self.algorithm == 2:
            if not self.queue:
                print("Búsqueda terminada (BFS). No se encontró el objetivo.")
                self.draw_tree()
                return
            (current_x, current_y), path = self.queue.popleft()


        
        if self.last_position:
            last_x, last_y = self.last_position
            if self.blind_matrix_map[last_y][last_x] == 2:
                self.blind_matrix_map[last_y][last_x] = 4

        self.blind_matrix_map[current_y][current_x] = 2
        self.last_position = (current_x, current_y)

        for i in range(-1, 2):
            for j in range(-1, 2):
                y, x = current_y + i, current_x + j
                if 0 <= y < self.height and 0 <= x < self.width:
                    if self.blind_matrix_map[y][x] not in [2, 4]:
                        self.blind_matrix_map[y][x] = self.matrix_map[y][x]

        
        self.draw_map()

        if (current_x, current_y) == self.end_tuple:
            print(f"Objetivo encontrado. Camino: {path}")
            self.draw_tree()
            return

        
        moves = [("B", 0, 1), ("D", 1, 0), ("I", -1, 0), ("A", 0, -1)]
        
        for direction, dx, dy in moves:
            next_x, next_y = current_x + dx, current_y + dy
            next_pos = (next_x, next_y)
            
            if (0 <= next_x < self.width and
                0 <= next_y < self.height and
                self.matrix_map[next_y][next_x] != 0 and
                next_pos not in self.visited):
                

                self.parent_map[next_pos] = ((current_x, current_y), direction) 
                self.visited.add(next_pos)

                if self.algorithm == 1:
                    self.stack.append((next_pos, path + [direction]))
                elif self.algorithm == 2:
                    self.queue.append((next_pos, path + [direction]))
                
        
        self.after(200, self.animation)
        # -------------------------------------------------------------- #
