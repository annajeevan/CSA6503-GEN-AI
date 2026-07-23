import matplotlib.pyplot as plt

labels = ["GAN", "VAE", "Transformer"]
sizes = [40, 30, 30]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()