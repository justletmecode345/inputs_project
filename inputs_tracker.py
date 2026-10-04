# This file is for the specific statements "inputs.all", "inputs.any", and "inputs.ask" as your generic input statement
class InputTracker:
    def __init__(self):
        self.history = []


    def ask(self, prompt_text):
        try:
            answer = input(prompt_text)
            self.history.append(answer)
            return answer

        except KeyboardInterrupt:
            print("Dont interrupt the keyboard by Crtl + C!")

        @property
        def all(self):
            if not self.history:
                return False

            first_input = self.history[0]

            for item in self.history:
                if item != first_input:
                    return False

        return first_input

        @property
        def any(self):
            if not self.history:
                return False
            return self.history[-1]
