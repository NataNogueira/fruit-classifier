import os

DATASET = "icebearogo/fruit-classification-dataset"
DEST = "data"
ZIP_PATH = os.path.join(DEST, "fruit-classification-dataset.zip")
CSV_DIR = os.path.join(DEST, "csv")
RAW_DIR = os.path.join(DEST, "raw")
DATASET_URL = "https://www.kaggle.com/api/v1/datasets/download/icebearogo/fruit-classification-dataset"
TRAIN_DIR = os.path.join(RAW_DIR, "train1")
VAL_DIR = os.path.join(RAW_DIR, "val1")
TEST_DIR = os.path.join(RAW_DIR, "test1")

IMG_SIZE = (100, 100)
BATCH_SIZE = 32
EPOCHS = 10
MODEL_PATH = "fruit_model.h5"