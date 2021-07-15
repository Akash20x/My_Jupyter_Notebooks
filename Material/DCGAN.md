A DCGAN is a direct extension of the GAN, except that it explicitly uses convolutional and convolutional-transpose layers in the discriminator and generator, respectively.

🔸The discriminator is made up of strided convolution layers, batch norm layers, and LeakyReLU activations. 

🔸The input is an image and the output is a scalar probability that the input is from the real data distribution. 

🔸The generator is comprised of convolutional-transpose layers, batch norm layers, and ReLU activations. 

🔸The input is a latent vector, zz, that is drawn from a standard normal distribution and the output is an RGB image. 

🔸The strided conv-transpose layers allow the latent vector to be transformed into a volume with the same shape as an image.

🔸The image that you see below is taken from the original DCGAN paper and shows you how impressive the results could be!
