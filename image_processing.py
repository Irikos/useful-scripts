# Actually, image and video processing

# import packages
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2 as cv


# read the image and show it inline
# INPUT: image_path - the path to the image
# OUTPUT: none
def show_image(image_path):
    # load the image
    image = Image.open(image_path)

    # convert the image to a numpy array
    image = np.array(image)

    # show the image
    plt.imshow(image)
    plt.show()

# convert the image to grayscale
# INPUT: image_path - the path to the image
# OUTPUT: none
def convert_to_grayscale(image_path):
    # load the image
    image = Image.open(image_path)

    # convert the image to grayscale
    image = image.convert('L')

    # show the image
    plt.imshow(image, cmap='gray')
    plt.show()


# load video and return frames
# INPUT: video_path - the path to the video
#        verbose - whether or not to print information about the video
# OUTPUT: frames - the frames of the video

def load_video(video_path, verbose=False):
    # load the video
    video = cv.VideoCapture(video_path)

    # get the fps of the video
    fps = video.get(cv.CAP_PROP_FPS)

    # get the number of frames in the video
    num_frames = int(video.get(cv.CAP_PROP_FRAME_COUNT))

    # get the width and height of the video
    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))

    # print information about the video
    if verbose:
        print("fps: " + str(fps))
        print("num_frames: " + str(num_frames))
        print("width: " + str(width))
        print("height: " + str(height))

    # read the frames of the video
    frames = []
    for i in range(num_frames):
        ret, frame = video.read()
        frames.append(frame)

    # release the video
    video.release()

    if verbose:
        print("Loaded " + str(len(frames)) + " frames")

    return frames


# save frames to mp4 video file
# INPUT: frames - the frames of the video
#        fps - the fps of the video
#        output_path - the path to the output video
#        verbose - whether or not to print information about the video
# OUTPUT: path to the output video
def save_video(frames, fps, output_path, verbose=False):
    # get the width and height of the video
    width = frames[0].shape[1]
    height = frames[0].shape[0]

    # create the video writer
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    video = cv.VideoWriter(output_path, fourcc, fps, (width, height))

    # write the frames to the video
    for frame in frames:
        video.write(frame)

    # release the video
    video.release()

    if verbose:
        print("Saved video to " + output_path)

    return output_path

# read .txt with VOC bounding box:(image_name, x-top left, y-top left, x-bottom right, y-bottom right, label)
# INPUT: file_path - the path to the file
#        separator - the separator between the values in the file
#        verbose - whether or not to print information about the photo
# OUTPUT: image_names - the name of each image
#         bounding_boxes - the bounding boxes in VOC format
#         labels - the labels for each bounding box
def read_voc_file(file_path, separator=',', verbose=False):
    # open the file
    with open(file_path, 'r') as f:
        # read the lines of the file
        lines = f.readlines()

    # get the values from the lines
    image_names = []
    bounding_boxes = []
    labels = []
    for line in lines:
        # split the line
        values = line.split(separator)

        # get the values
        image_name = values[0]
        x_min = int(values[1])
        y_min = int(values[2])
        x_max = int(values[3])
        y_max = int(values[4])
        label = str(values[5]).strip() # as it is the last item, it has a newline

        # append the values
        image_names.append(image_name)
        bounding_boxes.append([x_min, y_min, x_max, y_max])
        labels.append(label)

    if verbose:
        print("Read " + str(len(image_names)) + " lines from " + file_path)

    return image_names, bounding_boxes, labels


# visualize Pascal VOC Bounding box:(x-top left, y-top left, x-bottom right, y-bottom right) on an image
# INPUT: image_path - the path to the image
#        bounding_boxe - the bounding box coordinates to draw on the image, in PASCAL VOC format: [x-top left, y-top left, x-bottom right, y-bottom right]
#        label - the label of the bounding box
#        color - the color of the bounding box
#        verbose - whether or not to print information about the photo
# OUTPUT: none
def visualize_bounding_box_voc(image_path, bounding_box, label, color=(255, 0, 0), verbose=False):
    # load the image
    image = Image.open(image_path)

    # convert the image to a numpy array
    image = np.array(image)

    # get the bounding box coordinates
    x_min = bounding_box[0]
    y_min = bounding_box[1]
    x_max = bounding_box[2]
    y_max = bounding_box[3]

    # draw the bounding box
    cv.rectangle(image, (x_min, y_min), (x_max, y_max), color, 2)

    # draw the label
    cv.putText(image, label, (x_min, y_min - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    # show the image
    plt.imshow(image)
    plt.show()

# change labels from string to numeric classes
# INPUT: labels - the labels to change
#        verbose - whether or not to print information about the photo
# OUTPUT: labels - the labels in numeric classes
def change_labels_to_numeric(labels, verbose=False):
    # get the unique labels
    unique_labels = np.unique(labels)
    numeric_labels = labels.copy()
    # create a dictionary to map the labels to numeric classes
    label_to_numeric = {}
    for i in range(len(unique_labels)):
        label_to_numeric[unique_labels[i]] = i

    # change the labels to numeric classes
    for i in range(len(labels)):
        numeric_labels[i] = label_to_numeric[labels[i]]

    if verbose:
        print("Changed labels to numeric classes")

    return numeric_labels