def es_sudoku_correcto(sudoku):
    # Verificar filas y columnas
    for i in range(9):
        if len(set(sudoku[i])) != 9 or len(set(sudoku[j][i] for j in range(9))) != 9:
            return False

    # Verificar subgrids 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [sudoku[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if len(set(subgrid)) != 9:
                return False

    # Si todas las verificaciones son correctas, el Sudoku es válido
    return True

# Ejemplo de uso
sudoku_resuelto = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

if es_sudoku_correcto(sudoku_resuelto):
    print("El Sudoku es correcto.")
else:
    print("El Sudoku no es correcto.")
