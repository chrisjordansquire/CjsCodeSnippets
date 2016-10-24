
def solve_81(file_name,k=None):
    f = open(file_name)
    mat = []
    for line in f:	
        s = [int(i) for i in line.split(',')]
        mat.append(s)
    f.close()
    
    N = len(mat)

    best_parent = [[None]*N for i in range(N)]

    for i in range(N):
        for j in range(N):
                if i == j == 0:
                    pass
                else:
                    if i==0:
                        i_prev,j_prev = 0,j-1
                    elif j==0:
                        i_prev,j_prev = i-1,j
                    else:
                        if mat[i-1][j]<mat[i][j-1]:
                            i_prev,j_prev = i-1,j
                        else:
                            i_prev, j_prev = i,j-1
                    mat[i][j] += mat[i_prev][j_prev]
                    best_parent[i][j] = (i_prev, j_prev)
    
    return mat[-1][-1]
    
