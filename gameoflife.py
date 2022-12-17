import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# start = np.array([[0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,1,0,0,0,0],
#                   [0,0,0,1,1,1,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0],
#                   [0,0,0,0,0,0,0,0,0]])

start = np.random.randint(2,size=(9,9)) #generate random 0 1 matrix 9x9

def get_sum_of_neighbours(matrix,row,col):
    sum = 0
    sum+=matrix[row-1][col-1]
    sum+=matrix[row-1][col]
    sum+=matrix[row-1][col+1]
    sum+=matrix[row][col-1]
    sum+=matrix[row][col+1]
    sum+=matrix[row+1][col-1]
    sum+=matrix[row+1][col]
    sum+=matrix[row+1][col+1]
    return sum

if __name__ == '__main__':
    fig = plt.figure()
    ims = []
    rows = start.shape[0]
    cols = start.shape[1]
    new_matrix = start
    
    iterations = 11  #declare number of iterations
    im = plt.imshow(start,cmap=plt.cm.gray.reversed(),animated=True) 
    ims.append([im])
    ax = plt.gca()
    ax.set_xticks(np.arange(0,start.shape[0],1)) #change xlabel
    ax.set_yticks(np.arange(0,start.shape[1],1)) #change ylabel
    for n in range(iterations):
        start = np.hstack((start, np.zeros((start.shape[0], 1), dtype=start.dtype))) #add empty row at top of matrix
        start = np.vstack((start, np.zeros((1, start.shape[1]), dtype=start.dtype))) #add empty matrix and right side of matrix
        for i in range(rows):
            for j in range(cols):
                if get_sum_of_neighbours(start,i,j) == 3: #if sum == 3 set cell to 1
                    new_matrix[i][j] = 1
                elif get_sum_of_neighbours(start,i,j) < 2 or get_sum_of_neighbours(start,i,j) > 3: #else set to 0
                    new_matrix[i][j] = 0
        im = plt.imshow(new_matrix,cmap=plt.cm.gray.reversed(),animated=True)
        ims.append([im])
        start = new_matrix
    ani = animation.ArtistAnimation(fig,ims,interval=1000,blit=True,repeat=False) #combine images into one animation
    plt.show()
