#GERAÇÃO DE TEXTO COM CHAT GPT COM UM 
import openai

openai.api_key = "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"

model_engine = "gpt-3.5-turbo"
max_tokens = 4050
input_text = "Escreva uma artigo extenso com até 4000 caracteres sobre segunda guerra mundial e uma boa citação ilustre a respeito desse tema"

response = openai.ChatCompletion.create(
   model=model_engine,
   messages=[{"role": "user", "content": input_text }],
   max_tokens=max_tokens
)

output_text = response['choices'][0]['message']['content']
print("Output:", output_text)