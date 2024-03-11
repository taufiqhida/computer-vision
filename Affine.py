import cv2
import numpy as np

# Fungsi untuk melakukan affine transformasi pada gambar
def affine_transform(image, matrix):
    # Mendapatkan ukuran gambar
    height, width = image.shape[:2]
    # Melakukan affine transformasi
    transformed_image = cv2.warpAffine(image, matrix, (width, height))
    return transformed_image

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Tentukan matriks transformasi affine (misalnya: scaling sebesar 2 di sumbu x, dan translasi 50 piksel di sumbu y)
    matrix = np.float32([[2, 0, 0], [0, 1, 50]])
    
    # Lakukan affine transformasi pada gambar
    transformed_image = affine_transform(image, matrix)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_affine_transformed.png', transformed_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_affine_transformed.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
