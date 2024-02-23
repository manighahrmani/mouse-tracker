import tkinter as tk
from pynput import mouse


class MouseTracker:
    def __init__(self):
        # Instance variable to store the listener object
        self.listener = None
        # Instance variable to store the recording state
        self.is_recording = False

        # Create the root window
        self.root = tk.Tk()

        # Create the record button
        self.record_button = tk.Button(
            self.root, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack()

    def start_recording(self):
        # Start the listener if it's not already running
        if not self.is_recording:
            self.is_recording = True
            # Create a new listener object that listens for mouse movements
            # This is from the `pynput` library (look it up)
            # We pass the `on_move` method as the event handler for mouse movements
            self.listener = mouse.Listener(on_move=self.on_move)
            # Start the listener
            self.listener.start()

    def stop_recording(self):
        # Stop the listener if it's running
        if self.is_recording:
            self.is_recording = False
            self.listener.stop()
            self.listener = None

    def on_move(self, x, y):
        # This method is called whenever the mouse moves
        # We just print the coordinates of the mouse at the moment
        print(f"Mouse moved to ({x}, {y})")

    def toggle_recording(self):
        # This method is called when the record button is clicked
        if self.is_recording:
            # Call the `stop_recording`` method if we are currently recording
            self.stop_recording()
            # Change the text of the button to reflect the state
            self.record_button.config(text="Start Recording")
        else:
            self.start_recording()
            self.record_button.config(text="Stop Recording")

    def run(self):
        self.root.mainloop()


tracker = MouseTracker()
tracker.run()
