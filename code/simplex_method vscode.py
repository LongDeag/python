import numpy as np

def simplex_method():

    num_var, num_cons = [int(x) for x in input().split(' ')]
    max_func = [- int(x) for x in input().split(' ')]
    A = np.array([])
    for cons in range(num_cons):
        first_cons = [int(x) for x in input().split(' ')]
        A = np.append(A, first_cons)
    RHS = np.array([int(x) for x in input().split(' ')])
    RHS = np.append(RHS, 0).reshape(num_cons+1, -1)
    a = np.append(A, max_func).reshape(num_cons+1, num_var)
    Expected = np.array([0 for i in range(num_cons+1)]).reshape(num_cons+1, -1)
    slack = np.eye(num_cons+1)
    a = np.concatenate((a,slack),axis=1)
    a = np.concatenate((a,RHS), axis=1)
    a = np.concatenate((a, Expected), axis=1)


    while np.min(a[-1]) < 0:
        temp_L = []

        for col in range(a.shape[1]-1):
            if a[-1, col] == np.min(a[-1]):
                a[:, -1] = a[:, -2] / a[:,col]
                
                
                for j in range(a.shape[0]-1):
                    if a[j,-1] > 0:
                        temp_L.append(a[j,-1])
                if len(temp_L) == 0:
                    print('UNBOUNDED')
                    return 0
                for j in range(a.shape[0]-1):
                    if a[j,-1] == min(temp_L):
                        temp_num = col
                        a[j,:] /= a[j,col]
                        temp_row = a[j]
                    
        for j in range(a.shape[0]):
            if (a[j] == temp_row).all() == False:
                
                a[j] = a[j]-a[j,temp_num]*temp_row
                
        a[:,-1] = 0

        
    final_result = []
    for col in range(num_var):
        final = []
        for row in range(a.shape[0]-1):
            
            if a[row,col] == 1:
                final.append(1)
            elif a[row,col]!=1: 
                final.append(0)     
        
        if max(final) == 0:
            final_result.append(0)
        elif max(final) == 1:
            final_result.append(a[final.index(1),-2])     

    print(num_var)
    print(' '.join(str(e) for e in final_result))    

simplex_method()                       
    
