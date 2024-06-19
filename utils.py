import tkinter as tk

cli = False

class ValueObject():
    def __init__(self, value):
        self.value = value

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

class StringObject(ValueObject):
    pass

class BoolObject(ValueObject):
    pass

def init_string(value):
    return StringObject(value) if cli else tk.StringVar(value=value)

def init_bool(value):
    return BoolObject(value) if cli else tk.BooleanVar(value=value)

def init_int(value):
    return ValueObject(value) if cli else tk.IntVar(value=value)

def init_double(value):
    return ValueObject(value) if cli else tk.DoubleVar(value=value)
class UserInteraction():
    def __init__(self, root):
        self.root = root

    def write_command_text(self, text):
        if self.root.cli:
            print(text)
        else:
            self.root.command_Text.write(text)

    def log_error(self, error):
        if self.root.cli:
            print(error)
        else:
            self.root.error_log_var.set(error)

    def error_dialogue(self, error):
        if self.root.cli:
            print(error)
        else:
            self.root.error_dialoge(error)

    def message_box(self, message):
        if self.root.cli:
            print(message)
            return True
        else:
            self.root.message_box(message)
