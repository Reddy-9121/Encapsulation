class Widget:
    def render(self):
        pass

class Button(Widget):
    def render(self):
        print("Rendering a button")

class TextBox(Widget):
    def render(self): 
        print("Rendering a text box")


widgets = [Button(), TextBox()]
for widget in widgets:
    widget.render()  # Added parentheses to call the method
