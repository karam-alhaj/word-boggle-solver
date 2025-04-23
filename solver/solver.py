from .matrix_to_graph import matrix_to_graph
from .search import dfs

def search_for_words(matrix)-> dict:

    '''
        Search for words in a matrix using depth-first search (DFS).
        Parameters:
            matrix: list[list[str]]: The input matrix to search for words.
        Returns: 
            letter_locations: dict: A dictionary where the keys are words found in the matrix and the values are lists of coordinates (i,j) where the letters of the word are located.
        Example:
            >>> search_for_words([['a','b','c'],['d','f','g'],['h','g','k']])
            {'abc': [['0,0', '0,1', '0,2']], 'fg': [['1,1', '1,2']], 'gk': [['2,1', '2,2']], 'hgf': [['2,0', '2,1', '1,1']], 'd': [['1,0']]}

    '''


    def is_in_dict(word):
        '''
            check if the word is in the dictionary.
            Parameters:
                word: str: The word to check.
            Returns:
                bool: True if the word is in the dictionary, False otherwise.
            Example:
                >>> is_in_dict('abc')
                True
        '''
        with open('solver/words/words.txt', 'r') as f:
            words = f.read().splitlines()
            return (word in words)
        
    letter_locations = {}    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            search = dfs(matrix_to_graph(matrix), f'{i},{j}', visited=None, res=[])
            word = ''
            for search_loc in range(len(search)):
                loc = [int(k) for k in search[search_loc].split(',')]
                word += matrix[loc[0]][loc[1]]
                if len(word) > 2:
                    # Check if the word is in the dictionary
                    if is_in_dict(word):
                        if word not in letter_locations:
                            letter_locations[word] = [search[:search_loc+1]]


    return letter_locations

def main():
    print('hi')

if __name__ == '__main__':
    main()