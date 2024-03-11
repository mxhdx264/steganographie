from PIL import Image
import numpy


def lsb1(image_path, message, password):
    image_to_watermark = Image.open(image_path)
    array_image_to_watermark = numpy.array(image_to_watermark)
    array_image_to_watermark = array_image_to_watermark - array_image_to_watermark % 2 # Step 1

    # Chiffrement du message avec Vigenère
    encrypted_message = vigenere_encrypt(message, password)

    # Conversion du message chiffré en binaire
    binary_message = ''.join(format(ord(char), '08b') for char in encrypted_message)

    # Embedding du message chiffré dans l'image
    number_rows, number_columns, number_channels = array_image_to_watermark.shape
    index_binary_message = 0
    for index_row in range(number_rows):
        for index_column in range(number_columns):
            for index_channel in range(number_channels):
                if index_binary_message < len(binary_message):
                    array_image_to_watermark[index_row, index_column, index_channel] += int(binary_message[index_binary_message])
                    index_binary_message += 1 
                else:
                    break

    # Enregistrement de l'image avec le message caché
    watermarked_image = Image.fromarray(array_image_to_watermark)
    watermarked_image.save('watermarked_image.png')

def extract_message(watermarked_image_path, password):
    watermarked_image = Image.open(watermarked_image_path)
    array_watermarked_image = numpy.array(watermarked_image)
    array_watermarked_image %= 2

    # Extraction du message binaire caché dans l'image
    binary_message = [str(binary_value) for binary_value in array_watermarked_image.flatten()]
    for index_binary_char in range(0, len(binary_message), 8):
        if binary_message[index_binary_char : index_binary_char+8] == ["0"]*8:
            binary_message = "".join(binary_message[:index_binary_char])
            break

    # Conversion du message binaire en message texte
    encrypted_message = ''.join(binary_message)
    decrypted_message = vigenere_decrypt(encrypted_message, password)
    print("Decrypted Message:", decrypted_message)

def vigenere_encrypt(message, key):
    encrypted_message = ""
    key_index = 0
    for char in message:
        encrypted_char = chr((ord(char) + ord(key[key_index])) % 256)
        encrypted_message += encrypted_char
        key_index = (key_index + 1) % len(key)
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ""
    key_index = 0
    for char in encrypted_message:
        decrypted_char = chr((ord(char) - ord(key[key_index])) % 256)
        decrypted_message += decrypted_char
        key_index = (key_index + 1) % len(key)
    return decrypted_message

lsb1(image_path="./aladin.jpg", message="Nous avons réussi à coder le lsb1 en moins d'1h", password="secret_key")
extract_message(watermarked_image_path="watermarked_image.png", password="secret_key")

# def lsb1(image_path, message, password):
# 	image_to_watermark = Image.open(image_path)

# 	array_image_to_watermark = numpy.array(image_to_watermark)

# 	array_image_to_watermark = array_image_to_watermark - array_image_to_watermark % 2 # step 1


# 	binary_message = ''.join(format(ord(carac), '08b') for carac in message)

# 	number_rows, number_columns, number_canals = array_image_to_watermark.shape
# 	index_binary_message = 0
# 	for index_row in range(0, number_rows):
# 		for index_column in range(0, number_columns):
# 			for index_canal in range(0, number_canals):
# 				if index_binary_message < len(binary_message):
# 					array_image_to_watermark[index_row, index_column, index_canal] += int(binary_message[index_binary_message])
# 					index_binary_message += 1 
# 				else:
# 					break

# 	watermarked_image = Image.fromarray(array_image_to_watermark)
# 	watermarked_image.save('watermarked_image.png')



# def extract_message(watermarked_image_path, password):
# 	watermarked_image = Image.open(watermarked_image_path)

# 	array_watermarked_image = numpy.array(watermarked_image)

# 	array_watermarked_image %= 2
# 	binary_message = [str(binary_value) for binary_value in array_watermarked_image.flatten()]
# 	for index_binary_carac in range(0, len(binary_message), 8):
# 		if binary_message[index_binary_carac : index_binary_carac+8] == ["0"]*8:
# 			binary_message = "".join(binary_message[:index_binary_carac])
# 			break


# 	message = "".join([chr(int(binary_message[index_binary_carac : index_binary_carac + 8],2))for index_binary_carac in range(0, len(binary_message), 8)])
# 	print(message)

# lsb1(image_path="./aladin.jpg", message="Nous avons réussi à coder le lsb1 en moins d'1h", password=None)
# extract_message(watermarked_image_path="watermarked_image.png", password=None)
