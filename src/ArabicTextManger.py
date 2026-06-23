from arabic_reshaper import reshape, ArabicReshaper
from bidi.algorithm import get_display

class ArabicTextManger:
    def __init__(self):
        self.reshaper = ArabicReshaper()
        self.original_to_reshaped = {}
        self.reshped_to_original = {}

    def reshape_text(self, text):
        original = text
        reshaped = get_display(reshape(text))
        self.original_to_reshaped[original] = reshaped
        self.reshped_to_original[reshaped] = original
        return reshaped

    def unshape(self, text):
        return self.original_to_reshaped.get(text, text)
