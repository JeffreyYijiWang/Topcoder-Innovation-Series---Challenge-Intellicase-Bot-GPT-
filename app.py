import random
import gradio as gr

#pulls from history of the typed in the app
def alternatingly_agree(message, history):
    if len(history) % 2 == 0:
        return f"Yes, I do think that '{message}'"
    else:
        return "I don't think so"
    
#alternation- responses 
def random_response(message, history):
    return random.choice(["Yes", "No"])

import time
import gradio as gr

#create Lag time and individual key typing
def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.3)
        yield "You typed: " + message[: i+1]

def yes_man(message, history):
    if message.endswith("?"):
        return "Yes"
    else:
        return "Ask me anything!"

gr.ChatInterface(
    yes_man,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
    title="Yes Man",
    description="Ask Yes Man any question",
    theme="soft",
    examples=["Hello", "Am I cool?", "Are tomatoes vegetables?"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
).launch()