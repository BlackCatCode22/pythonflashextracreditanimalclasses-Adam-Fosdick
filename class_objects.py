class Lion:
    def __init__(self, voice):
        self.voice = voice

    def get_voice(self):
            return self.voice

    def set_voice(self, voice):
            self.voice = voice


lion1 = Lion("meow")
print(lion1.voice)

lion1.set_voice("roar")
print(lion1.voice)

class Hyena:
    def __init__(self, voice):
        self.voice = voice

    def get_voice(self):
            return self.voice

    def set_voice(self, voice):
            self.voice = voice


Hyena1 = Hyena("laugh")
print(Hyena1.voice)

Hyena1.set_voice("laugh out loud")
print(Hyena1.voice)