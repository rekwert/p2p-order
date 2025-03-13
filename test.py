from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Функция для проверки близости цветов
def is_close_color(color1, color2, threshold=10):
    return all(abs(c1 - c2) <= threshold for c1, c2 in zip(color1, color2))

# Функция для определения цвета треугольника по его центру
def get_triangle_color(x, y, image_array, unique_colors):
    pixel_color = tuple(image_array[y, x])
    for color in unique_colors:
        if is_close_color(pixel_color, color):
            return color
    return None

# Функция для вставки числа в треугольник
def draw_number_in_triangle(draw, number, x, y, font):
    text = str(number)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    text_x = x - text_width // 2
    text_y = y - text_height // 2
    draw.text((text_x, text_y), text, fill="black", font=font)

# Основной код
if __name__ == "__main__":
    # Загрузка изображения
    image = Image.open('input_image.png')
    width, height = image.size

    # Преобразование изображения в массив NumPy для анализа пикселей
    image_array = np.array(image)

    # Анализ изображения на цвета
    unique_colors = set()
    for y in range(height):
        for x in range(width):
            pixel_color = tuple(image_array[y, x])
            unique_colors.add(pixel_color)

    # Сопоставление цветов с цифрами
    color_to_number = {color: i + 1 for i, color in enumerate(unique_colors)}

    # Создание нового изображения для результата
    result_image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(result_image)

    # Загрузка шрифта
    try:
        font = ImageFont.truetype("arial.ttf", 10)  # Размер шрифта можно изменить
    except IOError:
        print("Шрифт 'arial.ttf' не найден. Убедитесь, что файл шрифта существует.")
        exit(1)

    # Проходим по каждому пикселю и определяем цвет треугольника
    for y in range(height):
        for x in range(width):
            color = get_triangle_color(x, y, image_array, unique_colors)
            if color is not None:
                number = color_to_number[color]
                draw_number_in_triangle(draw, number, x, y, font)

    # Сохраняем результат
    result_image.save('output_image.png')
    print("Результат сохранен в файл: output_image.png")