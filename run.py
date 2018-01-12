import cv2
from grip_ddcard import GripPipeline

def extra_processing(pipeline):
    center_x_positions = []
    center_y_positions = []
    widths = []
    heights = []

    # Find the bounding boxes of the contours to get x, y, width, and height
    for contour in pipeline.filter_contours_output:
        x, y, w, h = cv2.boundingRect(contour)
        center_x_positions.append(x + w / 2)  # X and Y are coordinates of the top-left corner of the bounding box
        center_y_positions.append(y + h / 2)
        widths.append(w)
        heights.append(y)
    
    # Print output
    print("center X: ", center_x_positions)
    print("center Y: ", center_y_positions)
    print("width: ", widths)
    print("height: ", heights)

def main():
    print('Creating Video Capture')
    cap = cv2.imread('target.jpg')

    print('Creating Pipeline')
    pipeline = GripPipeline()

    print('Running Pipeline')
    pipeline.process(cap)
    extra_processing(pipeline)

    print('Capture Closed')


if __name__ == '__main__':
    main()
