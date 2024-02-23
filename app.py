"""
This module contains a MouseTracker class that tracks the movement of the mouse and provides a GUI to start and stop recording.

The MouseTracker class uses the tkinter library for creating the GUI and the `pynput` library for listening to mouse movements.

Example usage:
    tracker = MouseTracker()
    tracker.run()
"""

import tkinter as tk
from pynput import mouse


class MouseTracker:
    """
    A class that tracks mouse movements and provides functionality to start and stop recording.

    Attributes:
    - listener: The listener object that listens for mouse movements.
    - is_recording: A boolean flag indicating whether the recording is in progress.
    - root: The root window of the application.
    - record_button: The button used to start and stop the recording.
    """

    def __init__(self):
        self.listener = None
        self.is_recording = False
        self.root = tk.Tk()
        self.record_button = tk.Button(
            self.root, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack()

    def start_recording(self):
        """
        Starts recording mouse movements by creating a new listener object and starting it.
        """
        if not self.is_recording:
            self.is_recording = True
            self.listener = mouse.Listener(on_move=self.on_move)
            self.listener.start()

    def stop_recording(self):
        """
        Stops the recording process.

        If the listener is currently running, it will be stopped and the `is_recording` flag will be set to False.
        """
        if self.is_recording:
            self.is_recording = False
            self.listener.stop()
            self.listener = None

    def on_move(self, x, y):
        """
        Callback function that is called when the mouse is moved.

        Parameters:
        - x (int): The x-coordinate of the mouse cursor.
        - y (int): The y-coordinate of the mouse cursor.
        """
        print(f"Mouse moved to ({x}, {y})")

    def toggle_recording(self):
        """
        Toggles the recording state and updates the text of the record button accordingly.
        If the recording is currently in progress, it stops the recording and changes the button text to "Start Recording".
        If the recording is not in progress, it starts the recording and changes the button text to "Stop Recording".
        """
        if self.is_recording:
            self.stop_recording()
            self.record_button.config(text="Start Recording")
        else:
            self.start_recording()
            self.record_button.config(text="Stop Recording")

    def run(self):
        self.root.mainloop()


tracker = MouseTracker()
tracker.run()
