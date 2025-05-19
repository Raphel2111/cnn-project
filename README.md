# Inventory Management with CNN and YOLOv8

This project implements a Convolutional Neural Network (CNN) and YOLOv8 for object detection and classification tasks, specifically aimed at improving inventory management. It includes data preprocessing, model training, evaluation, and integration with Supabase for data storage and analysis.

## Project Structure

```
cnn-project
├── app.py                 # Streamlit application for detection and visualization
├── data
│   ├── raw                # Raw dataset files (YOLOv8 format)
│   └── processed          # Processed dataset files ready for training
├── models
│   └── cnn_model.py       # CNN model architecture
├── notebooks
│   └── exploration.ipynb  # Jupyter notebook for exploratory data analysis
├── src
│   ├── data_preprocessing.py  # Data loading and preprocessing functions
│   ├── model_training.py      # Training logic for the CNN model
│   └── model_evaluation.py    # Model evaluation functions
├── supabase_config.py     # Configuration for Supabase integration
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd cnn-project
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Install YOLOv8:
   ```sh
   pip install ultralytics
   ```

4. Configure Supabase:
   - Update the `SUPABASE_URL` and `SUPABASE_KEY` in `supabase_config.py` with your Supabase project details.

## Dataset

The dataset is organized in YOLOv8 format and includes the following classes:
- `Glass`
- `Metal`
- `Paper`
- `Plastic`

Ensure the dataset is structured as follows:
```
data/raw/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

## Usage

### 1. Preprocess the Dataset
Done with Roboflow.

### 2. Train the YOLOv8 Model
Train the YOLOv8 model using the following script:
```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')  # Use a pre-trained YOLOv8 model
model.train(data='data/raw/data.yaml', epochs=50, imgsz=640, batch=16)
```

### 3. Evaluate the Model
Evaluate the trained model on the validation set:
```python
metrics = model.val()
print(metrics)
```

### 4. Run the Streamlit Application
Launch the Streamlit app to upload images, detect materials, and visualize results:
```sh
streamlit run app.py
```

### 5. Export and Analyze Data
- Export detection results to a CSV file using the app.
- Analyze detection statistics stored in Supabase.

## Features

- **Object Detection**: Detect and classify materials (Glass, Metal, Paper, Plastic) using YOLOv8.
- **Streamlit Integration**: User-friendly interface for uploading images and visualizing results.
- **Supabase Integration**: Store and retrieve detection statistics for further analysis.

## License

This project is licensed under the MIT License.