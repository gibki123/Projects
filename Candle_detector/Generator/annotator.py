"""
Created on Thu Dec 04 15:36:28 2020

@author: Maciej Król
"""
import pathlib
import os
import cv2
from os import listdir
from os.path import isfile, join
from relative_counter import get_bbox_cord, get_relative_bbox_cord, get_bbox_cord_with_background

classes = {'engulfing' : 0, 'rev-engulfing' : 1, 'three-line-strike' : 2, 'evening-star' : 3}

def create_train_txts(formations):
    path = pathlib.Path().absolute()
    with open(join(path, 'candles_train.txt'), 'w') as train_txt:
        for i, formation in enumerate(formations):
            jpeg_path = join(path, str(formation))
            jpegs = [f for f in listdir(jpeg_path) if isfile(join(jpeg_path, f))]
            for jpeg in jpegs:
                train_txt.write(join(f'data\\candles\\{formation}\\{jpeg}\n'))
                with open(join(path,formation,''.join((os.path.splitext(jpeg)[0], '.txt'))), 'w') as jpeg_file:
                    image = cv2.imread(join(path,formation,jpeg))
                    cords = get_bbox_cord(image)
                    rel_cords = get_relative_bbox_cord(image.shape, cords)
                    jpeg_file.write(' '.join((str(i), str(rel_cords[0][0]), str(rel_cords[0][1]), str(rel_cords[1]), str(rel_cords[2]), '\n')))


def create_train_txt_with_background(image, formation_positions, txt_name):
    path = pathlib.Path().absolute()
    with open(os.path.join(path,'train_txts',txt_name), 'w') as annotation_file:
        cords = get_bbox_cord_with_background(image, formation_positions)
        print(cords, formation_positions)
        for cord, formation_position in zip(cords, formation_positions):
            rel_cords = get_relative_bbox_cord(image.shape, cord)
            annotation_file.write(' '.join((str(classes[formation_position[0]]), str(rel_cords[0][0]), str(rel_cords[0][1]), str(rel_cords[1]), str(rel_cords[2]), '\n')))


def create_train_txt_for_bacground_txts():
    path = pathlib.Path().absolute()
    jpeg_path = os.path.join(path,'random_candles')
    with open(os.path.join(path,'candles_train.txt'), 'w') as candles_train_file:
        jpegs = [f for f in listdir(jpeg_path) if isfile(join(jpeg_path, f))]
        for jpeg in jpegs:
            candles_train_file.write(''.join((os.path.join('data','candles','random_candles',jpeg),'\n')))

def create_annotation_files(formations):
    path = pathlib.Path().absolute()
    with open(join(path, 'candles.names'), 'w') as names_file:
        for formation in formations:
            names_file.write(formation + '\n')
    with open(join(path, 'candles.data'), 'w') as data_file:
        data_file.write(''.join(('classes = ',str(len(self.sizes.keys())),'\n')))
        data_file.write('train = data/candles_train.txt\n')
        data_file.write('valid = data/candles_test.txt\n')
        data_file.write('names = data/candles.names\n')
        data_file.write('backup = backup/\n')
