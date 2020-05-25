import recorder
import net
import keylogger
import tensorflow as tf
import sys
import pickle

if __name__ == "__main__":
    # keylogger.keyListener()
    args = sys.argv
    if args[1] == "preview":
        recorder.previewScreen()
    if args[1] == "gen-data":
        print("Press key i to start and e to stop")
        recorder.recordScreen()
    if args[1] == "train":
        with open('train-data.pkl', 'rb') as f:
            data = pickle.load(f)
            model = net.gen_model()
            net.train_model(model, data)
    if args[1] == "predict":
        model = tf.keras.models.load_model('model.tf')
        recorder.predictScreen(model)
