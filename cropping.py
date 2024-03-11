import cv2

# Fungsi untuk melakukan pemotongan gambar (cropping)
def crop_image(image, x, y, width, height):
    return image[y:y+height, x:x+width]

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Tentukan koordinat dan ukuran kotak pemotongan
    x = 100  # Koordinat x pojok kiri atas kotak pemotongan
    y = 50   # Koordinat y pojok kiri atas kotak pemotongan
    width = 200  # Lebar kotak pemotongan
    height = 150 # Tinggi kotak pemotongan
    
    # Lakukan pemotongan gambar
    cropped_image = crop_image(image, x, y, width, height)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_cropped.png', cropped_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_cropped.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
