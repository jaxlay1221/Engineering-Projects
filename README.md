# Engineering Projects

Code from my personal projects involving imbedded devices, C++, and Python
I am a first-year Mechanical Engineering student with a Minor in Computer Science at Quincy University
I have interests in the fields of Aerospace, energy production, and robotics

# Arduino Analog Joystick Pong

Description: After completing this fundamental Arduino project, I wanted to put it to use for something more than printing a reading. This pong game displays directly on the serial monitor in the Arduino IDE. The analog joystick moves the paddle. This was a great project to teach me how to use readings from an input device in a complex manner. I relied on the assistance of AI to help me with code as this was different than any other project I have done before.

Features:
- Calibrates the center at the beginning of each run
- Creates a dead zone to avoid stick drift
- increases/decreases paddle speed based on joystick readings
- balls angle and speed varies by where the paddle hits it and how many times
- Keeps track of wins and losses based off of first to three misses loses. 

**Hardware:** Arduino UNO, analog joystick module (Y axis on A1, button on pin 7)

**To run:** upload `pong.ino`, open the Serial Monitor, and set it to 250000 baud.

# Q-learning Route Finder

Description: This is a worked example from the book _AI Crash Course_ by Hadelin De Ponteves. It was an eye-opening experience to me to see how Artificial Intelligence is applied in the real world. This example uses a matrix imported by numpy to simulate possible moves in a factory floor. The algorithm then navigates through the floorplan and finds the fastest way from a predetermined point to another. This is a 12-location map but can easily be expanded

**Requires:** Python 3, NumPy

**To run:** `python route_finder.py`

# Task Tracker App 

Description: After completing a few simpler GUI projects, I was fascinated by seeing my code get translated into a simple UI. Therefore, I wanted to build something practical and more complex. This task tracker allows users to input tasks and categorizes them into one of the three categories. It then keeps track of days until the task is due. This is my favorite software project I have done thus far due to how independent I was in the code using only minimal assistance with the JSON and Date Time portion. It is also something that I use from time to time.

Features:
- Three task lists: miscellaneous, room, and general
- Tasks can be set to repeat every set number of days
- Color shows status: green for upcoming, yellow for due today, red for overdue
- Saves tasks to a JSON file so they are still there after closing the app

**Requires:** Python 3 (Tkinter is included)

**To run:** `python task_tracker.py`

## Contact

[jaxlay9@gmail.com](mailto:jaxlay9@gmail.com) · [LinkedIn](https://www.linkedin.com/in/jaxonlay)
