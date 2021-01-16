"""
Clone of 2048 game.
"""

# http://www.codeskulptor.org/#user34_VxCJtOATZ8_23.py

import poc_2048_gui   
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """ 
    result = []
    for dummy_unit in range(len(line)):
        result.append(0)
        
    result_index = 0
    merged = False
    
    for cell in line:
        if cell != 0:
            
            if cell == result[result_index - 1]:
               
                if merged == False:
                    merged = True
                    result[result_index-1] = cell * 2
                                                          
                else:
                    merged = False
                    result[result_index] = cell
                    result_index += 1
                    
            else:
                result[result_index] = cell
                result_index += 1
                merged = False
        else:
            pass
        
        
    return  result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        
        up_cords = []
        down_cords = []
        left_cords = []
        right_cords = []
        
        for dummy_x in range(self.grid_width):
            up_cords.append([0,dummy_x])
    
        for dummy_y in range(self.grid_width):   
            down_cords.append([self.grid_height-1,dummy_y])
    
        for dummy_z in range(self.grid_height):
            left_cords.append([dummy_z, 0])
    
        for dummy_a in range(self.grid_height):
            right_cords.append([dummy_a, self.grid_width-1])
            
        self.move_dict = {UP:up_cords,
                          DOWN:down_cords,
                          LEFT:left_cords,
                          RIGHT:right_cords}
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self.grid = [ [0 for dummy_column in range(self.grid_width)] for dummy_row in range(self.grid_height)]
       
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for row in self.grid:
            print row

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == UP:
            list_range = self.grid_height
        elif direction == DOWN:
            list_range = self.grid_height
        elif direction == RIGHT:
            list_range = self.grid_width
        elif direction == LEFT:
            list_range = self.grid_width
            
        for intial_cell in self.move_dict[direction]:
            temp_x = intial_cell[0]
            temp_y = intial_cell[1]
            temp_list = []
            offset_tuple = OFFSETS[direction]
            for dummy_x in range(list_range):
               
                
                temp_list.append(self.grid[temp_x][temp_y])
                
                temp_x += offset_tuple[0]
                temp_y += offset_tuple[1]
            
            else:
                merged_list = merge(temp_list)
                dummy_counter = 0
                rewrite_x = intial_cell[0]
                rewrite_y = intial_cell[1]
                for dummy_x in range(list_range):
                    
                    self.grid[rewrite_x][rewrite_y] = merged_list[dummy_x]
                    
                    rewrite_x += offset_tuple[0]
                    rewrite_y += offset_tuple[1]
                    dummy_counter += 1
                
            
        else:
            self.new_tile()
                
            
               
         
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        random_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
        
        counter_x = 0
        counter_y = 0
        open_coords = []
        for list_in_grid in self.grid:
            for dummy_x in list_in_grid:
                if list_in_grid[counter_y] == 0:
                    open_coords.append([counter_x, counter_y])
                    counter_y += 1
                else:
                    counter_y += 1
            counter_x  +=1  
            counter_y = 0
        if len(open_coords) > 0:
            chosen_tile = random.choice(open_coords)
        
            dummy_x = chosen_tile[0]
            dummy_y = chosen_tile[1]
            self.grid[dummy_x][dummy_y] = random.choice(random_list)
        else:
            pass
        
            
    def set_tile(self, row, col, value):
        """
        assigns value based on row and col
        
        """
        self.grid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self.grid[row][col]
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


