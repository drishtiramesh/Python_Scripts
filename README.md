Basic python scripts for various operations:

1. Automatic_frame_extract_ffmpeg.py : This python script extracts frames from a folder of videos and stores the images in specified folders. This is done using ffmpeg.

2. extract_frames.py : Extraction of images from video using cv2.

3. Create_XML_file_for_for_random_bounding_box.py: This python script takes a particular folder of images and creates an XML file for each image containing random bounding box coordinates for it.

4. Extract_Wrong_Detections.py: This python script compares the target and predicted output values recorded in an excel file and extract the wrong predictions. Then, a text file is created which contains all the wrongly predicted images with their path.

5. XML_to_Text.py: There are two forms of files which are used to record bounding box coordinates for an images- XML and Txt. This script converts a folder of XML files containing bounding box coordinates to a txt file.

6. Background_bounding_boxes.py: This python script reads an existing txt file with bounding box coordinates, and generates more bounding boxes in the background of the highlighted region(original bounding box) and appends the coordinate details of new background bounding boxes to the txt file.

6. Merge_2_Images.py: Script for weighted merging of two given images.


