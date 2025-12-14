import pandas as pd
from matplotlib import pyplot as plt

hours = pd.DataFrame({
    "officer": ["A", "B", "C", "D", "E"],
    "desk_work": [5, 6, 4, 7, 8],
    "fiedl_work": [3, 2, 4, 1, 2],
    "avg_hours_worked": [8, 8, 8, 8, 10],
    "std_hours_worked": [1, 0.5, 1.5, 0.2, 0.3]
})


plt.bar(hours.officer, hours.avg_hours_worked, yerr=hours.std_hours_worked)
# plt.bar(hours.officer, hours.desk_work, label="Desk Work")
# plt.bar(hours.officer, hours.fiedl_work, label="Field Work", bottom=hours.desk_work)

plt.legend()
plt.show()
