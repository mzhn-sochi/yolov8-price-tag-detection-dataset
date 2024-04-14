# YOLOv8 Price Tag Detection Dataset

## Добавление новых картинок

1. Добавляем картинки в форматах .jpeg, .jpg, .webp, .png в `input_images`;
2. Вызываем `python prepare_input.py`;
3. Вызываем `python remove_existing.py`;
4. Загружаем содержимое `prepared_images` в CVAT;
5. Размечаем таску;
6. Export (task) dataset YOLO 1.1 с Save image;
7. Распоковываем архив в cvat2yolo/my_dataset
8. В cvat2yolo:
```
python main_cvat2yolo.py --cvat my_dataset --mode autosplit --split 0.8 --train_folder obj_train_data --output_folder yolov8-price-tag-detection-dataset --img_format jpg
```
9. Перекидывам cvat2yolo/yolov8-price-tag-detection-dataset в репу