# NeurotechX - 2018
This repository contains all code that will be submitted to the Neurotech 2018 student competition.
The idea behind this project is to explore the ability to read brain signals and interpret them in a meaningful way.
To show this, we are using a Muse headband to read signals and a MeArm robotic arm as a system to control. The aim of this project 
will be to read a signal to halt the automated motion of a robotic arm.

## Procedure & Setup
## MeArm
This project works with a MeArm controlled with an Arduino using the MeArm library we developed:

https://github.com/SamuelSVD/MeArm

To set up the MeArm we purchased a MeArm v1.02 and an arduino Uno kit. The Arduino was programmed using the setup method as described in the MeArm library then a set of positions in which the robot should move in. We've pre-programmed the robot to move in a predetermined pattern (See mearm_controller.py, dance) that will repeat forever until a signal to halt motion is read. When halt is called, the controller will not send control messages until the resume signal is called again.

### Muse
Using muse headband with the help of the muse-lsl library: 

https://github.com/alexandrebarachant/muse-lsl

To set up the Muse we acquired a Muse headband and downloaded the muse-lsl library. This helped us build our competencies with the muse, however we did not end up using it for our final product.

Originally, we'd throught use use some of the stimuli in the muse-lsl library and use SSEVP waves. Instead, we decided to use SVM to classify brain waves and control the robot by thinking to move left/right hand.

## Streaming  Muse Data: Muse Direct
We used Muse Direct to start the OSC stream. We used the default UBP port. 

First, you plug in the BLED 112 dongle and ensure that the bluetooth connection between the muse and the computer is secure. 

![capture1](https://user-images.githubusercontent.com/35237911/37561356-19815fec-2a23-11e8-832d-9cc3819e0bdf.JPG)

Next, open up Muse Direct and turn the bluetooth connection on. Wait until the icon stops blinking and is stable. Then, turn on the record button and to  open the OSC stream. Then open up MuseLab to visualize the data.

![capture2](https://user-images.githubusercontent.com/35237911/37561377-b698e00c-2a23-11e8-936f-e41da05b595d.PNG)

## Visualizing Data: Muse Lab

Next, we visualized the data in MuseLab using these steps:

1. ![capture3](https://user-images.githubusercontent.com/35237911/37561588-5d4af526-2a28-11e8-93a1-5d95c4dd19cf.PNG)

Establish the UDP port by entering 7000 and makeing sure you've selected the UDP option.

2. ![capture4](https://user-images.githubusercontent.com/35237911/37561597-bc298922-2a28-11e8-8c7d-327f11d9e40a.png)

Next, go into the drop down bar and select Visualizer. Select New and then Scrolling Line Graph. Click Finish, and then you can select which brain waves you'd like to view. For our purposes, we used the Filtered EEG group to collect our data.

## Collecting Data: MusePlayer and MatLab.
MusePlayer allows us to conver the .muse files into matlab files. We set up out Muse Player using this tutorial:
https://bitbucket.org/interaxon/museplayer/src/108658199aaa37c58f5c70dbd15e9a77e8e8191b/README.md?at=master&fileviewer=file-view-default

To collect the data using MatLab, we used this code for one second of data:
http://www.neuroeconlab.com/muse-data-collection.html

## Using SVM as a classifier:
Recording will be trials of the person imagining moving their right hand and their left hand. Collect frequency values for alpha, beta, gamma, theta and create a matrix where the columns correspond to the brain wave and the rows contain information about the imagined movement. Then, used a linear Support Vector Machine to classify the most salient brain wave.

## MatLab Arduino Interface

We're sending structured messages over a serial port depending on the signal we receive from the Muse.

Here's a good introductory tutorial: 
http://www.instructables.com/id/Arduino-and-Matlab-let-them-talk-using-serial-comm/

Then using MeArm github we created, we were able to get the arm to move using signals recieved from the Arduino.
