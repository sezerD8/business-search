import pandas as pd
import openpyxl
import xlsxwriter

def get_data(data):
    print(data)
    rows = []
    for item in data:
        row_companyName = item.get("Şirket Adı")
        row_companyAddress = item.get("Adres")
        row_companyRating = item.get("Puan")
        row_companyPhone = item.get("İletişim")
        
        rows.append({
            "Şirket Adı": row_companyName,
            "Şirket Adresi": row_companyAddress,
            "Şirket Puanı": row_companyRating,
            "Şirket İletişim": row_companyPhone
        })
    print(rows)
    df = pd.DataFrame(rows)
    with pd.ExcelWriter("data.xlsx", engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name="sheet1", index=False)
        worksheet = writer.sheets["sheet1"] 
        for idx, col in enumerate(df.columns):
            max_len = max(
                df[col].astype(str).map(len).max(),
                len(str(col))) + 2
            worksheet.set_column(idx, idx, max_len)