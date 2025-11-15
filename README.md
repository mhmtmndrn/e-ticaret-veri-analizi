# E-Ticaret Veri Analizi

Bu proje, bir e-ticaret sitesine ait müşteri ve satış verilerinin analiz edilmesi ve çeşitli grafiklerle görselleştirilmesi amacıyla hazırlanmıştır. Analiz sürecinde Pandas, Numpy ve Matplotlib kütüphaneleri kullanılmıştır.

## Kullanılan Veri Setleri

1. customer_details.csv
   - customer_id
   - sex
   - customer_age
   - tenure

2. basket_details.csv
   - basket_id
   - customer_id
   - product_id
   - basket_count
   - basket_date

## Kullanılan Kütüphaneler

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Yapılan Analizler

1. Cinsiyet Dağılımı
   - Yalnızca Male ve Female verileri alınmıştır.
   - Cinsiyet adetleri ve yüzdeleri hesaplanmıştır.
   - Pie chart ile görselleştirilmiştir.
   - Sonuçlar terminale yazdırılmıştır.

2. Yaş Dağılımı
   - 10 yaş altı ve 80 yaş üstü veriler dahil edilmemiştir.
   - 5’er yıllık yaş aralıkları oluşturulmuştur.
   - Histogram grafiği çizilmiştir.
   - Her yaş aralığındaki kişi sayısı terminale yazdırılmıştır.
   - Ortalama yaş hesaplanmıştır.

3. Günlük Satış Analizi
   - basket_date değişkeni datetime formatına dönüştürülmüştür.
   - Günlük toplam satış adedi hesaplanmıştır.
   - Günlük satış grafiği çizilmiştir.
   - En çok satış yapılan 10 gün terminale yazdırılmıştır.

4. En Çok Satılan Ürünler
   - product_id baz alınarak toplam satış adetleri hesaplanmıştır.
   - En çok satılan ilk 10 ürün bar grafiği ile gösterilmiştir.
   - Terminalde ürün ID ve satış adetleri listelenmiştir.
   - Toplam farklı ürün sayısı hesaplanmıştır.
## Analizler sonucunda ortaya çıkanlar 
   - Bu e-ticaret sitesini kullanan kişilerin yakaşık %77'si erkek, %23 kadındır.
   - Bundan dolayı diyebiliriz ki site çoğunlukla erkeklere yönelik ürün satmaktadır.
   - Kullanıcıların çok büyük bir çoğunluğu 25-35 yaşları arasındadır.
   - Günlük satış grafiğinden görebileceğimiz üzere 2019-05-25 ve 2019-05-27 tarihleri arasında bir kampanya olmuş olabilir.
   - Çünkü satışlar incelediğimiz diğer zamanlara göre yaklaşık 3 kat daha fazladır.
   - En çok satılan 3 ürün açık ara 43524799 , 31516269 , 39833031 ürün ID'li 3 üründür.
   - Site bu ürünler için kampanya yapmış olabilir veya bu ürünler, bu dönem ihtiyacı olan ürünler olup daha fazla satılmış olabilir.
## Çalıştırma
Terminali açarak kütüphaneler yüklü değil ise ;
pip install pandas
pip install numpy
pip install matplotlib yazarak yüklemesi yapılmalı.

terminali açarak:

git clone https://github.com/mhmtmndrn/e-ticaret-veri-analizi.git 
sonrasında dosyayı visual studio code ile çalıştırınız.

## Proje Yapısı

proje.py
customer_details.csv
basket_details.csv
README.md

## Notlar

- Grafikler ekranda gösterilir, dosyaya kaydedilmez.
- Veri dosyalarının proje dizininde bulunması gereklidir.
- Kod yalnızca veri analizi ve görselleştirme amacıyla yazılmıştır.

## Geliştirici

GitHub: https://github.com/mhmtmndrn

