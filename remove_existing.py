import os

# Пути к папкам с исходными данными
source_folders = [
    'yolov8-price-tag-detection-dataset/images/train',
    'yolov8-price-tag-detection-dataset/images/test',
    'yolov8-price-tag-detection-dataset/images/val'
]

# Папка, из которой нужно удалить дублирующиеся изображения
target_folder = 'prepared_images'

# Создаем множество для хранения уникальных имен файлов
existing_files = set()

# Заполняем множество именами файлов из source_folders
for folder in source_folders:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith('.jpg'):
                existing_files.add(file)

# Проверяем каждый файл в target_folder и удаляем его, если он уже существует в source_folders
for file in os.listdir(target_folder):
    if file in existing_files:
        os.remove(os.path.join(target_folder, file))
        print(f"Файл {file} удален.")

print("Операция завершена.")
