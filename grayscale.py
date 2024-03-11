import cv2

# Fungsi untuk mengonversi gambar ke mode Grayscale
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Lakukan pemrosesan gambar di sini (misalnya: deteksi wajah, filter, dll)
    
    # Contoh: Mengonversi gambar ke mode Grayscale
    grayscale_image = convert_to_grayscale(image)
    
    # Simpan gambar hasil
    cv2.imwrite('gambar_output_grayscale.png', grayscale_image)
    print("Gambar berhasil diproses dan disimpan sebagai gambar_output_grayscale.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
