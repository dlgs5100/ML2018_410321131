import imageio
import matplotlib.pyplot as plt

key1 = imageio.imread('key1.png', format='png')
key2 = imageio.imread('key2.png', format='png')
E = imageio.imread('E.png', format='png')
I = imageio.imread('I.png', format='png')
Eprime = imageio.imread('Eprime.png', format='png')

epoch = 1   #training time
a = 0.00001 #learning rate
wk = [0,0,0]  #initial coefficient

while True: 
    for H in range(300):
        for W in range(400):
            ak = wk[0] * key1[H][W] + wk[1] * key2[H][W] + wk[2] * I[H][W]
            ek = E[H][W] - ak
            wk[0] = wk[0] + a * ek * key1[H][W]
            wk[1] = wk[1] + a * ek * key2[H][W]
            wk[2] = wk[2] + a * ek * I[H][W]
        print("H:",H)

    if epoch >= 0:
        print("Epoch:", epoch)
        print("Coefficient of w:",wk)

        Decryption_E = (E - (wk[0] * key1) - (wk[1] * key2)) / wk[2]

        plt.imshow(Decryption_E, cmap='gray')
        plt.show()
        
        Decryption_Eprime = (Eprime - (wk[0] * key1) - (wk[1] * key2)) / wk[2] 

        plt.imshow(Decryption_Eprime, cmap='gray')
        plt.show()

    epoch+=1
        
