# Amazon Movie Analysis and Visualization


![movie](https://github.com/user-attachments/assets/471c2a3c-6922-41a8-bc40-331868c15a58)

Bu proje, Amazon.com'daki film ve dizi verilerini analiz etmeyi ve görselleştirmeyi amaçlamaktadır. Veri seti, her bir film hakkında başlık, puan, yönetmen, oyuncular, yayın yılı, MPAA derecelendirmesi, format ve fiyat gibi bilgileri içermektedir. Bu projede, filmleri çeşitli ölçütlere göre inceleyip görselleştirmeler yaparak en yüksek puanlı filmleri, popüler yönetmenleri ve oyuncuları keşfetmeyi amaçlıyoruz.

## Kullanılan Teknolojiler
- **Python**
  - **Pandas**: Veri manipülasyonu ve analizi için.
  - **Matplotlib**: Görselleştirme için.
- **Veri Seti**: Amazon'daki filmler ve diziler hakkında bilgiler içeren bir CSV dosyası.

## Proje Özellikleri
- **Veri Analizi**: Filmler, yönetmenler, oyuncular, yayın yılı ve MPAA derecelendirmeleri gibi farklı kategorilere göre analiz edilmiştir.
- **Görselleştirmeler**:
- Top_10_Highest_Rated_Movies.png: En yüksek puanlı 10 film.
- Top_10_Most_Popular_Actors.png: En popüler 10 oyuncu.
- Films_Released_by_Year.png: Yıllara göre yayınlanan film sayısı.
- Average_Rating_by_Year.png: Yıllara göre ortalama film puanı.
- Films_by_MPAA_Rating.png: MPAA derecelendirmelerine göre film sayısı.
- Average_Rating_by_MPAA_Rating.png: MPAA derecelendirmelerine göre ortalama puan.
- Average_Price_by_MPAA_Rating.png: MPAA derecelendirmelerine göre ortalama fiyat.
  
## Kullanım
1. **Bağımlılıkların Yüklenmesi**:
   - Bu projeyi çalıştırmak için aşağıdaki kütüphaneleri yüklemeniz gerekmektedir:
   
   ```bash
   pip install pandas matplotlib os
   python Amazon Movie Analysis and Visualization.py

## Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakabilirsiniz.
