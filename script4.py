#CÓDIGO COM TRÊS PROMPT E UNINDO OS DOIS
import openai

openai.api_key = ""

model_engine = "text-davinci-002"
max_tokens = 4000

prompt1 = "Escreva uma artigo extenso sobre o campeonato de Counter Strike Major 2018"
prompt2 = "Escreva uma artigo extenso sobre campeonato de Counter Strike Major 2019"
prompt3 = "Escreva uma artigo extenso sobre campeonato de Counter Strike Major 2020"

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
