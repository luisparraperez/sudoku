class sudoku:
    def __init__(self,array):
        self.array=array
        self.N=9
    def imprimeMatriz(self):
    
        for i in  self.array:
            fila="|"
            for j in i:
                fila+= str(j)+'|'
            print fila
                
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
    def validaLargoMatriz(self):
        if len(self.array) != self.N:
            return False
        for i in self.array:
            if len(i) !=self.N:
                return False
        return True
    def celdaObjetivo(self):
        
        for i in range(len(self.array)):
            for j in range(len(self.array[0])):
                if (self.array[i][j]==0):
                    return i,j
        return []
        
    def validaTodo(self,i,j,valor):
        
        return (self.validaFila(i,valor) and self.validaColumna(j,valor) and self.validaTresXTres(i,j,valor))
        
        
    def resolver(self):
        if not self.validaLargoMatriz():
            print "Matriz no respeta el formato 9x9"
            return False
        objetivo = self.celdaObjetivo()
        if objetivo==[]:
            return True
        else:
            i,j = objetivo
        for valor in range(1,self.N+1):
            if self.validaTodo(i,j,valor):
                self.array[i][j] = valor
                if(self.resolver()):
                    return True
                self.array[i][j]=0
        return False
                
        

        print "aqui empieza el mambo"
array =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

array =[[5,1,7,6,0,0,0,3,4],[2,8,9,0,0,4,0,0,0],[3,4,6,2,0,5,0,9,0],[6,0,2,0,0,0,0,1,0],[0,3,8,0,0,6,0,4,7],[0,0,0,0,0,0,0,0,0],[0,9,0,0,0,0,0,7,8],[7,0,3,4,0,0,5,6,0],[0,0,0,0,0,0,0,0,0]]
instancia = sudoku(array)
if instancia.resolver():
    print "Sudoku resuelto"
    sudoku(array).imprimeMatriz()
else:
    print "No se puede resolver sudoku"

        
