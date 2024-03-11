import cv2

# Load gambar menggunakan OpenCV
image = cv2.imread('aku1.png')

# Cek apakah gambar berhasil dimuat
if image is not None:
    # Memisahkan kanal warna
    blue_channel, green_channel, red_channel = cv2.split(image)
    
    # Simpan setiap kanal warna sebagai gambar terpisah
    cv2.imwrite('blue_channel.png', blue_channel)
    cv2.imwrite('green_channel.png', green_channel)
    cv2.imwrite('red_channel.png', red_channel)
    
    print("Kanal warna berhasil dipisahkan dan disimpan sebagai blue_channel.png, green_channel.png, dan red_channel.png.")
else:
    print("Gagal memuat gambar. Pastikan path gambar yang diberikan benar.")
