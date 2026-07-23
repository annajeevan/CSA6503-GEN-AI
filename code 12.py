import matplotlib.pyplot as plt

accuracy = [60, 70, 80, 90, 95]
plt.plot(accuracy)
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.show()