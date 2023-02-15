import numpy as np


def world():
    """"
    grid=[0,None,None,None,None,None,None,None]
    h=[1,0,0,-3,0,-4,0,0]
    gama=0.9
    d=1
    #while True:
    for i in range (len(grid)-1):
        old=grid
        grid[i+1]=h[i]+gama*grid[i]
        d=grid[i+1]-old[i+1]
        #if d<0.1:
            #break
    print(grid)
    """
    gamma=0.9
    cilj=(2,1)
    """V={
        (0, 0): float("-inf"),
        (0, 1): float("-inf"),
        (0, 2): float("-inf"),
        (1, 0): float("-inf"),
        (1, 1): 0,
        (1, 2): float("-inf"),
        (2, 0): float("-inf"),
        (2, 1): float("-inf"),
        (2, 2): float("-inf")
    }"""
    V = {}
    for i in range(3):
        for j in range(3):
            V[(i, j)] = float("-inf")
    V[cilj]=0

    H={}
    for i in range(3):
        for j in range(3):
            for k in range(4):
                H[((i, j), k)]= 0

    H[(cilj, 0)] = 1
    H[(cilj, 1)] = 1
    H[(cilj, 2)] = 1
    H[(cilj, 3)] = 1

    #print(H)

    # 0 right, 1 down, 2 left, 3 up
    Actions={
        (0, 0): [0,1],
        (0, 1): [0,1,2],
        (0, 2): [1,2],
        (1, 0): [0,1,3],
        (1, 1): [0,1,2,3],
        (1, 2): [1,2,3],
        (2, 0): [0,3],
        (2, 1): [0,2,3],
        (2, 2): [2,3]
    }
    t=0
    while t<8:
        old=V
        for states in V.copy():
            v = [float("-inf"), float("-inf"), float("-inf"), float("-inf")]
            for a in Actions[states]:
                #print(a)
                #print(states)
                #print(H[(states,a)])
                #print(V[states])
                v[a] = H[(states, a)] + gamma * V[states]

            ind=[index for index,item in enumerate(v) if item==max(v)]
            #print(ind)
            for i in ind:
                if max(v)==float("-inf"):
                    continue
                #i=np.argmax(v)
                V[cilj] = 0
                if i==0:
                    """if is_calculated[(states[0],states[1]+1)]:
                        continue
                    else:"""
                    V[(states[0],states[1]+1)]=max(v[0],V[(states[0],states[1]+1)])
                    #is_calculated[(states[0],states[1]+1)]=True
                elif i==1:
                    """if is_calculated[(states[0] + 1, states[1])]:
                        continue
                    else:"""
                    V[(states[0] + 1, states[1])] = max(V[(states[0] + 1, states[1])],v[1])
                    #is_calculated[(states[0] + 1, states[1])]=True

                elif i==2:
                    """if is_calculated[(states[0], states[1] - 1)]:
                        continue
                    else:"""
                    V[(states[0], states[1] - 1)] = max(V[(states[0], states[1] - 1)],v[2])
                    #is_calculated[(states[0], states[1] - 1)]=True

                elif i==3:
                    """if is_calculated[(states[0] - 1, states[1])]:
                        continue
                    else:"""
                    V[(states[0] - 1, states[1])] = max(V[(states[0] - 1, states[1])],v[3])
                    #is_calculated[(states[0] - 1, states[1])]=True

        """if V[states] - old[states] < 0.1:
            print("AAAAAAAAAA"+ str(t))
            break"""

        t+=1
    my_array = list(V.values())
    my_array=np.round(my_array,2)
    num_rows = 3
    num_cols = 3

    # Loop over the rows and columns and print the values
    for i in range(num_rows):
        for j in range(num_cols):
            print(my_array[j+3*i], end=" | ")  # Use end=" " to separate the values with a space
        print()  # Move to the next row


"""
    for key in V:
        if key==(0,4):
            break
        for a in Actions:
            if a==0:
                V[(0, key[1] + 1)] = H[(key, 0)] + gamma * V[key]
                print(V)
            elif a==1:
                V[(0, key[1] + 1)] = H[(key, 0)] + gamma * V[key]
                print(V)

"""



if __name__ == '__main__':
    world()


