import openai
import docx

openai.api_key = "CODIGO API AQUI"

model_engine = "text-davinci-002"
max_tokens = 4050

prompt1 = "Escreva um título de artigo sobre segunda guerra mundial e uma sinopse desse artigo"
prompt2 = "Escreva uma introdução extensa com 4000 caracteres para um artigo sobre segunda guerra mundial"
prompt3 = "Escreva um título para um tópico de desenvolvimento e contextualize de forma extensa com até 4000 caracteres sobre a história da segunda guerra"

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

# cria um objeto Document
doc = docx.Document()

# adiciona o conteúdo ao documento
doc.add_paragraph(output_text)

# salva o documento
doc.save('output4.docx')


