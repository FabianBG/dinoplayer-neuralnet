import time
import cv2
import mss
import numpy as np
import keylogger
import pickle
from pynput import keyboard

state = {
    "space": False,
    "save": False,
    "reward": 1,
}


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.144])


def save(data):
    with open('train-data.pkl', 'wb') as output:
        pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)


def previewScreen():

    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {'top': 200, 'left': 200, 'width': 600, 'height': 200}
        while 'Screen capturing':
            last_time = time.time()
            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(monitor))
            cv2.imshow('Preview', img)

            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            # cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
            print('fps: {0}'.format(1 / (time.time()-last_time)))
            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break


def recordScreen(sleep=0.01, max_stack=3):
    keylogger.keyListener(state)
    stack = 0
    imgstack = {
        "stack": [],
        "value": [1, 0]
    }
    train_data = []
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {'top': 200, 'left': 200, 'width': 600, 'height': 200}

        while 'Screen capturing':
            last_time = time.time()
            time.sleep(sleep)
            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(monitor))
            gray = rgb2gray(img)
            if state["save"]:
                if stack == max_stack:
                    print(state["space"])
                    if state["space"]:
                        imgstack["value"] = [0, 1]
                    train_data.append(imgstack)
                    state["space"] = False
                    imgstack = {
                        "stack": [],
                        "value": [1, 0]
                    }
                    stack = 0

                gray = cv2.resize(gray, dsize=(120, 40),
                                  interpolation=cv2.INTER_CUBIC)
                print(np.average(gray))
                gray *= (255.0/gray.max())
                imgstack["stack"].append(gray)
                stack = stack + 1

            # Display the picture
            cv2.imshow('Preview', img)

            # Display the picture in grayscale
            # cv2.imshow('OpenCV/Numpy grayscale',
            # cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))
            print('fps: {0}'.format(1 / (time.time()-last_time)))
            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                save(train_data)
                break


def predictScreen(model, max_stack=3):
    stack = 0
    imgstack = {
        "stack": [],
        "value": [1, 0]
    }
    keylogger.keyListener(state)
    handler = keylogger.init_controller()
    with mss.mss() as sct:
        # Part of the screen to capture
        monitor = {'top': 200, 'left': 200, 'width': 600, 'height': 200}

        while 'Screen capturing':
            last_time = time.time()
            # Get raw pixels from the screen, save it to a Numpy array
            img = np.array(sct.grab(monitor))
            gray = rgb2gray(img)
            if state["save"]:
                if stack == max_stack:
                    pred = model.predict_classes(
                        np.array([np.stack(imgstack["stack"], axis=2)]))
                    if pred[0] == 1:
                        print("jump")
                        keylogger.pressSpace(handler)
                    state["space"] = False
                    imgstack = {
                        "stack": [],
                        "value": [1, 0]
                    }
                    stack = 0

                gray = cv2.resize(gray, dsize=(120, 40),
                                  interpolation=cv2.INTER_CUBIC)
                gray *= (255.0/gray.max())
                imgstack["stack"].append(np.array(gray)/255)
                stack = stack + 1

            # Press "q" to quit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
