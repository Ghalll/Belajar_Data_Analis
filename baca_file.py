import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_excel(
    r"data\Jumlah penduduk Menurut Jenis Kelamin dan Rasio Jenis Kelamin-2023-Provinsi.xlsx")
# print(df)

provinsi_sumatera = [
    "ACEH",
    "SUMATERA UTARA",
    "SUMATERA BARAT",
    "RIAU",
    "JAMBI",
    "SUMATERA SELATAN",
    "BENGKULU",
    "LAMPUNG",
    "KEPULAUAN BANGKA BELITUNG",
    "KEPULAUAN RIAU"
]

df_sumatera = df[df["Cakupan"].isin(provinsi_sumatera)]

fig = px.bar(
    df_sumatera,
    x="Cakupan",
    y=df_sumatera["TOTAL"] / 1_000_000,
    labels={"y": "Jumlah Penduduk (juta)", "Cakupan": "Provinsi di Sumatera"},
    title="Jumlah Penduduk di Provinsi Sumatera (2023)"
)

fig.update_traces(
    hovertemplate="<b>%{x}</b><br>Total: %{customdata:,.0f} jiwa",
    customdata=df_sumatera["TOTAL"]
)

plt.figure(figsize=(10, 6))
plt.bar(
    df_sumatera["Cakupan"],
    df_sumatera["TOTAL"] / 1_000_000,  # Convert to millions
)
plt.gca().yaxis.set_major_formatter(
    lambda x, _: f'{x:.1f} juta'
)
plt.xticks(rotation=90)
plt.xlabel("Provinsi di Sumatera")
plt.ylabel("Jumlah Penduduk")
plt.title("Jumlah Penduduk di Provinsi Sumatera (2023)")


plt.tight_layout()
plt.show()
fig.show()
