import numpy as np
def world():

    #INICIJALIZACIJA
    cilj=(2,4)
    dim=(5,5)
    prag = 0.1
    gamma = 0.9

    V = {} #VREDNOST STANJA
    for i in range(dim[0]):
        for j in range(dim[1]):
            V[(i, j)] = np.random.randint(0,4)
    V[cilj]=0


    H={} #NAGRADA
    for i in range(dim[0]):
        for j in range(dim[1]):
            for k in range(4):
                H[((i, j), k)]= 0

    #NAGRADA KADA DODJEMO DO CILJA
    H[(cilj, 0)] = 1
    H[(cilj, 1)] = 1
    H[(cilj, 2)] = 1
    H[(cilj, 3)] = 1

    #KAZNENA POLJA
    H[((0,2), 0)] = -1
    H[((0,2), 1)] = -1
    H[((0,2), 2)] = -1
    H[((0,2), 3)] = -1

    H[((3, 3), 0)] = -1
    H[((3, 3), 1)] = -1
    H[((3, 3), 2)] = -1
    H[((3, 3), 3)] = -1

    #DODAVANJE ZAMKI
    """H[((0, 3), 0)] = -100000000000000
    H[((0, 3), 1)] = -100000000000000
    H[((0, 3), 2)] = -100000000000000
    H[((0, 3), 3)] = -100000000000000

    H[((3, 4), 0)] = -100000000000000
    H[((3, 4), 1)] = -100000000000000
    H[((3, 4), 2)] = -100000000000000
    H[((3, 4), 3)] = -100000000000000"""

    old_V = {}
    for i in range(dim[0]):
        for j in range(dim[1]):
            old_V[(i, j)] = np.random.randint(0,4)


    # 0 right, 1 down, 2 left, 3 up
    #DEFINISANJE AKCIJA, KADA SMO NA IVICI NE MOZEMO DA IZADJEMO IZ SVETA
    Actions={}
    for i in range(dim[0]):
        for j in range(dim[1]):
            if i==0 and j==0:
                Actions[(i, j)] = [0, 1]
            elif i==0 and j==dim[1]-1:
                Actions[(i, j)] = [1,2]
            elif i==dim[0]-1 and j==0:
                Actions[(i, j)] = [0, 3]
            elif i==dim[0]-1 and j==dim[1]-1:
                Actions[(i, j)] = [2, 3]
            elif i==0:
                Actions[(i, j)] = [0, 1, 2]
            elif i==dim[0]-1:
                Actions[(i, j)] = [0, 2, 3]
            elif j==0:
                Actions[(i, j)] = [0, 1, 3]
            elif j==dim[1]-1:
                Actions[(i, j)] = [1, 2, 3]

            else:
                Actions[(i, j)] = [0, 1, 2, 3]



    #NOVO STANJE U KOJEM SE NADJEMO KADA SE IZVRSI AKCIJA
    def update_state(a,s):
        if a==0:
            return (s[0],s[1]+1)
        elif a==1:
            return (s[0]+1,s[1])
        elif a==2:
            return (s[0],s[1]-1)
        elif a==3:
            return (s[0]-1,s[1])
        else:
            return None

    #PRIKAZ VREDNOSTI STANJA
    def prikaz(V):
        my_array = list(V.values())
        my_array = np.round(my_array, 2)
        num_rows = dim[0]
        num_cols = dim[1]

        # Loop over the rows and columns and print the values
        for i in range(num_rows):
            for j in range(num_cols):
                print(my_array[j + dim[0] * i], end=" | ")  # Use end=" " to separate the values with a space
            print()  # Move to the next row
        print("=====================")



    policy = {}
    def create_policy(v,states,policy):

        a=np.argmax(v)
        if a==0:
            policy[states]="R"
        elif a==1:
            policy[states] = "D"
        elif a==2:
            policy[states] = "L"
        elif a==3:
            policy[states] = "U"
        else:
            policy[states] = "GRESKA"
        policy[cilj]="C"
        return policy

    def prikaz_policy(policy):
        for i in range(dim[0]):
            for j in range(dim[1]):
                print(policy[i,j], end=" | ")  # Use end=" " to separate the values with a space
            print()  # Move to the next row
        print("=====================")



    c = 0 #BROJAC
    flag=True
    while flag:
        if c==dim[0]*dim[1]:
            flag=False #AKO SU SVE VREDNOSTI STANJA MANJE OD PRAGA ZAUSTAVLJA SE RACUNANJE
        c = 0
        for states in V.copy():
            v = [float("-inf"), float("-inf"), float("-inf"), float("-inf")]
            for a in Actions[states]:
                v[a] = H[(states, a)] + gamma * V[update_state(a,states)]
            V[states]=max(v)
            policy=create_policy(v, states,policy)
            if abs(old_V[states]-V[states])<prag:
                c+=1
        #prikaz(V)
        prikaz_policy(policy)
        old_V = V





if __name__ == '__main__':
    world()


