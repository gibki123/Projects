# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:18:14 2020

@author: Maciej Król
"""
import pandas as pd
import mplfinance as fplt
import random
from random import  randint, uniform
from datetime import datetime, timedelta
import os
import pathlib
from os.path import join
import annotator
import cv2

mc = fplt.make_marketcolors(up='#26a69a', down='#ef5350', inherit=True)
custom_style = fplt.make_mpf_style(marketcolors=mc, gridcolor='#000000', facecolor='#000000',)


class CandlesGenerator:
    sizes = {
        'engulfing': 2,
        'rev-engulfing': 2,
        'three-line-strike': 4,
        'evening-star': 3,
    }

    ranges = {
        'engulfing': [{'Open': (0, 20), 'High': (10, 40), 'Low': (-30, -14.75), 'Close': (-15.25, -14.75)},
                      {'Open': (-20, -10), 'High': (20, 50), 'Low': (-30, -14.75), 'Close': (20, 40)}],

        'rev-engulfing': [{'Open': (0, 15), 'High': (20, 55), 'Low': (-15, 0), 'Close': (25, 45)},
                          {'Open': (15, 55), 'High': (25, 65), 'Low': (-20, 0), 'Close': (-15, 5)}],

        'three-line-strike':[{'Open': (0, 5), 'High': (0, 15), 'Low': (-35, -10), 'Close': (-25, -10)},
                          {'Open': (-30, -10), 'High': (-25, 0), 'Low': (-50, -30), 'Close': (-45, -30)},
                          {'Open': (-50, -30), 'High': (-45, -20), 'Low': (-65, -50), 'Close': (-65, -50)},
                          {'Open': (-75, -55), 'High': (5, 25), 'Low': (-75, -55), 'Close': (5, 15)}],

        'evening-star':[{'Open': (0, 10), 'High': (55, 70), 'Low': (-10, 10), 'Close': (50,65)},
                          {'Open': (70, 80), 'High': (70, 85), 'Low': (45, 70), 'Close': (50,70)},
                          {'Open': (50,60), 'High': (55,70), 'Low': (0, 40), 'Close': (10,40)}],
    }

    formations = {0 : 'engulfing', 1 : 'rev-engulfing', 2 : 'three-line-strike', 3 : 'evening-star'}

    no_candles = [20,25,30,35,40,50]


    def __generate_candle_set(self, candlestick_form = None):
        FORMATION_PROB = 0.03 + uniform(0.0,0.02)
        STARTING_VALUE = 0
        STARTING_VALUE_THRESH = 20 + randint(0,80)
        CANDLE_DIFFERENCE_THRESH = randint(0,20)
        HIGH_LOW_THRESH = 3
        THRESH_BETWEEN_CANDLES = 20
        MAX_CANDLE_HIGH = 30 + randint(0,40)
        MAX_CANDLE_VALUE = 100 + randint(0,300)
        SQUARE_UNI = 5

        candles = []
        last_candle = None
        candle = {}
        formation_positions = []

        candle = self.__generate_random_candles(STARTING_VALUE, STARTING_VALUE_THRESH, MAX_CANDLE_HIGH, HIGH_LOW_THRESH, SQUARE_UNI, MAX_CANDLE_VALUE)
        print(candle)
        last_close = candle['Close']
        candles.append(candle)

        num = randint(0, len(self.no_candles) - 1)
        if candlestick_form is None:
            i = 0
            while i < self.no_candles[num]:
                generate_formation = random.random() < FORMATION_PROB
                if generate_formation:
                    formation_name = self.formations[randint(0, len(self.formations) - 1)]
                    formation_positions.append((formation_name, i))
                    form_range = self.ranges[formation_name]
                    for j in range(self.sizes[formation_name]):
                        candle = self.__generate_given_candle(
                        (form_range[j]['Open'][0] + last_close, form_range[j]['Open'][1] + last_close),
                        (form_range[j]['High'][0] + last_close, form_range[j]['High'][1] + last_close),
                        (form_range[j]['Low'][0] + last_close, form_range[j]['Low'][1] + last_close),
                        (form_range[j]['Close'][0] + last_close, form_range[j]['Close'][1] + last_close))
                        candles.append(candle)
                        i += 1
                    last_close = candle['Close']
                else:
                    candle = self.__generate_random_candles(last_close, CANDLE_DIFFERENCE_THRESH, MAX_CANDLE_HIGH, HIGH_LOW_THRESH, SQUARE_UNI, MAX_CANDLE_VALUE)
                    last_close = candle['Close']
                    candles.append(candle)
                    i += 1
        else:
            i = 0
            while i < self.no_candles[num]:
                generate_formation = random.random() < FORMATION_PROB
                if generate_formation:
                    formation_positions.append((formation_name, i))
                    form_range = self.ranges[candlestick_form]
                    for j in range(self.sizes[candlestick_form]):
                        candle = self.__generate_given_candle(
                            (form_range[j]['Open'][0] + last_close, form_range[j]['Open'][1] + last_close),
                            (form_range[j]['High'][0] + last_close, form_range[j]['High'][1] + last_close),
                            (form_range[j]['Low'][0] + last_close, form_range[j]['Low'][1] + last_close),
                            (form_range[j]['Close'][0]  + last_close, form_range[j]['Close'][1]  + last_close))
                        candles.append(candle)
                        i += 1
                    last_close = candle['Close']
                else:
                    candle = self.__generate_random_candles(last_close, CANDLE_DIFFERENCE_THRESH, MAX_CANDLE_HIGH, HIGH_LOW_THRESH, SQUARE_UNI, MAX_CANDLE_VALUE)
                    last_close = candle['Close']
                    candles.append(candle)
                    i += 1
        return candles, formation_positions


    def __generate_random_candles(self, last_close, CANDLE_DIFFERENCE_THRESH, MAX_CANDLE_HIGH, HIGH_LOW_THRESH, SQUARE_UNI, MAX_CANDLE_VALUE):
        open = None
        drop_power = 50

        open = uniform(last_close - CANDLE_DIFFERENCE_THRESH, last_close + CANDLE_DIFFERENCE_THRESH)
        if open > MAX_CANDLE_VALUE:
            open = uniform(last_close - CANDLE_DIFFERENCE_THRESH - drop_power, last_close + CANDLE_DIFFERENCE_THRESH - drop_power)
        elif open < -MAX_CANDLE_VALUE:
            open = uniform(last_close - CANDLE_DIFFERENCE_THRESH + drop_power, last_close + CANDLE_DIFFERENCE_THRESH + drop_power)

        close = uniform(open - MAX_CANDLE_HIGH, open + MAX_CANDLE_HIGH)
        if close > MAX_CANDLE_VALUE:
            close = uniform(open - MAX_CANDLE_HIGH - drop_power, open + MAX_CANDLE_HIGH - drop_power)
        elif close < -MAX_CANDLE_VALUE:
            close = uniform(open - MAX_CANDLE_HIGH + drop_power, open + MAX_CANDLE_HIGH + drop_power)

        close = uniform(open - MAX_CANDLE_HIGH, open + MAX_CANDLE_HIGH)
        high, low = self.__generate_high_low(open, close, HIGH_LOW_THRESH, SQUARE_UNI)
        candle = {'Open' : open, 'Close' : close, 'High' : high, 'Low' : low}
        return candle


    def __generate_high_low(self, open, close, HIGH_LOW_THRESH, square_uni):
        method = randint(0,1)
        multiplicator = 3
        high, low = None, None
        if open >= close:
            if method == 0:
                square = uniform(0,multiplicator)
                high = open + HIGH_LOW_THRESH*(square**2)
                square = uniform(0,multiplicator-square_uni)
                low = close - HIGH_LOW_THRESH*(square**2)
            else:
                square = uniform(0,multiplicator)
                low = close - HIGH_LOW_THRESH*(square**2)
                square = uniform(0,multiplicator-square_uni)
                high = open + HIGH_LOW_THRESH*(square**2)
        else:
            if method == 0:
                square = uniform(0,multiplicator)
                high = close + HIGH_LOW_THRESH*(square**2)
                square = uniform(0,multiplicator-square_uni)
                low = open - HIGH_LOW_THRESH*(square**2)
            else:
                square = uniform(0,multiplicator)
                low = open - HIGH_LOW_THRESH*(square**2)
                square = uniform(0,3-square_uni)
                high = close + HIGH_LOW_THRESH*(square**2)
        return high, low


    def __generate_given_candle(self, open_range, high_range, low_range, close_range):
        candle = {}
        candle['Open'] = random.uniform(open_range[0], open_range[1])
        candle['Close'] = random.uniform(close_range[0], close_range[1])
        if candle['Open'] >= candle['Close']:
            candle['High'] = random.uniform(candle['Open'], high_range[1])
            candle['Low'] = random.uniform(low_range[0], candle['Close'])
        else:
            candle['High'] = random.uniform(candle['Close'], high_range[1])
            candle['Low'] = random.uniform(low_range[0], candle['Open'])
        return candle


    def __generate_dataframe(self, candlestick_form):
        df = pd.DataFrame(columns=['Open', 'High', 'Low', 'Close'])
        ranges = self.ranges[candlestick_form]
        for j in range(self.sizes[candlestick_form]):
            candle = self.__generate_given_candle(
                ranges[j]['Open'], ranges[j]['High'], ranges[j]['Low'], ranges[j]['Close'])
            df = df.append(candle, ignore_index=True)
        today = datetime.now()
        date = pd.date_range(today, today + timedelta(self.sizes[candlestick_form]-1), freq='D')
        df = df.set_index(date)
        return df


    def __generate_dataframe_with_background(self, candlestick_form = None):
        df = pd.DataFrame(columns=['Open', 'High', 'Low', 'Close'])
        candles, formation_positions = self.__generate_candle_set(candlestick_form)
        for candle in candles:
            df = df.append(candle, ignore_index=True)
        today = datetime.now()
        date = pd.date_range(today, today + timedelta(len(candles)-1), freq='D')
        df = df.set_index(date)
        return df, formation_positions


    def generate_samples(self, no_samples, candlestick_form = None, with_background=False):
        path = pathlib.Path().absolute() if candlestick_form is None else os.path.join(pathlib.Path().absolute(), candlestick_form)
        if not os.path.exists(path):
            os.mkdir(path)
        for i in range(no_samples):
            df = None
            formation_positions = None
            if with_background:
                df, formation_positions = self.__generate_dataframe_with_background(candlestick_form)
            else:
                df = self.__generate_dataframe(candlestick_form)
            image_path = os.path.join(path,'random_candles', ''.join(('candlestick_form', str(i), '.png')))
            fplt.plot(
                df,
                type='candle',
                style=custom_style,
                axisoff=True,
                # figscale=random.uniform(0.1, 1.0),
                # figratio=self.figratios[self.sizes[candlestick_form]],
                savefig=image_path,
            )
            im = cv2.imread(image_path)
            height, width, channels = im.shape
            left = 160
            right = 700
            im_cropped = im[0:height, left:right]
            cv2.imwrite(image_path,im_cropped)
            txt_name = ''.join(('candlestick_form', str(i), '.txt'))
            annotator.create_train_txt_with_background(im_cropped, formation_positions, txt_name)


# generator = CandlesGenerator()
# generator.generate_samples(4000, candlestick_form = None, with_background=True)
annotator.create_train_txt_for_bacground_txts()


# generator.generate_samples('engulfing', 1000)
# print('engulfing done')
# generator.generate_samples('rev-engulfing', 1000)
# print('rev-engulfing done')
# generator.generate_samples('three-line-strike', 1000)
# print('three-line-strike done')
# generator.generate_samples('evening-star', 1000)
# print('evening-star done')
#
#
# generator.create_annotation_files()
# print('annotation files done')
# generator.create_train_txts()
# print('train_txt files done')
# annotator.create_train_txts(generator.sizes.keys())
