import numpy as np
import matplotlib.pyplot as plt

def logistic_eq(a, z):
    return a*z*(1-z)

def iterate_log_eq(a, z):
    for i in range(60):
        z = logistic_eq(a, z)

    if abs(z) < 3:
        return 1
    else:
        return 0

def figure1():
    width, height = (600, 600)
    rmin, rmax = (1.0, 4.0)
    cmin, cmax = (-1.5, 1.5)

    a = np.zeros(shape=(height,width))

    for x in range(width):
        r = (x * (rmax-rmin)/width) + rmin
        for y in range(height):
            c = (y * (cmax-cmin)/height) + cmin
            if abs(complex(r-2, c)) <= 1:
                a[y,x] = 0
            else:
                a[y,x] = abs(iterate_log_eq(complex(r, c), 0.5))

    a = np.transpose(a)
    a = np.flip(a)

    plt.imshow(a, cmap='Greys', extent=[cmin, cmax, rmin, rmax])
    plt.show()

def figure2():
    width, height = (600, 600)
    rmin, rmax = (-2.0, 2.0)
    cmin, cmax = (-2.0, 2.0)

    a = np.zeros(shape=(height,width))

    for x in range(width):
        r = (x * (rmax-rmin)/width) + rmin
        for y in range(height):
            c = (y * (cmax-cmin)/height) + cmin
            a[y,x] = abs(iterate_log_eq(0.222520934-0.9749279122j, complex(r, c)))
            #a[y,x] = abs(iterate_log_eq(4, complex(r, c)))
            #a[y,x] = abs(iterate_log_eq(2.4161+0.9093j, complex(r, c)))
            #a[y,x] = abs(iterate_log_eq(0.5, complex(r, c)))

    a = np.transpose(a)
    a = np.flip(a)

    plt.imshow(a, cmap='Greys', extent=[cmin, cmax, rmin, rmax])
    plt.show()

def figure3():
    width, height = (600, 600)
    rmin, rmax = (-0.5, 1.5)
    cmin, cmax = (-1.2, 1.2)

    a = np.zeros(shape=(height,width))

    for x in range(width):
        r = (x * (rmax-rmin)/width) + rmin
        for y in range(height):
            c = (y * (cmax-cmin)/height) + cmin
            a[y,x] = max(a[y,x],abs(iterate_log_eq(1.0, complex(r, c)))*1)
            a[y,x] = max(a[y,x],abs(iterate_log_eq(1.5, complex(r, c)))*2)
            a[y,x] = max(a[y,x],abs(iterate_log_eq(2.5, complex(r, c)))*3)
            a[y,x] = max(a[y,x],abs(iterate_log_eq(2.9, complex(r, c)))*4)

    a = np.flip(a)

    plt.imshow(a, cmap='Greys', extent=[rmin, rmax, cmin, cmax])
    plt.show()




if __name__ == '__main__':
    figure1()
    figure2()
    figure3()
