#CÓDIGO COM TRÊS PROMPT E UNINDO OS DOIS
import openai

openai.api_key = "CODIGO API AQUI"

model_engine = "text-davinci-002"
max_tokens = 4000

prompt1 = "Escreva um título de artigo sobre segunda guerra mundial e uma sinopse desse artigo"
prompt2 = "Escreva uma introdução de artigo sobre segunda guerra e uma boa citação ilustre a respeito desse tema"
prompt3 = "escreva dois parágrafos sobre a história do segunda guerra"

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

response3 = openai.Completion.create(
   engine=model_engine,
   prompt=prompt1,
   max_tokens=max_tokens,
   temperature=0.7,
   n=1,
   stop=None,
   frequency_penalty=0,
   presence_penalty=0
)

output_text = response1.choices[0].text.strip() + response2.choices[0].text.strip() + response3.choices[0].text.strip()
print("Output:", output_text)
