import cv2

# Fungsi untuk melakukan flipping gambar
def flip_image(image, flip_code):
    flipped_image = cv2.flip(image, flip_code)
    return flipped_image

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Tentukan kode flipping (0 untuk flipping sepanjang sumbu x, 1 untuk flipping sepanjang sumbu y, -1 untuk flipping sepanjang kedua sumbu)
    flip_code = 1
    
    # Lakukan flipping gambar
    flipped_image = flip_image(image, flip_code)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_flipped.png', flipped_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_flipped.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
