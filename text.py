import pytesseract as tess #library convert dari gambar ke teks
import  pandas as pd #library text untuk dimasukkan ke excell
import PySimpleGUI as sg
import datetime #menampilkan waktu

sg.theme('DarkG reen4')
EXCEL_FILE = 'output.xlsx'
df = pd.read_excel(EXCEL_FILE)
tess.pytesseract.tesseract_cmd = r'C:/Users/aryat/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
from PIL import Image

img = Image.open('data/data3.jpg') #mengambil file dari explorer
text = tess.image_to_string(img)

print(text)
# Load data dari file Excel jika ada
try:
    df = pd.read_excel("output.xlsx")
except FileNotFoundError:
    df = pd.DataFrame()

# Buat baris baru dengan tanggal otomatis
new_row = pd.DataFrame({'col1': [text], 'Date': [datetime.datetime.now()]})

# Tambahkan baris baru ke DataFrame
df = pd.concat([df, new_row], ignore_index=True)

# Simpan perubahan ke file Excel
df.to_excel("output.xlsx", index=False, engine='openpyxl')