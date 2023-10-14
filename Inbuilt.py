#EE596
#Lab 01 - Huffman Code
#ChiranjithD
#Huffman Inbuilt

import numpy as np
from PIL import Image
import dahuffman as dh

# Load the RGB image using a library like Pillow
image = Image.open('Parrots-680x680.jpg')
pixels = np.array(image)

# Convert the 3D RGB array into a 1D array of pixel values
pixel_values = pixels.flatten().tolist()

counts = np.bincount(pixel_values)

# Calculate the probability of each pixel value
probs = counts / len(pixel_values)

# Calculate the entropy of the source
entropy = -np.sum(probs * np.log2(probs))
print('Inbuilt Huffman Image Entropy: ', entropy)

# Use the dahuffman library to generate the Huffman codes and compress the pixel values
encoder = dh.HuffmanCodec.from_data(pixel_values)
compressed_bits = encoder.encode(pixel_values)

#print(compressed_bits)
code_table = encoder.get_code_table()
for symbol, code in code_table.items():
    print(f'Symbol: {symbol}, Code: {code}')

# Write the compressed bits to a file
with open('compressed.txt', 'wb') as f:
    f.write(compressed_bits)

#print('Compressed bits:')
#print(compressed_bits.hex())

# To decompress the image
with open('compressed.bin', 'rb') as f:
    compressed_bits = f.read()


# To decompress the image
with open('compressed.bin', 'rb') as f:
    compressed_bits = f.read()

#encoder.decode(compressed_bits)

decompressed_pixel_values = encoder.decode(compressed_bits)
decompressed_pixels = np.array(decompressed_pixel_values, dtype=np.uint8).reshape(pixels.shape)

# Convert the pixel values back into an image using a library like Pillow
decompressed_image = Image.fromarray(decompressed_pixels)
decompressed_image.show()


compressed_file_size = len(compressed_bits)
compression_ratio = 680*680*8 / (compressed_file_size)
print(compression_ratio)
