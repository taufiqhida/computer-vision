import cv2
import numpy as np

# Fungsi untuk melakukan translasi gambar
def translate_image(image, x, y):
    # Tentukan matriks translasi
    translation_matrix = np.float32([[1, 0, x], [0, 1, y]])
    # Lakukan translasi menggunakan warpAffine
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Tentukan jumlah piksel untuk translasi (misalnya: 50 piksel ke kanan dan 30 piksel ke bawah)
    x_translation = 50
    y_translation = 30
    
    # Lakukan translasi gambar
    translated_image = translate_image(image, x_translation, y_translation)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_translated.png', translated_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_translated.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
