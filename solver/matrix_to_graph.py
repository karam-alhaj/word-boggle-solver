def matrix_to_graph(matrix:list[list[str]])->dict:
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