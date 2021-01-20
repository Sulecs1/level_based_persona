#HADİ BAKALIM BAŞLAYALIM !
#PEDAL ÇEVİRMEYE DEVAMMM
import numpy as np
import pandas as pd

#users.csv tablosu bizim müşterimizin karakteristlik özelliklerini tutuyor :)

users=pd.read_csv("users.csv")
users.head()

purchases=pd.read_csv("purchases.csv")
purchases.head()

#İki tabloyu birleştirme işlemi(uid) numarası ile yapılmaktadır.

df = purchases.merge(users, how="inner", on="uid")#purchases tablosuna göre birleştirme işlemi

df.shape
df["uid"].nunique()

purchases.head()
df.head()

#country,device,gender,age kırılımında toplam kazançlar:
df.groupby(["country", "device", "gender", "age"]).agg({"price": ["sum"]})
#kazançları küçükten büyüğe sıralama işlemi(sort_values) yapıp agg_df değişkenine atadım.
agg_df=df.groupby(["country", "device", "gender", "age"]).agg({"price": "sum"}).sort_values("price",ascending=False)
agg_df.reset_index(inplace=True) #indeks değerleri atadım
agg_df.head() #ilk beş veri
agg_df.columns
#age değişkenini kategorik değişkene çevirip,agg_df'e "age_cat" değişkeni ile ekleme işlemi
#Numerik değişkeni kategorik değişkene çevirme işlemi yaptık!
agg_df["age_cat"] = pd.cut(agg_df["age"],bins=[0, 19, 23, 40, 50,agg_df["age"].max()],labels=["0_18", "19_23", "24_39", "40_49", "50_"+str(agg_df["age"].max())]) #sayısal değişkeni  verdiğimiz aralığa göre böldü
agg_df.head()

#new_df.columns

#level based müşterileri tanımlayıız ve veri setine değişken olarak ekleyiniz :)
#price değişkenine göre segmente ayırma işlemi yaptım
agg_df["customers_level_based"]=[rows[0]+"_"+rows[1].upper()+"_"+rows[2]+"_"+rows[5]  for rows in agg_df.values]
agg_df=agg_df[["customers_level_based","price"]]
agg_df = agg_df.groupby("customers_level_based").agg({"price":"mean"})
agg_df.reset_index(inplace=True)
## 7. Yeni müşterileri price'a göre segmentlere ayırınız, "segment" isimlendirmesi ile agg_df'e ekleyiniz.
# Segmentleri betimleyiniz.
agg_df["segment"]=pd.qcut(agg_df["price"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("segment").agg({"price":["mean"]}).head()
agg_df.head(200)


###42 yaşında IOS kullanan bir kadın hangi segmenttedir?
new_user = "TUR_AND_F_40_49"

istenen =  agg_df.loc[agg_df['customers_level_based'] == new_user]

print(istenen)