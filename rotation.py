import cv2

# Fungsi untuk melakukan rotasi gambar
def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Tentukan sudut rotasi (misalnya: 45 derajat)
    angle = 45
    
    # Lakukan rotasi gambar
    rotated_image = rotate_image(image, angle)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_rotated.png', rotated_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_rotated.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
