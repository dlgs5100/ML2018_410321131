import imageio

key1 = imageio.imread('key1.png', format='png')
key2 = imageio.imread('key2.png', format='png')
E = imageio.imread('E.png', format='png')
I = imageio.imread('I.png', format='png')
Eprime = imageio.imread('Eprime.png', format='png')

epoch = 1
a = 0.00001
wk = [0,0,0]
