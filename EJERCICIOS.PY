def calcularErrorCuadratico (a,b):
    e=[]
    n=len(a)
    m=len(b)
    for i in range(n):
        suma=0
        for j in range(m):
            resta=a[i][j]-b[j]
            suma=suma+resta**2
        mse=suma / m
        e.append([mse])
    return e

def buscarFila(a,b):
     n=len(a)
     for i in range(n):
        if a[i] == b:
             return True
     return False
def BuscarFIla1(a,b):
    for i in a:
        if i==b:
             return True
    return False


def BuscarColumna(a,c):
    n=len(a)
    m=len(a[0])
    for j in range(m):           
        es_igual = True          
        for i in range(n):       
            if a[i][j] != c[i][0]:
                es_igual = False
                break
        if es_igual:
            return True          
    return False  

def BuscarEnFilas (a,d):
    n=len(a)
    m=len(a[0])
    k=len(d)
    for i in range (n):
        for j in range(m-k+1):
            segmento=a[i][j:j+k]
            if segmento==d:
                return True
    return False
def buscarEnColumnas(a, f):
    n = len(a)       
    m = len(a[0])     
    k = len(f)       

    for j in range(m): 
        for i in range(n - k + 1):  
            segmento = [a[i + t][j] for t in range(k)]
            vectorb = [f[t][0] for t in range(k)]
            if segmento == vectorb:
                return True
    return False

def SumarSoloPares(a, h):
    n = len(a)
    m = len(a[0])
    z = []
    for i in range(n):
        fila = []
        for j in range(m):
            if a[i][j] % 2 == 0 :
                par1 = a[i][j] 
                par2 = h[i][j]
                suma = par1 + par2
                fila.append(suma)
            else :
                fila.append(0)  
        z.append(fila)
    return z    
def sumarLimitado(a, h):
    n = len(a)
    m = len(a[0])
    z = []
    for i in range(n):
        fila = []
        for j in range(m):
            par1 = a[i][j] 
            par2 = h[i][j]
            if par1+par2<10:
                suma = par1 + par2
                fila.append(suma)
            else :
                fila.append(10) 
        z.append(fila)
    return z  
def ContarRepeticiones(a,x):
    n=len(a)
    m=len(a[0])
    cont=0
    for i in range(n):
        for j in range(m):
            if x==a[i][j]:
                cont=cont+1
    return cont


def intercambiarFilas(a, k, l):
    if k < len(a) and l < len(a): 
        a[k], a[l] = a[l], a[k]
    return a


def intercambiarColumnas(a, k, l):
    n = len(a)
    m = len(a[0])
    if k < m and l < m: 
        for i in range(n):
            a[i][k], a[i][l] = a[i][l], a[i][k]
    return a

def CrearFormato(d):
    a=[]
    l=d//2
    for i in range(d):
        a.append([0]*d)
        for j in range(d):
            for k in range(d):
                if (i < l  and j >= l) or (i >= l and j < l) :
                    a[i][j]=1
    return a

def CrearFormato1(d):
    a=[]
    cont=1
    for i in range(d):
        fila=[]
        for j in range(d):
            fila.append(cont)
            cont=cont+1
        a.append(fila)
    return a
def CrearFormato2(d):
    a=[]
    for i in range(d):
        fila=[]
        for j in range(d):
            if i==j or j==d-i-1:
                fila.append(i+1)
            elif abs(i-j)==1 or abs((d-i-1)-j)==1:
                fila.append(0)
            else:
                fila.append(1)         
        a.append(fila)
    return a

def copiarFilasImpares(a):
    n=len(a)
    m=len(a[0])
    z=[]
    for i in range(n):
        suma=0
        for j in range(m):
            suma=a[i][j]
        if suma%2!=0:
            z.append(a[i])
    return z
def copiaMayores(a,c):
    n=len(a)
    m=len(a[0])
    z=[]
    for i in range(n):
        for j in range(m):
            if c<a[i][j]:
                z.append(a[i][j])
    return z

def CrearFormato4(d):
    a=[]
    p=d//2
    for i in range(d):
        fila=[]
        for j in range(d):
            fila.append(0)     
        a.append(fila)
    for k in range(d):
        for l in range(d): 
                if k<p :
                    if l>=p:
                        a[k][l]=2   
                if k>=p :
                    if l<p:
                        a[k][l]=3
                if k==l:
                    a[k][l]=1
                if k<p and l<p:
                    if k>=l:
                        a[k][l]=1
                if k>=p and l>=p:
                    if k>=l:
                        a[k][l]=1      
    return a
def CrearFormato5(d):
    a=[]
    p=d//2
    for i in range(d):
        fila=[]
        for j in range(d):
            fila.append(0)
        a.append(fila)
    for k in range(d):
        for l in range(d):
            if k<p and l<p:
                if k==l:
                    a[k][l]=1
            if k>=p :
                if l<p:
                    a[k][l]=1
            if k<p and l>=p:
                if  k==(p-1-(l-p)):
                    a[k][l]=1
    return a
def CrearFormato6(d):
    a=[]
    p=d//2
    for i in range(d):
        fila=[]
        for j in range(d):
            fila.append(0)
        a.append(fila)
    for k in range(d):
        for l in range(d):
            if k<p and l<p:
                a[k][l]=1
            if k<p and l>=p:
                a[k][l]=2
            if k>=p and l<p:
                a[k][l]=3
            if k>=p and l>=p:
                a[k][l]=4

    return a
def CrearFormato7(d):
    a=[]
    p=d//2
    for i in range(d):
        fila=[]
        for j in range(d):
            fila.append(0)
        a.append(fila)
    for k in range(d):
        for l in range(d):
            if k+l==(d-1):
                a[k][l]=2
            if k<p and l<p:
                if k%2==0 and l%2==0:
                        a[k][l]=1
                if k%2!=0 and l%2!=0:
                        a[k][l]=1
            if k>=p and l>=p:
                if k%2==0 and l%2==0:
                        a[k][l]=1
                if k%2!=0 and l%2!=0:
                        a[k][l]=1
    return a
def CrearFormato8(d):
    a=[]
    p=d//2
    for i in range(d):
        fila=[]
        for j in range(d):
            fila.append(0)
        a.append(fila)
    for k in range(d):
        for l in range(d):
            if k<p and l<p:
                if k%2==0:
                    a[k][l]=1
            if k>=p and l>=p:
                if k%2==0:
                    a[k][l]=1
            if k<p and l>=p:
                if l%2==0:
                    a[k][l]=2
            if k>=p and l<p:
                if l%2==0:
                    a[k][l]=2
    return a
def MultiplicarMatrices(a,b):
    c=[]
    n=len(a)
    m=len(a[0])
    z=len(b[0])
    for i in range(n):
        fila=[]
        for j in range(z):
            fila.append(0)
        c.append(fila)

    for k in range(n):
        for l in range(z):
            for d in range(m):
                c[k][l]+=a[k][d]*b[d][l]
 
    return c
def EstriDiagonoal(a):
    n=len(a)
    m=len(a[0])
    for i in range(n):
        for j in range(m):
            if abs(i-j)>1  and a[i][j]!=0:
                return False

    return True 
def EstriangularSuperior(a):
    n=len(a)
    m=len(a[0])
    for i in range(n):
        for j in range(m):
            if i>j and a[i][j]!=0:
                return False
    return True
def CalcularFrecuencia(a):
    fila = a[0]         
    unicos = []
    frecuencia = []

    for valor in fila:  
        if valor not in unicos:
            unicos.append(valor)
            cont = 0
            for x in fila:
                if x == valor:
                    cont += 1
            frecuencia.append(cont)

    b = [unicos, frecuencia]
    return b
def relMSE(a, c, b):
    n = len(a)
    m = len(a[0])
    e = []

    for i in range(n):
        mseA = 0
        for j in range(m):
            mseA += (a[i][j] - b[0][j]) ** 2
        mseA = mseA / m
        mseC = 0
        for j in range(m):
            mseC += (c[i][j] - b[0][j]) ** 2
        mseC = mseC / m
        rel = mseA / mseC
        e.append(rel)

    return e
def Remplazar(a,b,c):
    n=len(a)
    m=len(a[0])
    k=len(b)
    for i in range(n):
        for j in range(m):
            segmento=a[i][j:j+k]
            if segmento==b:
                a[i][j:j+k]=c
    return a

def SubMatriz(a,b):
    n=len(a)
    m=len(a[0])
    k=len(b)
    l=len(b[0])
    for i in range(n-k+1):
        for j in range(m-l+1):
            segmento=[]
            for fi in range(i,i+k):
                fila=[]
                for col in range(j,j+l):
                    fila.append(a[fi][col])
                segmento.append(fila)
            if segmento== b:
                return True
    return False
def BuscarSubmatrizConTolerancia(a, b):
    n = len(a)
    m = len(a[0])
    k = len(b)
    l = len(b[0])

    for i in range(n - k + 1):
        for j in range(m - l + 1):
            segmento = []

            for fi in range(i, i + k):
                fila = []
                for col in range(j, j + l):
                    fila.append(a[fi][col])
                segmento.append(fila)

            diferencias = 0
            for fi in range(k):
                for col in range(l):
                    if segmento[fi][col] != b[fi][col]:
                        diferencias += 1

            if diferencias <= 1:
                return True
    return False
def buscarSubmatrizCon1Rotacion(A, B):
    n = len(A)
    m = len(A[0])
    a = len(B)
    b = len(B[0])

    for i in range(n - a + 1):
        for j in range(m - b + 1):
            sub = []
            for x in range(a):
                fila = A[i + x][j:j + b]
                sub.append(fila)
            if sub == B:
                return True

    filas = len(B)
    columnas = len(B[0])
    B_rotada = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas - 1, -1, -1):
            nueva_fila.append(B[i][j])
        B_rotada.append(nueva_fila)

    a_rot = len(B_rotada)
    b_rot = len(B_rotada[0])

    for i in range(n - a_rot + 1):
        for j in range(m - b_rot + 1):
            sub = []
            for x in range(a_rot):
                fila = A[i + x][j:j + b_rot]
                sub.append(fila)
            if sub == B_rotada:
                return True

    return False
a=[
   [5,3,8,7],
   [9,5,4,4],
   [2,1,8,4]
   ]
h=[
   [2,3,5,8],
   [7,8,4,1],
   [1,2,6,8]
]

b=[9,5,4,4]

c=[
  [3],
  [5],  
  [1]
]
d=[8,4]


g=[
    [4],
    [5]
]

y=[
   [5,3,8],
   [9,5,4],
   [2,1,8]
]
u=[
   [2,3,5],
   [7,8,4],
   [1,2,6]
]
i=[
    [1,2,0,0,0],
    [2,5,6,0,0],
    [0,4,2,7,0],
    [0,0,2,1,1],
    [0,0,0,3,2]
]
ñ=[
    [5,6,1],
    [0,4,6],    
    [0,0,1]
]
j=[[1,2,1,3,4,2,7,5]]


A = [
    [2, 3, 4],
    [1, 5, 7]
]

C = [
    [1, 3, 5],
    [2, 5, 6]
]

B = [[2, 4, 6]]

D=[
    [1,2,3,4],
    [4,1,2,5],
    [3,2,6,7],
    [1,2,8,9]
]
E=[1,2]
F=[8,9]
H=[
    [0,0,0,0,0],
    [0,1,1,0,0],
    [0,3,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
]
I=[
    [3,1],
    [1,1]
]
e=calcularErrorCuadratico(a,b)
print("matris e:")
for f in e:
    print(f)
ej2=buscarFila(a,b)
print(ej2)
ej3=BuscarFIla1(a,b)
print(ej3)
ej4=BuscarColumna(a,c)
print(ej4)
ej5=BuscarEnFilas(a,d)
print(ej5)
ej6=buscarEnColumnas(a,g)
print(ej6)
ej7=SumarSoloPares(a,h)
print(ej7)
ej8=sumarLimitado(a,h)
print(ej8)
ej9=ContarRepeticiones(a,5)
print(ej9)
ej10=intercambiarFilas(a,0,1)
print(ej10)
ej11=intercambiarColumnas(a,0,1)
print(ej11)
ej12=CrearFormato(6)
print(ej12)
ej13=CrearFormato1(3)
print(ej13)
ej14=CrearFormato2(7)
print(ej14)
ej15=copiarFilasImpares(a)
print(ej15)
ej16=copiaMayores(a,4)
print(ej16)
ej17=CrearFormato4(10)
print(ej17)
ej18=CrearFormato5(6)
print(ej18)
ej19=CrearFormato6(6)
print(ej19)
ej20=CrearFormato7(8)
print(ej20)
ej21=CrearFormato8(8)
print(ej21)  
ej22=MultiplicarMatrices(y,u)
print(ej22)
ej23=EstriDiagonoal(i)
print(ej23)
ej24=EstriangularSuperior(ñ)
print(ej24)
ej25=CalcularFrecuencia(j)
print(ej25)
ej26=relMSE(A,C,B)
print(ej26)
ej27=Remplazar(D,E,F)
print(ej27)
ej28=SubMatriz(H,I)
print(ej28)
ej29=BuscarSubmatrizConTolerancia(H,I)
print(ej29)
ej30=buscarSubmatrizCon1Rotacion(H,I)
print(ej30)

