import tkinter as tk
from pynput import mouse


class MouseTracker:
    def __init__(self):
        self.listener = None
        self.is_recording = False
        self.root = tk.Tk()
        self.record_button = tk.Button(
            self.root, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack()

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.listener = mouse.Listener(on_move=self.on_move)
            self.listener.start()

    def stop_recording(self):
        if self.is_recording:
            self.is_recording = False
            self.listener.stop()
            self.listener = None

    def on_move(self, x, y):
        print(f"Mouse moved to ({x}, {y})")

    def toggle_recording(self):
        if self.is_recording:
            self.stop_recording()
            self.record_button.config(text="Start Recording")
        else:
            self.start_recording()
            self.record_button.config(text="Stop Recording")

    def run(self):
        self.root.mainloop()


def create_app():
    tracker = MouseTracker()
    tracker.run()


if __name__ == "__main__":
    create_app()
