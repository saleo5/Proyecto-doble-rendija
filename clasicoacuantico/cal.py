import cal_matrix_cpmx as cal_co

#vec = [2-1j, 2j, 1-1j, 1, -2j, 2]
#val = 2-1j
#rest = (val)**2
vec = [-3-1j,-2j,1j,2]

def normal(vec):
    suma = 0
    for i in range(len(vec)):
        #print("resultado:",vec[i]**2)
        suma+=abs(vec[i])**2
    return suma**0.5

def module(vec):
    return vec.real**2 + vec.imag**2

def normalizar(vec):
    nor = normal(vec)
    for i in range(len(vec)):
        vec[i] = vec[i]/nor
    return vec

def propabi(vec,pos):
    x = vec[pos]
    val = abs(x)**2
    prope = normal(vec)
    #print(val)
    #print(prope)
    return val/prope**2

def transicion(vec1,vec2):
    re = cal_co.produc_interno_vec(vec2,vec1)
    b = re/(normal(vec1))*(normal(vec2))
    return module(b)

#vec1 = [((2**0.5)*1j)/2,(((2**0.5)*-1)/2)]
#vec2 = [((2**0.5)*1)/2,(((2**0.5)*-1j)/2)]
vec = [2+1j,-1+2j,1j,1,3-1j,2,-2j,-2+1j,1-3j,-1j]


#print(transicion(vec1,vec2))

aux = []
for i in range(0,len(vec)):
    aux.append(round(propabi(vec,i)*100,2))
for j in range(len(aux)):
    print(aux[j])