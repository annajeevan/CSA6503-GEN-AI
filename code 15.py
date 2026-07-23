import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5]
loss = [0.9, 0.7, 0.5, 0.4, 0.2]

plt.scatter(epochs, loss)
plt.title("Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()