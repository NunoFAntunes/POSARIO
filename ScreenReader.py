# importing the required packages
import pyautogui
import cv2
import numpy as np
import easyocr
import ReaderUtils
import yaml
import logging

# Starts logger
logger = logging.getLogger(__name__)


def run(test_mode):
    # Specify resolution
    resolution = (1920, 1080)

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"XVID")

    # Specify name of Output file
    filename = "Recording.avi"

    # Specify frames rate. We can choose
    # any value and experiment with it
    fps = 1.0

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # Create an Empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    
    # Resize this window
    cv2.resizeWindow("Live", 1920, 1080)

    reader = easyocr.Reader(['en', 'pt']) # this needs to run only once to load the model into memory

    while True:
    
        # Take screenshot using PyAutoGUI
        #img = pyautogui.screenshot(region=(1080,500,1920,1080))
        if test_mode:
            img = pyautogui.screenshot(region=(3840,1100,1920,1080))
        else:
            img = pyautogui.screenshot(region=(4100,1130,1150,880))
    
        # Convert the screenshot to a numpy array
        frame = np.array(img)
    
        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        # Write it to the output file
        out.write(frame)
        
        output = reader.readtext(frame)
        print(output)
        
        image_with_bboxes = ReaderUtils.create_bounding_boxes(frame, output)
        
        
        # Optional: Display the recording screen
        cv2.imshow('Live', image_with_bboxes)
        
        # Stop recording when we press 'q'
        if cv2.waitKey(1) == ord('q'):
            break
        
    # Release the Video writer
    out.release()
    
    # Destroy all windows
    cv2.destroyAllWindows()
    
if __name__ == '__main__':
    
    # Loads config file
    logger.info('Fetching config file parameters')
    config_path = 'params.yaml'
    config=yaml.safe_load(open(config_path))
    is_test_mode = config['global_configurations']['test_mode']
    run(is_test_mode)