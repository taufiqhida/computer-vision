import cv2

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Resize gambar menjadi ukuran 30x30 piksel
    resized_image = cv2.resize(image, (120, 120))
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_resized_120.png', resized_image)
    print("Gambar berhasil diresize menjadi ukuran 120x120 piksel dan disimpan sebagai gambar_output_resized.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
