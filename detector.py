from ultralytics import YOLO
from collections import Counter

# Carga el modelo una vez
model = YOLO(r"C:\Users\Rafa\Desktop\cuarto año\TFG\TFG\cnn-project\data\raw\runs\detect\train\weights\best.pt")

def detectar_objetos(imagen_path):
    results = model(imagen_path)[0]
    img_array = results.plot()

    names = model.names
    detections = [names[int(cls)] for cls in results.boxes.cls]
    counts = Counter(detections)

    return img_array, counts
