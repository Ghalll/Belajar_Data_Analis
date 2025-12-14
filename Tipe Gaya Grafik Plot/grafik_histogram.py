import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

puppies = pd.DataFrame({
    "age_months": [2, 4, 6, 8, 10, 12],
    "weight": [1.5, 3.0, 5.0, 7.5, 10.0, 12.5]
})

plt.figure()
plt.hist(puppies.weight, range=(3, 10))
plt.xlabel("Weight (lbs)")
plt.ylabel("Number of Puppies")
plt.title("Distribution of Puppy Weights")
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))


gravel = pd.DataFrame({
    "radius": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})


plt.figure()
plt.hist(gravel.radius, bins=40, range=(2, 8), density=True)
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency Density')
plt.title('Gravel Size Distribution')


plt.show()
