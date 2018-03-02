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

To set up the Muse we acquired a Muse headband and downloaded the muse-lsl library.
Currently, this is still a work in progress.
