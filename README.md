# Simulton Simulation

## Overview
This project is a Python simulation built using the Model-View-Controller (MVC) design pattern, using inheritance and object-oriented programming principles. Users interact with a GUI to add various "simultons": simulated objects that move and interact within a canvas, each with distinct behaviors implemented via an inheritance hierarchy.

The model module defines classes representing different simultons. The view and controller modules handle the graphical display and user interaction using tkinter.

## Features

* Add and control different simulton types:
  * Ball: Moves in straight lines and bounces off walls.
  * Floater: Moves erratically, optionally displayed as a UFO image.
  * Black_Hole: Stationary; “eats” any prey within its radius.
  * Pulsator: A Black_Hole that grows when it eats and shrinks/starves otherwise.
  * Hunter: A mobile Pulsator that pursues the closest visible prey.
  * Special: A user-defined simulton with custom behavior.
* Simulation control buttons: Start, Stop, Step (advance one update), Remove, Reset.
* Responsive canvas that adapts to window resizing.
* Uses inheritance to minimize code duplication and promote clean, maintainable design.

## How to Run
Run the simulation via the main script:

```shell
python script.py
```
* Use the buttons at the top of the screen to select which simulton type to add.
* Click on the canvas to place simultons.
* Control the simulation with Start, Stop, Step, Remove, and Reset buttons
* Watch simultons move, interact, grow, shrink, and behave according to their rules.
