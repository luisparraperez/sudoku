class sudoku:
    def __init__(self,array):
        self.array=array
    def validaFila(self,i,valor):
        for j in range(9):
            if self.array[i][j] == valor:
                return False
        return True
    def validaColumna(self,j,valor):
        for i in range(9):
            if self.array[i][j]==valor:
                return  False
        return True
    def retornaInicial(self,posicion):
        if posicion >=0 and posicion <=2:
            return 0
        elif posicion >=3 and posicion <=5:
            return 3
        else:
            return 6
    def validaTresXTres(self,i,j,valor):
        init = self.retornaInicial(i)
        fin = self.retornaInicial(j)
        for ix in range(init,init+3):
            for jx in range(fin,fin+3):
                if self.array[ix][jx] == valor:
                    return False
        return True
        
    def resolver(self):
        print self.array
array =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
print sudoku(array).validaTresXTres(8,8,6)

        
