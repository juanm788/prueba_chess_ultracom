# -- coding: utf-8 --

import numpy as np

MATRIX_SIZE = 8
ITEM_POSITION_NUMBER = 8

starting_matrix = np.zeros((MATRIX_SIZE, MATRIX_SIZE), dtype=int)
    """
    Parametros
            ----------
            MATRIX_SIZE : positive int
                Tamaño definido para la matriz.
            
            ITEM_POSITION_NUMBER :   
                Número definifo para graficar la posición de la ficha.

        """

x = input(""" Tomando como referencia la siguiente:
                              _ _ _ _ _ _ _ _
                        ...  |_|_|_|_|_|_|_|_|7 ...
                        ...  |_|_|_|_|_|_|_|_|6 ...
                        ...  |_|_|_|_|_|_|_|_|5 ...
                        ...  |_|_|_|_|_|_|_|_|4 ...
                        ...  |_|_|_|_|_|_|_|_|3 ...
                        ...  |_|_|_|_|_|_|_|_|2 ...
                        ...  |_|_|_|_|_|_|_|_|1 ...
                        ...  |_|_|_|_|_|_|_|_|0 ...
                        

Ingrese un numero  entero  0 y 7 para seleccionar la posición en la fila que desea    : """)

y = input(""" Tomando como referencia la siguiente:
                              _ _ _ _ _ _ _ _
                        ...  |_|_|_|_|_|_|_|_| ...
                        ...  |_|_|_|_|_|_|_|_| ...
                        ...  |_|_|_|_|_|_|_|_| ...
                        ...  |_|_|_|_|_|_|_|_| ...
                        ...  |_|_|_|_|_|_|_|_| ...
                        ...  |_|_|_|_|_|_|_|_| ...
                        ...  |_|_|_|_|_|_|_|_| ...
                        ...  |_|_|_|_|_|_|_|_| ...
                              0 1 2 3 4 5 6 7 
          
Ingrese un numero  entero  0 y 7 para seleccionar la posición en la columna que desea : """)
x = int(x)
y = int(y)

def build_rook_positions(matrix, x_position, y_position):
    rook_positions_matrix = matrix

    for index, number in enumerate(rook_positions_matrix[x_position, :]):
        if number != ITEM_POSITION_NUMBER:
            rook_positions_matrix[x_position][index] = 1

    for index, number in enumerate(rook_positions_matrix[:, y_position]):
        if number != ITEM_POSITION_NUMBER:
            rook_positions_matrix[index][y_position] = 1

    return rook_positions_matrix

    """ Movimiento para la ficha rook:
                En la que con el número 1 definimos los movimientos en la fila y la columna en dónde se ubica la ficha.
                    
    Parametros
            ----------
            MATRIX_SIZE : positive int
                Tamaño definido para la matriz.
            
            ITEM_POSITION_NUMBER :   
                Número definifo para graficar la posición de la ficha.

            x_position : positive int
                Posición de la ficha rook en la fila
            
            y_position : positive int   
                Posición de la ficha rook en la Columna
        """    


def build_bishop_positions(matrix, x_position, y_position):
    bishop_positions_matrix = matrix

    for i in range(MATRIX_SIZE):
        rows_difference = x_position - i
        for j in range(MATRIX_SIZE):
            if j == y_position - rows_difference and bishop_positions_matrix[i][j] != ITEM_POSITION_NUMBER:
                bishop_positions_matrix[i][j] = 1

            if j == y_position + rows_difference and bishop_positions_matrix[i][j] != ITEM_POSITION_NUMBER:
                bishop_positions_matrix[i][j] = 1

    return bishop_positions_matrix

    """ Movimiento para la ficha bishop:
                En la que con el número 1 definimos los en diagonal en dónde se ubica la ficha.
                    
    Parametros
            ----------
            MATRIX_SIZE : positive int
                Tamaño definido para la matriz.
            
            ITEM_POSITION_NUMBER :   
                Número definifo para graficar la posición de la ficha.

            rows_difference : Es la diferencia entre la posición de la ficha con el margen para poder cumplir la condión 
                                de soólo graficar las diagonales.
        """    


def build_king_positions(matrix, x_position, y_position):
    king_positions_matrix = matrix

    for i in range(MATRIX_SIZE):


        for j in range(MATRIX_SIZE):
            if(x_position >= -1)and (x_position <= MATRIX_SIZE) and (y_position >= -1)and (y_position <= MATRIX_SIZE):
                if (i >= x_position - 1) and (i <= x_position + 1) and (j >= y_position - 1)and (j <= y_position + 1) and (king_positions_matrix[i][j] != ITEM_POSITION_NUMBER):
                    king_positions_matrix[i][j] = 1
                else:
                    None

    return king_positions_matrix

    """ Movimiento para la ficha king:
                En la que definimos el movimiento que puede tener la ficha king que está definido como la posición inmediata
                  tanto en izquierda , derecha como arriba con sus respectivas diagonales inmediatas dentro de los margenes de la matriz.  
    Parametros
            ----------
            MATRIX_SIZE : positive int
                Tamaño definido para la matriz.
            
            ITEM_POSITION_NUMBER :   
                Número definifo para graficar la posición de la ficha.

            x_position : positive int
                Posición de la ficha king en la fila
            
            y_position : positive int   
                Posición de la ficha king en la Columna
        
        """ 

def build_pawnd_positions(matrix, x_position, y_position):
    pawnd_positions_matrix = matrix

    for i in range(MATRIX_SIZE):
    

        for j in range(MATRIX_SIZE):
            if(x_position >= -1)and (x_position <= MATRIX_SIZE) and (y_position >= -1)and (y_position <= MATRIX_SIZE):
                if (i >= x_position ) and (i <=  x_position + 1) and (j >= y_position)and (j <= y_position) and (pawnd_positions_matrix[i][j] != ITEM_POSITION_NUMBER):
                    pawnd_positions_matrix[i][j] = 1
                else:
                    None

    return pawnd_positions_matrix

def build_pawn_positions(matrix, x_position, y_position):
    pawn_positions_matrix = matrix

    for i in range(MATRIX_SIZE):
    

        for j in range(MATRIX_SIZE):
            if(x_position >= -1)and (x_position <= MATRIX_SIZE) and (y_position >= -1)and (y_position <= MATRIX_SIZE):
                if (i >= x_position -1) and (i <= x_position ) and (j >= y_position)and (j <= y_position) and (pawn_positions_matrix[i][j] != ITEM_POSITION_NUMBER):
                    pawn_positions_matrix[i][j] = 1
                else:
                    None

    return pawn_positions_matrix

    """ Movimiento para la ficha pawn:
                Para la ficha pawn definí las condiciones para qué sólo se pueda la ficha se mueva ya sea una posición arriba o una abajo
                para la ficha pawnd(Depende del sentido en el que se posicione el jugador).  
    Parametros
            ----------
            MATRIX_SIZE : positive int
                Tamaño definido para la matriz.
            
            ITEM_POSITION_NUMBER :   
                Número definifo para graficar la posición de la ficha.

            x_position : positive int
                Posición de la ficha pawn y pawd en la fila
            
            y_position : positive int   
                Posición de la ficha pawn y pawd  en la Columna
        
        """ 
def build_queen_positions(matrix, x_position, y_position):
    queen_mat = build_bishop_positions(np.array(matrix), x_position, y_position) + build_rook_positions(np.array(matrix), x_position, y_position)

    if queen_mat[x][y] == ITEM_POSITION_NUMBER * 2:
        queen_mat[x][y] = ITEM_POSITION_NUMBER

    return queen_mat

    
    """ Movimiento para la ficha queen:
                Realizo una sobreposición de matrices utilizando la matriz construida para rook y la matriz construida para bishop.
    Parametros
            ----------
            MATRIX_SIZE : positive int
                Tamaño definido para la matriz.
            
            ITEM_POSITION_NUMBER :   
                Número definifo para graficar la posición de la ficha.

            queen_mat[x][y] :
                Es la ubicación de la ficha en el tablero.
            
        
        """ 
def build_knight_positions(matrix, x_position, y_position):
    knight_positions_matrix = matrix

    for i in range(MATRIX_SIZE):

        for j in range(MATRIX_SIZE):
            if knight_positions_matrix[i][j] == ITEM_POSITION_NUMBER:
                continue

            is_upper_right = (x_position - 2 == i) and (y_position + 1 == j)
            is_up_righter = (x_position - 1 == i) and (y_position + 2 == j)
            is_upper_left = (x_position - 2 == i) and (y_position - 1 == j)
            is_up_lefter = (x_position - 1 == i) and (y_position - 2 == j)

            is_lower_right = (x_position + 2 == i) and (y_position + 1 == j)
            is_below_righter = (x_position + 1 == i) and (y_position + 2 == j)
            is_lower_left = (x_position + 2 == i) and (y_position - 1 == j)
            is_below_lefter = (x_position + 1 == i) and (y_position - 2 == j)

            is_an_up_movement = is_upper_right or is_up_righter or is_upper_left or is_up_lefter
            is_a_below_movement = is_lower_right or is_below_righter or is_lower_left or is_below_lefter

            if is_an_up_movement or is_a_below_movement:
                knight_positions_matrix[i][j] = 1

    return knight_positions_matrix
    
    """ Movimiento para la ficha knight:
               Para ésta ficha definí  parámetros y condiciones para cumplir el movimientos de izquierda,derecha,arriba y abajo para una y dos posiciones en la matriz. 
    Parametros
            ----------
            MATRIX_SIZE : positive int
                Tamaño definido para la matriz.
            
            ITEM_POSITION_NUMBER :   
                Número definifo para graficar la posición de la ficha.

            x_position : positive int
                Posición de la ficha knight en la fila
            
            y_position : positive int   
                Posición de la ficha knight en la Columna
                
            is_upper_right,is_up_righter, is_upper_left,is_up_lefter:
                Son los movimientos de la ficha en la parte superior de la posición dando saltos dobles e individuales
                
            is_lower_right,is_below_righter,is_lower_left,s_below_lefter: 
                Son los movimientos de la ficha en la parte  inferior saltos dobles e individuales    
        """        

if x >= 0 and y >= 0:
    if x < MATRIX_SIZE and y < MATRIX_SIZE:
        starting_matrix[x][y] = ITEM_POSITION_NUMBER
else:
    print ('Vuelve a digitar los valores indicados')

print('\n')
print('\n')
print('       BISHOP                ')
print(build_bishop_positions(np.array(starting_matrix), x, y))
print('\n')
print('\n')
print ('       ROOK               ')
print(build_rook_positions(np.array(starting_matrix), x, y))
print('\n')
print('\n')
print ('       QUEEN               ')
print(build_queen_positions(np.array(starting_matrix), x, y))
print('\n')
print('\n')
print ('       KING               ')
print(build_king_positions(np.array(starting_matrix), x, y))
print('\n')
print('\n')
print ('     PAWN UP             ')
print(build_pawn_positions(np.array(starting_matrix), x, y))
print('\n')
print('\n')
print ('     PAWN DOWN             ')
print(build_pawnd_positions(np.array(starting_matrix), x, y))
print('\n')
print('\n')
print ('       KNIGHT             ')
print(build_knight_positions(np.array(starting_matrix), x, y))
print('\n')

