import matplotlib.pyplot as plt

models = ["GAN", "VAE", "Diffusion"]
images = [100, 80, 120]

plt.bar(models, images)
plt.title("Generated Images")
plt.show()