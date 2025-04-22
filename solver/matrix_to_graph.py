def matrix_to_graph(matrix:list[list[str]])->dict:
    '''
        Convert a matrix to a graph representation.

        Parameters:
            matrix: list[list[str]]: The input matrix to be converted.

        Returns:
            graph: dict: A dictionary representing the graph, where each key is a node (i,j) and the value is a tuple containing the letter at that position and its neighbours.
        
        Example:
                >>> matrix_to_graph([['a','b','c'],['d','f','g'],['h','g','k']])
                {'0,0': ('a', ['0,1', '1,0', '1,1']), '0,1': ('b', ['0,0', '0,2', '1,0', '1,1', '1,2']), '0,2': ('c', ['0,1', '1,1', '1,2']),
                '1,0': ('d', ['0,0', '0,1', '1,1', '2,0', '2,1']), '1,1': ('f', ['0,0', '0,1', '0,2', '1,0', '1,2', '2,0', '2,1', '2,2']),
                    '1,2': ('g', ['0,1', '0,2', '1,1', '2,1', '2,2']), '2,0': ('h', ['1,0', '1,1', '2,1']), '2,1': ('g', ['1,0', '1,1', '1,2', '2,0', '2,2']),
                    '2,2': ('k', ['1,1', '1,2', '2,1'])}

    '''
    def get_neighbours(i,j)->list:
        n = []
        for x in (-1,0,1):
            for y in (-1,0,1):
                if x==y  and x==0: 
                    continue
                elif i+x > (len(matrix)-1) or i+x < 0:
                    continue
                elif (j+y > (len(matrix[0])-1) ) or j+y < 0:
                    continue
                else:
                    # I appended the coordinates of the neighbours to the list because the letters are not unique and this may lead unwanted behaviour
                    n.append(f'{x+i},{y+j}')
        return n

    graph = {}

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            neighbours = get_neighbours(i,j)
            graph[f'{i},{j}'] = (matrix[i][j],neighbours)
    return graph

def main():
    print(matrix_to_graph([['a','b','c'],['d','f','g'],['h','g','k']]))

# again, I want the main function to run only when I'm testin (running the file directly). 
if __name__ == '__main__':
    main()