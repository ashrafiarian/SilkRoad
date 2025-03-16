from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt

def plot_digit(image_data):
    image = image_data.reshape(28, 28)
    plt.imshow(image, cmap="binary")
    plt.axis("off")

mnist = fetch_openml("mnist_784", as_frame=False)
for _ in range(18):
    X = mnist.data[60000 + _]
    plot_digit(X)
    plt.savefig(f"mnist_X_test_{_}.png")