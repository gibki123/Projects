import os
import pathlib
import cv2

sys.path.append("../../darknet/")
import darknet as dn
import darknet_images as dimgs

NETWORK = None
CLASS_NAMES = None
COLORS = None
PROJECT_PATH = None
BATCH_SIZE = 1


def load_darknet():
    global NETWORK, CLASS_NAMES, COLORS, PROJECT_PATH, BATCH_SIZE
    PROJECT_PATH = pathlib.Path().absolute()
    config_path = os.path.join(PROJECT_PATH,'candles-obj.cfg')
    data_path = os.path.join(PROJECT_PATH,'candles.data')
    weights_path = os.path.join(PROJECT_PATH,'weights','candles-obj_2000.weights')
    NETWORK, CLASS_NAMES, COLORS = dn.load_network(
                                                config_file = config_path,
                                                data_file = data_path,
                                                weights = weights_path,
                                                batch_size = BATCH_SIZE)
    print(CLASS_NAMES)
    print(COLORS)


def detect_candles():
    image_path = os.path.join(PROJECT_PATH, 'screen_candle.png')
    image, detections = dimgs.image_detection(image_path, NETWORK, CLASS_NAMES,
                                           COLORS, thresh = 0.2)
    cv2.imwrite(f'output_screen_candle.png', image)
    print(detections)
