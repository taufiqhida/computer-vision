import cv2

# Fungsi untuk mengonversi gambar ke mode RGB
def convert_to_rgb(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Lakukan pemrosesan gambar di sini (misalnya: deteksi wajah, filter, dll)
    
    # Contoh: Mengonversi gambar ke mode RGB
    rgb_image = convert_to_rgb(image)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output.jpg', rgb_image)
    print("Gambar berhasil diproses dan disimpan.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
