from PIL import Image
import random

def shuffle_pixels(image, key):
    random.seed(key)
    width, height = image.size
    pixels = [(x, y) for x in range(width) for y in range(height)]
    random.shuffle(pixels)
    return pixels

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = image.load()
    
    shuffle_order = shuffle_pixels(image, key)
    
    encrypted_image = Image.new('RGB', image.size)
    encrypted_pixels = encrypted_image.load()
    
    width, height = image.size
    
    random.seed(key + 1) 
    random_numbers = [random.randint(0, 255) for _ in range(width * height * 3)]
    rand_idx = 0
    
    for i, (x, y) in enumerate(shuffle_order):
        r, g, b = pixels[x, y]
        
        encrypted_r = (r ^ random_numbers[rand_idx]) % 256
        rand_idx += 1
        encrypted_g = (g ^ random_numbers[rand_idx]) % 256
        rand_idx += 1
        encrypted_b = (b ^ random_numbers[rand_idx]) % 256
        rand_idx += 1
        
        new_x, new_y = shuffle_order[i]
        encrypted_pixels[new_x, new_y] = (encrypted_r, encrypted_g, encrypted_b)
    
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")
    
    return shuffle_order

def decrypt_image(input_image_path, output_image_path, key, shuffle_order):
    image = Image.open(input_image_path)
    pixels = image.load()
    
    decrypted_image = Image.new('RGB', image.size)
    decrypted_pixels = decrypted_image.load()
    
    width, height = image.size
    
    random.seed(key + 1)
    random_numbers = [random.randint(0, 255) for _ in range(width * height * 3)]
    rand_idx = 0
    
    for i, (x, y) in enumerate(shuffle_order):
        encrypted_r, encrypted_g, encrypted_b = pixels[x, y]
        
        decrypted_r = (encrypted_r ^ random_numbers[rand_idx]) % 256
        rand_idx += 1
        decrypted_g = (encrypted_g ^ random_numbers[rand_idx]) % 256
        rand_idx += 1
        decrypted_b = (encrypted_b ^ random_numbers[rand_idx]) % 256
        rand_idx += 1
        
        original_x, original_y = shuffle_order[i]
        decrypted_pixels[original_x, original_y] = (decrypted_r, decrypted_g, decrypted_b)
    
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

input_image_path = "./car mage3.jpg" #Image path
encrypted_image_path = "./encrypted_image.png"
decrypted_image_path = "./decrypted_image.png"
encryption_key = 42 #Example Key

shuffle_order = encrypt_image(input_image_path, encrypted_image_path, encryption_key)

decrypt_image(encrypted_image_path, decrypted_image_path, encryption_key, shuffle_order)