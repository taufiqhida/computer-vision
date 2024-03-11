import cv2
import numpy as np

# Fungsi untuk melakukan perspective transformasi pada gambar
def perspective_transform(image, src_points, dst_points):
    # Membuat matriks transformasi perspektif
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    # Melakukan perspektif transformasi
    transformed_image = cv2.warpPerspective(image, matrix, (image.shape[1], image.shape[0]))
    return transformed_image

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Tentukan titik-titik sudut pada gambar asli dan gambar hasil yang ingin Anda capai
    # Misalnya, untuk melakukan perspektif transformasi ke gambar persegi panjang yang diinginkan
    src_points = np.float32([[0, 0], [image.shape[1], 0], [image.shape[1], image.shape[0]], [0, image.shape[0]]])
    dst_points = np.float32([[0, 0], [300, 0], [300, 400], [0, 400]])  # Contoh titik-titik pada gambar hasil
    
    # Lakukan perspective transformasi pada gambar
    transformed_image = perspective_transform(image, src_points, dst_points)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_perspective_transformed.png', transformed_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_perspective_transformed.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
