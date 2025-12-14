import pandas as pd
from matplotlib import pyplot as plt

cellphone = pd.DataFrame({
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 3, 5, 7, 11]
})

plt.scatter(cellphone.X, cellphone.Y, color="red", marker="s", alpha=0.3)

plt.xlabel("Latitude")
plt.ylabel("Longitude")

plt.show()
