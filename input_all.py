# This file is for the specific command "inputs.all"
class InputTracker:
    def __init__(self):
        self.history = []


    def ask(self, prompt_text):
        try:
            awnser = input(prompt_text)
            self.history.append
            return awnswer

        except KeyboardInterrupt:
            print("Dont interrupt the keyboard by Crtl + C!")
