import os
import pandas as pd

# Klasör yolu
folder_path = r'data/processed_csv_files'  # CSV dosyalarının bulunduğu klasör

# Crime data için dictionary yapısı
crime_data = {}

# Klasördeki tüm dosyaları döngüyle işleme
for file_name in os.listdir(folder_path):

    # Dosya adı parçalama
    parts = file_name.split(",")  # Örnek: ["Bribery", "number.csv"]
    crime_type = parts[0].strip()  # "Bribery"
    metric_type = parts[1].replace(".csv", "").strip()  # "number" veya "per100k"

    # Dosyayı yükleme
    file_path = os.path.join(folder_path, file_name)
    df = pd.read_csv(file_path)  # İlk sütunu index olarak al

    # Dictionary yapısını güncelleme
    if crime_type not in crime_data:
        crime_data[crime_type] = {}  # Suç türü için boş dict oluştur
    if metric_type == "number":
        crime_data[crime_type]["number"] = df
    elif metric_type == "per100k":
        crime_data[crime_type]["per_100k"] = df

# Kontrol: İlk suç türünün verilerini inceleme
for crime, metrics in crime_data.items():
    print(f"Crime Type: {crime}")
    print("Total Counts DataFrame:\n", metrics.get("number", "No data"))
    print("Per 100k DataFrame:\n", metrics.get("per_100k", "No data"))
    break  # İlkini yazdır, tümünü görmek istemiyorsak
