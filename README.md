# Dino game neural net

A simpleneural net to play chrome offline dino game. You can generate the data and train a neural net to 
play the game for you, it is very simple aproach but it is a firts stepto the more complex state of the art 
models like deep reinformcementlearning.

It generate the data taking screen shoots of the navigator and listening when you press space to jump, then 
this data is used to learn when to trigger the space key, and finally it uses the trained model to predict if
it time to jump.

## Requirements
 * python3

You have to install all this libraries before any usage of this code:

 * tensorflow
 * tensorflow-gpu
 * pynput
 * opencv
 * mss
 * numpy

It is very recomended to have *a GPU* for a better performance and preview.

## Usage

First of all you need to open google chrome on [crome://dino].

Then in the folder of this code execute the next command:
`python3 main.py preview` 
It show the preview of the area which the code take the screenshoots so move the navigator with the game to fit the preview.

![preview](https://github.com/FabianBG/dinoplayer-neuralnet/blob/master/docs/dino1.png?raw=true)


When the screenshoot area is setted, the command will generate the train data:
`python3 main.py gen-data`
To start recording data *press the key i*, adn to stop *key e*, and to save the data on the preview window press the *key q*.

It will generate a data-train.pkl file on the folder. This contains the train data for you model.

Next step is to train the model, so just exec:
`python3 main.py train`

![train](https://github.com/FabianBG/dinoplayer-neuralnet/blob/master/docs/dino2.png?raw=true)

When all the train is donne it saves a *model.tf* file which has the trained model.

Finally to see how it does, execute
`python main.py predict`

And to start predicting press *press the key i* start the game and let the computer tries to do its best.

![sample](https://github.com/FabianBG/dinoplayer-neuralnet/blob/master/docs/dino3.gif?raw=true)


## NEXT STEPS
The neuralnet it is very simple, it can be improved in many ways, and apply more stateof the art models to
comprea which is best.


## LICENCE
MIT
