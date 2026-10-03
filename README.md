# inputs-tracker

A clean Python tool to check multiple console text inputs instantly without messy daisy chains.

## Read This Before Using (Project Rules)
* **Completely Free:** You can copy, change, or use this code anywhere for free.
* **No Responsibility:** This code comes as-is. If you use it and your code breaks, that is on you.
* **No Feature Requests:** I will NOT be implementing extra features (like integer support or auto-casting). The framework is strictly for text.
* **Tweakers Welcome:** If you want new features, tweak the code and add them yourself!
* * **Legal Notice (Philippines):** This source code is an original creation protected under Republic Act No. 8293 (Intellectual Property Code of the Philippines). It is distributed globally under the standard MIT License conditions.


## How to use it
## This is for the "input_all.py" file
```python
# Copy the class code into your project
inputs = InputTracker()

inputs.ask("To test, say 'abort' and on the next one too: ")
inputs.ask("To test, say 'abort' again: ")

if inputs.all == "abort":
  print("aborting...")
  exit()

else:
  print("test failed due to not saying 'abort'")
