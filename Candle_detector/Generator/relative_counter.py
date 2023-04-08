import cv2

sizes = {
    'engulfing': 2,
    'rev-engulfing': 2,
    'three-line-strike': 4,
    'evening-star': 3,
}

def get_relative_bbox_cord(shape, cords):
    image_height = shape[0]
    image_width = shape[1]

    candles_width = cords[3] - cords[2]
    candles_height = cords[1] - cords[0]

    center_x = (cords[2] + cords[3])/2
    center_y = (cords[0] + cords[1])/2

    relative_center = (center_x/image_width, center_y/image_height)
    relative_width = candles_width/image_width
    relative_height = candles_height/image_height

    return (relative_center, relative_width, relative_height)


def get_bbox_cord(image):

    def __check_top(image, height, width):
        for y in range(height):
            for x in range(width):
                R,G,B = image[y, x]
                if R != 255 or G != 255 or B != 255:
                    return y - 1

    def __check_bottom(image, height, width):
        for y in reversed(range(height)):
            for x in range(width):
                R,G,B = image[y, x]
                if R != 255 or G != 255 or B != 255:
                    return y + 1

    def __check_left(image, height, width):
        for x in range(width):
            for y in range(height):
                R,G,B = image[y, x]
                if R != 255 or G != 255 or B != 255:
                    return x - 1

    def __check_right(image, height, width):
        for x in reversed(range(width)):
            for y in range(height):
                R,G,B = image[y, x]
                if R != 255 or G != 255 or B != 255:
                    return x + 1
    # grab the image dimensions
    height, width, channels = image.shape
    # loop over the image, pixel by pixel
    top = __check_top(image, height, width)
    bottom = __check_bottom(image, height, width)
    left = __check_left(image, height, width)
    right = __check_right(image, height, width)

    return (top, bottom, left, right)


def get_bbox_cord_with_background(image, formation_positions):

    def __check_top(image, left, right, height):
        for y in range(height):
            for x in range(left, right + 1):
                R,G,B = image[y, x]
                if R != 255 or G != 255 or B != 255:
                    return y - 1

    def __check_bottom(image, left, right, height):
        for y in reversed(range(height)):
            for x in range(left, right + 1):
                R,G,B = image[y, x]
                if R != 255 or G != 255 or B != 255:
                    return y + 1

    height, width, channels = image.shape
    this_column_candle = False
    last_column_candle = False
    no_candle = 0
    no_formation = 0
    formation_position = None
    formation_name = None

    formations_size = len(formation_positions)

    positions_list = []

    left,right,top,bottom = None, None, None, None
    tmp_left = None
    RGB = None

    if formations_size == 0:
        return positions_list
    else:
        formation_name = formation_positions[no_formation][0]
        formation_position = formation_positions[no_formation][1] + 1
        formation_end_position = formation_position + sizes[formation_name]
        print(formation_position, formation_end_position)

    for x in range(width):
        this_column_candle = False
        if tmp_left is not None:
            left = tmp_left
            tmp_left = None
        for y in range(height):
            B,G,R = image[y, x]
            if (int(R) + int(G) + int(B)) < 550:
                this_column_candle = True
                if not last_column_candle:
                    last_column_candle = True
                    if no_candle == formation_end_position:
                        print(x)
                        right = x - 4
                    if no_candle == formation_position:
                        if left is None:
                            print(x)
                            left = x - 4
                        else:
                            tmp_left = x - 4
                    no_candle += 1
                break
        if left is not None and right is not None:
            top = __check_top(image, left + 3, right - 3, height)
            bottom = __check_bottom(image, left + 3, right - 3, height)
            positions_list.append((top, bottom, left, right))
            left,right,top,bottom = None, None, None, None
            no_formation += 1
            if no_formation == formations_size:
                return positions_list
            else:
                formation_name = formation_positions[no_formation][0]
                formation_position = formation_positions[no_formation][1] + 1
                formation_end_position = formation_position + sizes[formation_name]
        if not this_column_candle:
            last_column_candle = False
    return positions_list
