import pandas as pd
from matplotlib import pyplot as plt

data = pd.DataFrame({
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Phoenix Police Dept": [1200, 1300, 1250, 1400, 1500],
    "Los Angeles Police Dept": [2000, 2100, 2200, 2300, 2400],
    "Chicago Police Dept": [1800, 1750, 1700, 1650, 1600]
})

plt.style.use("ggplot")

plt.plot(data["Year"], data["Phoenix Police Dept"],
         label="Phoenix", color="DarkCyan")

plt.plot(data["Year"], data["Los Angeles Police Dept"],
         label="Los Angeles", linestyle=":")

plt.plot(data["Year"], data["Chicago Police Dept"],
         label="Chicago", marker="s")

plt.legend()
plt.show()
