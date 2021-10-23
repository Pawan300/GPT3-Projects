import json
import openai

class GPT:

  def __init__(self, engine='davinci', temperature=0.5, max_tokens=100):

    self.examples = []
    self.engine  = engine
    self.temperature = temperature
    self.max_tokens = max_tokens

  def set_examples(self, example):
    text = "input:{} \noutput:{}\n".format(example[0], example[1])
    return self.examples.append(text)

  def get_engine(self):
    return self.engine

  def get_examples(self):
    return "\n".join(self.examples) + "\n"

  def set_prompt(self, prompt):
    return self.get_examples() + "\ninput:" + prompt + "\n"

  def create_response(self, prompt, initials=""):

    response = openai.Completion.create(
        engine=self.get_engine(),
        prompt=initials+ "\n"+self.set_prompt(prompt),
        temperature=self.temperature,
        max_tokens=self.max_tokens,
        top_p=1, 
        n=1,
        stream=False,
        stop="\ninput:"
    )

    return response