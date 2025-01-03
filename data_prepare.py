# import os
# import pandas as pd

# # Dosya yolu
# file_path = r'data\crim_off_cat_spreadsheet.xlsx'  # Buraya orijinal Excel dosyasının yolunu yaz
# output_dir = "processed_csv_files"  # Çıkış dosyalarının kaydedileceği klasör

# # Çıkış klasörünü oluştur (yoksa)
# os.makedirs(output_dir, exist_ok=True)

# # Excel dosyasını yükle
# excel_file = pd.ExcelFile(file_path)

# # Summary sheet'inden suç türlerini al
# summary_sheet = pd.read_excel(file_path, sheet_name="Summary", header=None)
# crime_types = summary_sheet.iloc[15:57, 3].dropna().tolist()

# # Her bir sheet'i işle ve ayrı CSV dosyalarına kaydet
# sheet_index = 0
# for sheet_name in excel_file.sheet_names[2:]:
#     # Sheet'i oku
#     df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

#     # Gerçek verinin başladığı satırdan itibaren al
#     df = df.iloc[8:].reset_index(drop=True)
#     df = df.dropna(axis=1, how='all')
#     # İkinci satırı kaldır
#     df = df.drop(1)
#     # Son 2 satırı kaldır
#     df = df.drop(df.tail(3).index)
#     # İlk satır kolon başlıkları olarak belirleniyor
#     df.columns = df.iloc[0]
#     df = df[1:].reset_index(drop=True)

#     # ":" ile işaretlenmiş boş değerleri NaN olarak işaretle
#     df.replace(":", pd.NA, inplace=True)
#     #1.sütündaki headerı Country yap
#     df.rename(columns={df.columns[0]: "Country"}, inplace=True)


#     # Suç türü ve metrik bilgisi
#     crime_type = crime_types[sheet_index]
#     metric = "number" if sheet_index % 2 == 0 else "per100k"
#     new_file_name = f"{crime_type},{metric}.csv"
#     output_path = os.path.join(output_dir, new_file_name)

#     # İşlenmiş veriyi yeni CSV dosyasına kaydet
#     df.to_csv(output_path, index=False)

#     sheet_index += 1

# print(f"Tüm işlenmiş veriler {output_dir} klasörüne CSV olarak kaydedildi.")
import os
import pandas as pd

# Dosya yolu
file_path = r'data\crim_off_cat_spreadsheet.xlsx'  # Buraya orijinal Excel dosyasının yolunu yaz
output_dir_csv = "data\processed_csv_files"  # Çıkış dosyalarının kaydedileceği klasör
output_dir_xlsx = "data\processed_xlsx_files"  # Çıkış dosyalarının kaydedileceği klasör
# Çıkış klasörünü oluştur (yoksa)
os.makedirs(output_dir_csv, exist_ok=True)
os.makedirs(output_dir_xlsx, exist_ok=True)

# Excel dosyasını yükle
excel_file = pd.ExcelFile(file_path)

# Summary sheet'inden suç türlerini al
summary_sheet = pd.read_excel(file_path, sheet_name="Summary", header=None)
crime_types = summary_sheet.iloc[15:57, 3].dropna().tolist()
print(crime_types)

# Her bir sheet'i işle ve ayrı CSV dosyalarına kaydet
sheet_index = 0
for sheet_name in excel_file.sheet_names[2:]:
    # Sheet'i oku
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=8)

    # Gerçek verinin başladığı satırdan itibaren al
    df = df.iloc[1:]
    df = df.dropna(axis=1, how='all')
    df = df.rename(columns={"TIME": "Country"})
    df.replace(":", pd.NA, inplace=True)
    df = df.iloc[:-3]
    df.set_index("Country", inplace=True)

    # Suç türü ve metrik bilgisi
    crime_type = crime_types[sheet_index]
    metric = "number" if sheet_index % 2 == 0 else "per100k"
    new_file_name_csv = f"{crime_type},{metric}.csv"
    new_file_name_xlsx = f"{crime_type},{metric}.xlsx"
    output_path_csv = os.path.join(output_dir_csv, new_file_name_csv)
    output_path_xlsx = os.path.join(output_dir_xlsx, new_file_name_xlsx)

    # İşlenmiş veriyi yeni CSV dosyasına kaydet
    df.to_csv(output_path_csv)
    df.to_excel(output_path_xlsx, engine='openpyxl')

    sheet_index += 1

print(f"Tüm işlenmiş veriler kaydedildi.")
