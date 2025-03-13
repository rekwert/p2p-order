from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Загрузка изображения
image = Image.open('input_image.png')
width, height = image.size

# Преобразование изображения в массив NumPy для анализа пикселей
image_array = np.array(image)

# Определение цветов и соответствующих им чисел
color_to_number = {
    (165, 42, 42): 2,  # Коричневый
    (255, 255, 0): 1,  # Жёлтый
    (255, 0, 0): 3,    # Красный
    (0, 255, 0): 4,    # Зеленый
    (0, 0, 255): 5,    # Синий
    (255, 255, 255): 6,# Белый
    (128, 0, 0): 7,    # Темно-красный
    (0, 0, 128): 8,    # Темно-синий
    (255, 165, 0): 9,  # Оранжевый
    (0, 255, 255): 10  # Голубой
}

# Создание нового изображения для результата
result_image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(result_image)

# Функция для определения цвета треугольника по его центру
def get_triangle_color(x, y):
    return tuple(image_array[y, x])

# Функция для вставки числа в треугольник
def draw_number_in_triangle(draw, number, x, y, font):
    text = str(number)
    # Используем textbbox для получения размеров текста
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]  # Ширина текста
    text_height = bbox[3] - bbox[1]  # Высота текста
    text_x = x - text_width // 2
    text_y = y - text_height // 2
    draw.text((text_x, text_y), text, fill="black", font=font)

# Проходим по каждому пикселю и определяем цвет треугольника
for y in range(height):
    for x in range(width):
        color = get_triangle_color(x, y)
        if color in color_to_number:
            number = color_to_number[color]
            draw_number_in_triangle(draw, number, x, y, ImageFont.truetype("arial.ttf", 10))

# Сохраняем результат
result_image.save('output_image.png')
print("Результат сохранен в файл: output_image.png")