import os

KAGGLE_USERNAME = ""
KAGGLE_KEY = ""

TEST_CLASSES = ["abiu", "acai", "acerola", "ackee", "ambarella"]

DATASET = "icebearogo/fruit-classification-dataset"
DEST = "data"
ZIP_PATH = os.path.join(DEST, "fruit-classification-dataset.zip")
CSV_DIR = os.path.join(DEST, "csv")
RAW_DIR = os.path.join(DEST, "raw")

TRAIN_DIR = os.path.join(RAW_DIR, "train1")
VAL_DIR = os.path.join(RAW_DIR, "val1")
TEST_DIR = os.path.join(RAW_DIR, "test1")

IMG_SIZE = (224, 224)
BATCH_SIZE = 16
EPOCHS = 5   
MODEL_PATH = "fruit_model.h5"