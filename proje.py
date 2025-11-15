#Kütüphaneleri içe aktarma 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

#Veri yükleme
baskets = pd.read_csv("basket_details.csv")
customers = pd.read_csv("customer_details.csv")
# tarihi datetime yapma
baskets["basket_date"] = pd.to_datetime(baskets["basket_date"], errors="coerce")

# Cinsiyet Analizi------------------------------------------------------------------------
filtered_customers = customers[customers["sex"].isin(["Male", "Female"])]#sadece male ve female aldım.
sex_counts = filtered_customers["sex"].value_counts()
sex_percent = (sex_counts / sex_counts.sum()) * 100

plt.figure()
plt.pie(
    sex_percent,
    labels=sex_percent.index,
    autopct="%.1f%%"
)
plt.title("Cinsiyet Dağılımı")
plt.tight_layout()
plt.show()

#terminal çıktısı
print("\nCinsiyet Dağılımı \n")

for c in sex_counts.index:
    adet = sex_counts[c]
    yuzde = sex_percent[c]
    print(f"{c}: {adet} kişi  |  %{yuzde:.2f}")

print("\nToplam Müşteri Sayısı:", sex_counts.sum())
print("\n")

#Cinsiyet Analizi------------------------------------------------------------------------

# Yaş dağılımı---------------------------------------------------------------
ages = customers["customer_age"]
filtered_ages = ages[(ages >= 10) & (ages <= 80)]

#Yaş aralıklarını tanımlama
bins = list(range(10, 85, 5))  # 10, 15, 20, 25 ... 80
labels = [f"{bins[i]}-{bins[i+1]-1}" for i in range(len(bins)-1)]

age_groups = pd.cut(filtered_ages, bins=bins, labels=labels, right=False)

plt.figure(figsize=(10,6))
plt.hist(
    filtered_ages,
    bins=bins, 
    edgecolor="black"
)
plt.title("Müşteri Yaş Dağılımı (10–80 Arası)")
plt.xlabel("Yaş")
plt.ylabel("Kişi Sayısı")
plt.xticks(range(10, 85, 5))
plt.tight_layout()
plt.show()

print("\nYaş Dağılımı\n")

age_counts = age_groups.value_counts().sort_index()

for interval, count in age_counts.items():
    print(f"{interval}: {count} kişi")

print("\nToplam kişi:", age_counts.sum())
print("\n")

avg_age = filtered_ages.mean()

print(f"Ortalama yaş: {avg_age:.2f}")
print("\n")


#yaş dağılmı----------------------------------------------------

#Günlük toplam satış----------------------------------------------
daily_sales = baskets.groupby("basket_date")["basket_count"].sum()

plt.figure(figsize=(12,6))
plt.plot(daily_sales.index, daily_sales.values, marker="o")
plt.title("Günlük Satış Grafiği")
plt.xlabel("Tarih")
plt.ylabel("Toplam Satış")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
#Günlük toplam satış----------------------------------------------
# En çok satış yapılan 10 gün-----------------------------------
# Günlük satış 
daily_sales = baskets.groupby("basket_date")["basket_count"].sum()

top10_days = daily_sales.sort_values(ascending=False).head(10)

print("\nEN ÇOK SATIŞ YAPILAN 10 GÜN\n")
for date, count in top10_days.items():
    print(f"Tarih: {date.date()}  |  Toplam satış: {count}")

print("\nToplam gün sayısı:", len(daily_sales))
print("\n")
# En çok satış yapılan 10 gün-----------------------------------

#En çok satılan 10 ürün------------------------------------------

#id'ye göre toplam satış adedi
product_sales = baskets.groupby("product_id")["basket_count"].sum()
top10 = product_sales.sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
plt.bar(top10.index.astype(str), top10.values, edgecolor="black")
plt.title("En Çok Satılan İlk 10 Ürün")
plt.xlabel("Ürün ID")
plt.ylabel("Toplam Satış")
plt.tight_layout()
plt.show()

print("\nEn çok satılan 10 ürün \n")
for product_id, count in top10.items():
    print(f"Ürün ID: {product_id}  |  Toplam satış: {count}")

print("\nToplam farklı ürün sayısı:", product_sales.shape[0])
print("\n")