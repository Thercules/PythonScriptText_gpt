#CÓDIGO COM DOIS PROMPT E UNINDO OS DOIS
import openai

openai.api_key = ""

model_engine = "text-davinci-002"
max_tokens = 2000

prompt1 = "Escreva uma artigo extenso sobre segunda guerra mundial"
prompt2 = "Escreva uma artigo extenso sobre guerra fria"

response1 = openai.Completion.create(
   engine=model_engine,
   prompt=prompt1,
   max_tokens=max_tokens,
   temperature=0.7,
   n=1,
   stop=None,
   frequency_penalty=0,
   presence_penalty=0
)

response2 = openai.Completion.create(
   engine=model_engine,
   prompt=prompt2,
   max_tokens=max_tokens,
   temperature=0.7,
   n=1,
   stop=None,
   frequency_penalty=0,
   presence_penalty=0
)

output_text = response1.choices[0].text.strip() + response2.choices[0].text.strip()
print("Output:", output_text)


