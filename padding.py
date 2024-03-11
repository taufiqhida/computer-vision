import cv2
import numpy as np

# Fungsi untuk menambahkan padding pada gambar
def add_padding(image, top, bottom, left, right, color=(0, 0, 0)):
    padded_image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    return padded_image

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Tentukan ukuran padding untuk setiap sisi (misalnya: 20 piksel untuk setiap sisi)
    top_padding = 20
    bottom_padding = 20
    left_padding = 20
    right_padding = 20
    
    # Tentukan warna padding (default: hitam)
    padding_color = (0, 0, 0)
    
    # Tambahkan padding pada gambar
    padded_image = add_padding(image, top_padding, bottom_padding, left_padding, right_padding, padding_color)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_padded.png', padded_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_padded.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
