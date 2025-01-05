import pandas as pd
import matplotlib.pyplot as plt
import os

# Veriyi yükleyelim (örnek veri seti)
data = pd.read_csv('Amazon- Movies and Films.csv')

# Klasör oluşturma (eğer yoksa)
output_dir = 'movie_analysis_graphs'
os.makedirs(output_dir, exist_ok=True)

# Rating'e göre en yüksek puanlı filmleri sıralama
highest_rated = data.sort_values(by='Movie_Rating', ascending=False)

# Yüksek puanlı ve çok sayıda oylanan filmleri filtreleme
popular_high_rated = data[data['No_of_Ratings'] > 1000].sort_values(by='Movie_Rating', ascending=False)

# İlk 10 filmi gösterme
top_10_movies = popular_high_rated.head(10)
print(top_10_movies[['title', 'Movie_Rating', 'No_of_Ratings', 'Directed_By', 'Starring']])

# Görselleştirme: En yüksek puan alan ilk 10 filmi bar grafiğiyle göstermek
plt.figure(figsize=(10, 6))
plt.barh(top_10_movies['title'], top_10_movies['Movie_Rating'], color='skyblue')
plt.xlabel('Rating')
plt.title('Top 10 Highest Rated Movies (with >1000 Ratings)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Top_10_Highest_Rated_Movies.png'))  # Grafik kaydetme
plt.close()

# Yönetmenlere göre en çok beğenilen filmleri bulma
directors_popularity = data.groupby('Directed_By').agg({'Movie_Rating': 'mean', 'No_of_Ratings': 'sum'}).sort_values(by='Movie_Rating', ascending=False)

# En çok tercih edilen 10 yönetmeni ve filmlerini görme
top_directors = directors_popularity.head(10)
print(top_directors)

# Benzer şekilde oyuncular için analiz yapabiliriz
actors_popularity = data.groupby('Starring').agg({'Movie_Rating': 'mean', 'No_of_Ratings': 'sum'}).sort_values(by='Movie_Rating', ascending=False)

# En çok tercih edilen 10 oyuncuyu görmek
top_actors = actors_popularity.head(10)
print(top_actors)

# Görselleştirme: En çok beğenilen oyuncuların bar grafiği
plt.figure(figsize=(10, 6))
plt.barh(top_actors.index, top_actors['Movie_Rating'], color='salmon')
plt.xlabel('Average Rating')
plt.title('Top 10 Most Popular Actors')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Top_10_Most_Popular_Actors.png'))  # Grafik kaydetme
plt.close()

# Çıkış yılına göre film sayısını hesaplama
films_by_year = data.groupby('ReleaseYear').size()

# Çıkış yılına göre filmlerin ortalama puanını hesaplama
average_rating_by_year = data.groupby('ReleaseYear')['Movie_Rating'].mean()

# Film sayısının yıllara göre dağılımını görselleştirme
plt.figure(figsize=(12, 6))
films_by_year.plot(kind='bar', color='lightblue')
plt.title('Number of Films Released by Year')
plt.xlabel('Year')
plt.ylabel('Number of Films')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Films_Released_by_Year.png'))  # Grafik kaydetme
plt.close()

# Çıkış yılına göre ortalama puanları görselleştirme
plt.figure(figsize=(12, 6))
average_rating_by_year.plot(kind='line', marker='o', color='green')
plt.title('Average Rating by Year')
plt.xlabel('Year')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Average_Rating_by_Year.png'))  # Grafik kaydetme
plt.close()

# MPAA derecelendirmesine göre film sayısını hesaplama
films_by_mpaa = data.groupby('MPAA_Rating').size()

# MPAA derecelendirmesine göre ortalama puanları hesaplama
average_rating_by_mpaa = data.groupby('MPAA_Rating')['Movie_Rating'].mean()

# MPAA derecelendirmelerine göre film sayısının dağılımını görselleştirme
plt.figure(figsize=(10, 6))
films_by_mpaa.plot(kind='bar', color='lightcoral')
plt.title('Number of Films by MPAA Rating')
plt.xlabel('MPAA Rating')
plt.ylabel('Number of Films')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Films_by_MPAA_Rating.png'))  # Grafik kaydetme
plt.close()

# MPAA derecelendirmelerine göre ortalama puanları görselleştirme
plt.figure(figsize=(10, 6))
average_rating_by_mpaa.plot(kind='bar', color='purple')
plt.title('Average Rating by MPAA Rating')
plt.xlabel('MPAA Rating')
plt.ylabel('Average Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Average_Rating_by_MPAA_Rating.png'))  # Grafik kaydetme
plt.close()

# MPAA derecelendirmelerine göre fiyat dağılımını görselleştirme
plt.figure(figsize=(10, 6))
data.groupby('MPAA_Rating')['Price'].mean().plot(kind='bar', color='gold')
plt.title('Average Price by MPAA Rating')
plt.xlabel('MPAA Rating')
plt.ylabel('Average Price in Dollars')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'Average_Price_by_MPAA_Rating.png'))  # Grafik kaydetme
plt.close()

print(f"Grafikler '{output_dir}' klasörüne kaydedildi.")
