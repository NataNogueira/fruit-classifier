import os

KAGGLE_USERNAME = ""
KAGGLE_KEY = ""

DATASET = "icebearogo/fruit-classification-dataset"
DEST = "data"
ZIP_PATH = os.path.join(DEST, "dataset.zip")
CSV_DIR = os.path.join(DEST, "csv")
RAW_DIR = os.path.join(DEST, "raw")

TRAIN_DIR = os.path.join(RAW_DIR, "train1")
VAL_DIR = os.path.join(RAW_DIR, "val1")
TEST_DIR = os.path.join(RAW_DIR, "test1")

IMG_SIZE = (100, 100)
BATCH_SIZE = 32
EPOCHS = 10
MODEL_PATH = "fruit_model.h5"