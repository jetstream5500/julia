import matplotlib.pyplot as plt
import numpy as np

def iterate_point(c):
    counter = 0
    while abs(c) < 2 and counter < 100:
        c = c*c + .5*np.exp(1j*2*np.pi*.895)
        counter+=1

    return counter

def main():
    xmin = -2
    xmax = 2
    xwidth = 1000

    ymin = -2
    ymax = 2
    ywidth = 1000

    a = np.zeros(shape=(xwidth,ywidth))

    for i,x in enumerate(np.linspace(xmin, xmax, num=xwidth)):
        for j,y in enumerate(np.linspace(xmin, xmax, num=ywidth)):
            a[i][j] = iterate_point(complex(x, y))

    a = np.flip(a, 0)

    plt.imshow(a)
    plt.show()


if __name__ == '__main__':
    main()
