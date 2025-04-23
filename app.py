from ui import ui
from solver.matrix_to_graph import matrix_to_graph
from solver import solver


def main(matrix:list[list[str]],looper):
    '''
        Main function to display a matrix and draw lines between cells based on the search for words.
        
        Parameters:
            matrix: list[list[str]]: The input matrix to be displayed.
            looper: int: The index used to determine which word to draw.
        
        Returns:
            None
        
        Example:
            >>> main([['a','b','c'],['d','m','a'],['a','r','k']],0)
            Displays the matrix and draws lines between cells based on the search for words.
        '''
    ui.display_matrix(matrix)
    color = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']
    letter_locations = solver.search_for_words(matrix)
    length = len(letter_locations.values())
    looper = looper % length
    locations = list(letter_locations.values())[looper][0]
    for i in range(len(locations)):
        location = locations[i]
        start = location.split(',')
        start = int(start[0]), int(start[1])

        if i+1<len(locations):
            end = locations[i+1]
            end = end.split(',')
            end = int(end[0]), int(end[1])
            ui.draw_line_between_cells(start, end,color[looper])
        else:
            ui.draw_ball_at(start[0], start[1],color[looper])

def binder(event,i):#this is used to run the main function when the space key is pressed.
    if event.keysym == 'space':
        ui.canvas.delete('all')
        main([['a','b','c'],['d','m','a'],['a','r','k']],i[0])
        print(i)
        i[0]+=1

# created this boilerplate to insure that if I imported the file by mistake the function doesn't run   
if __name__ == '__main__':
    i = [0] #made it a list to be passed by refrenced there is a better way but I'm too burntout to think about it
    ui.root.bind('<KeyRelease>', lambda event: binder(event,i))
    ui.root.mainloop()