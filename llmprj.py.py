#Import Libraries
from llama_cpp import Llama

#Specifying the model path(Mistral.gguf)
model_path = "C:\\Users\\admin\\Desktop\\Codefest\\mistral-7b-instruct-v0.2.Q6_K.gguf"

# model variable
model = Llama(model_path=model_path)

training_message = "You are a factual and reliable assistant that provides true information and text on various Eco-sustainable hotels, restraunts, best modes of sustainable transortation, various places to see and observe in the area and also the carbon footprint that has been emitted through this entire tourist place vacation plan. "
user_input_message = "Generate a plan for a trip to a place consisting of Eco-sustainable hotels in the area, best restraunts, best cheap and eco-friendly modes of transport, best places to see in the area and also after the creation of a plan then tell the overall cost and approximate carbon footprint being emitted through this entire trip" 

prompt = f"""<s>[INST] <<SYS>>
{training_message}
<</SYS>>
{user_input_message} [/INST]"""

max_tokens = 100

output = model(prompt, max_tokens=max_tokens, echo=True)

print(output)
