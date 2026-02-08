import pandas as pd

df=pd.read_csv("musteri_harcama.csv")
df.head()
df.shape
df.isnull().sum()
df["Gender"].value_counts()
df.groupby("City")["Annual_Income_k$"].sum().sort_values(ascending=False)
df.groupby(["City","Gender"])["Annual_Income_k$"].sum().sort_values(ascending=False)
df["Annual_Income_k$"].max()
df["Spending_Score"].max()



#Yaş, cinsiyet ve şehir bazında harcama farklılıkları var mı?

print(df.groupby("Gender")["Spending_Score"].mean())
print(df.groupby("City")["Spending_Score"].mean().sort_values(ascending=False))
df["Yas_Grubu"] = pd.cut(df["Age"], bins=[18, 25, 35, 50, 65], labels=["Genç", "Yetişkin", "Orta", "Olgun"])
print(df.groupby("Yas_Grubu")["Spending_Score"].mean())

df["Annual_Income_k$"].corr(df["Spending_Score"])



df["Gelir_Grubu"] = pd.cut( df["Annual_Income_k$"],bins=[0, 40, 80, 120], labels=["Düşük", "Orta", "Yüksek"])

df["Harcama_Grubu"] = pd.cut( df["Spending_Score"],bins=[0, 30, 60, 100],labels=["Düşük", "Orta", "Yüksek"])

df.head()


#Gelir grubu düşük harcaması yüksek olanlar.
df[(df["Gelir_Grubu"] == "Düşük") & (df["Harcama_Grubu"] == "Yüksek")]

segment_tablosu = pd.crosstab(df["Gelir_Grubu"], df["Harcama_Grubu"])
print(segment_tablosu)

# 🔹 Görselleştirme (heatmap)
plt.figure(figsize=(7,5))
sns.heatmap(segment_tablosu, annot=True, cmap="YlGnBu", fmt="d")
plt.title("Gelir ve Harcama Gruplarına Göre Müşteri Dağılımı")
plt.xlabel("Harcama Grubu")
plt.ylabel("Gelir Grubu")
plt.show()




# Sadece orta gelir – orta harcama segmenti
orta_segment = df[(df["Gelir_Grubu"] == "Orta") & (df["Harcama_Grubu"] == "Orta")]

# Şehir bazında sayısı
print(orta_segment["City"].value_counts())


sadik_segment = df[(df["Gelir_Grubu"] == "Düşük") & (df["Harcama_Grubu"] == "Yüksek")]
print(sadik_segment["City"].value_counts())


df.groupby(["Gelir_Grubu","Harcama_Grubu"])[["Annual_Income_k$","Spending_Score"]].mean()