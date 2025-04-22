from ui import ui
from solver.matrix_to_graph import matrix_to_graph
from solver import solver


def main(matrix:list[list[str]],looper):
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

# n_words, locations in enumerate(letter_locations.items())



def binder(event,i):
    if event.keysym == 'space':
        ui.canvas.delete('all')
        main([['a','b','c'],['d','m','a'],['a','r','k']],i[0])
        print(i)
        i[0]+=1
        


# created this boilerplate to insure that if I imported the file by mistake the function doesn't run   
if __name__ == '__main__':
    # main([['a','b','c'],['d','m','a'],['a','r','k']],0)
    i = [0] #made it a list to be passed by refrenced there is a better way but I'm too burntout to think about it
    ui.root.bind('<KeyRelease>', lambda event: binder(event,i))
    ui.root.mainloop()