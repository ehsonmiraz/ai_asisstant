
import lucy
from lucy import settings
from lucy.core.console import ConsoleManager as cm
from lucy.utils.startup import *
import openai
from lucy.services.indicator import Indicator

class Processor:
    def __init__(self):
        openai.api_key = settings.OPENAI_APIKEY
        self.messages = [
        {"role": "system", "content":
            settings.PROMPTMESSAGE}]
        self.chat = None
        self.indicat = Indicator()
    def run(self):
        self.indicat.turn_on()
        message = lucy.input_engine.recognize_input()
        self.indicat.turn_of()
        if message:
            self.messages.append({"role": "user", "content": message}, )
            self.chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=self.messages
            )
        reply = self.chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        self.messages.append({"role": "assistant", "content": reply})
        lucy.output_engine.respond(reply)




