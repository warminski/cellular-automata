import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

start = np.zeros((40,40),dtype=int) #generate 40x40 matrix filled with 0
probability = 0.1 #probaility that two cells will "stuck"


def get_block(matrix, n, m):
    block = matrix[n:n + 2, m:m + 2]  # slice matrix into 2x2 blocks
    return block


def change_state(block):
    if block.shape[1] == 1 or block.shape[0] == 1:
        return block
    # check for condition [1 0]
    #                     [0 0]
    #
    # and swap to:        [0 0]
    #                     [1 0]
    if block.shape[1] == 2 and block[0][0] == 1 and block[0][1] == 0 and block[1][0] == 0 and block[1][1] == 0:
        block[0][0] = 0
        block[0][1] = 0
        block[1][0] = 1
        block[1][1] = 0

    # check for condition [0 1]
    #                     [0 0]
    #
    # and swap to:        [0 0]
    #                     [0 1]
    elif block.shape[1] == 2 and block[0][0] == 0 and block[0][1] == 1 and block[1][0] == 0 and block[1][1] == 0:
        block[0][0] = 0
        block[0][1] = 0
        block[1][0] = 0
        block[1][1] = 1

    # check for condition [1 0]
    #                     [1 0]
    #
    # and swap to:        [0 0]
    #                     [1 1]
    elif block.shape[1] == 2 and block[0][0] == 1 and block[0][1] == 0 and block[1][0] == 1 and block[1][1] == 0:
        block[0][0] = 0
        block[0][1] = 0
        block[1][0] = 1
        block[1][1] = 1

    # check for condition [1 0]
    #                     [0 1]
    #
    # and swap to:        [0 0]
    #                     [1 1]
    elif block.shape[1] == 2 and block[0][0] == 1 and block[0][1] == 0 and block[1][0] == 0 and block[1][1] == 1:
        block[0][0] = 0
        block[0][1] = 0
        block[1][0] = 1
        block[1][1] = 1

    # check for condition [0 1]
    #                     [1 0]
    #
    # and swap to:        [0 0]
    #                     [1 1]
    elif block.shape[1] == 2 and block[0][0] == 0 and block[0][1] == 1 and block[1][0] == 1 and block[1][1] == 0:
        block[0][0] = 0
        block[0][1] = 0
        block[1][0] = 1
        block[1][1] = 1

    # check for condition [0 1]
    #                     [0 1]
    #
    # and swap to:        [0 0]
    #                     [1 1]
    elif block.shape[1] == 2 and block[0][0] == 0 and block[0][1] == 1 and block[1][0] == 0 and block[1][1] == 1:
        block[0][0] = 0
        block[0][1] = 0
        block[1][0] = 1
        block[1][1] = 1

    # check for condition [1 1]
    #                     [1 0]
    #
    # and swap to:        [1 0]
    #                     [1 1]
    elif block.shape[1] == 2 and block[0][0] == 1 and block[0][1] == 1 and block[1][0] == 1 and block[1][1] == 0:
        block[0][0] = 1
        block[0][1] = 0
        block[1][0] = 1
        block[1][1] = 1

    # check for condition [1 1]
    #                     [0 1]
    #
    # and swap to:        [0 1]
    #                     [1 1]
    elif block.shape[1] == 2 and block[0][0] == 1 and block[0][1] == 1 and block[1][0] == 0 and block[1][1] == 1:
        block[0][0] = 0
        block[0][1] = 1
        block[1][0] = 1
        block[1][1] = 1

    # check for condition [1 1]
    #                     [0 0]
    #
    # and swap to:        [0 0]
    #                     [1 1]
    # THIS IS BASED ON PROBABILITY THAT TWO GRAINS WILL GET STUCK
    elif block.shape[1] == 2 and block[0][0] == 1 and block[0][1] == 1 and block[1][0] == 0 and block[1][1] == 0:
        if random.random() > probability:
            block[0][0] = 0
            block[0][1] = 0
            block[1][0] = 1
            block[1][1] = 1
    return block


if __name__ == '__main__':
    fig = plt.figure()
    ims = []
    
    for n in range(200): # number of iterations
        start[0:1,15:25] = np.random.randint(2,size=10) #generate sand on top
        im = plt.imshow(start,cmap=plt.cm.gray.reversed(),animated=True)
        
        if n % 2 == 0: # if iteration is even start grid from 0
            for i in range(0,start.shape[0],2):
                for j in range(0,start.shape[1],2):
                    start[i:i+2, j:j+2] = change_state(get_block(start, i, j)) # change state of cells
        else: # if iteration is odd start grid from 1
            for i in range(1,start.shape[0],2):
                for j in range(1,start.shape[1],2):
                    start[i:i+2, j:j+2] = change_state(get_block(start, i, j)) #change state of cells
        ims.append([im])
        
    ani = animation.ArtistAnimation(fig,ims,interval=50,blit=True,repeat=False) #combine images into one animation
    plt.show()





