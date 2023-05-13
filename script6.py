#nao funcionou
import openai
import docx
import PyPDF4
import os

openai.api_key = "CODIGO API AQUI"

model_engine = "text-davinci-002"
max_tokens = 2000

prompt1 = "Por favor, descreva de forma clara e detalhada o assunto principal da petição que está sendo analisada. Inclua informações relevantes sobre a causa em questão e os motivos pelos quais a petição foi iniciada."
prompt2 = "Gostaria de obter uma descrição completa do objetivo da petição em questão. Por favor, inclua detalhes sobre quais ações ou mudanças a petição busca promover, e para quem elas são direcionadas. Se houver um prazo para a realização dessas mudanças, por favor, informe também."
prompt3 = "Quero entender melhor quem é o autor ou organizador da petição. Por favor, forneça informações relevantes sobre a pessoa ou organização responsável pela criação e divulgação da petição, incluindo seu nome, histórico e possíveis motivações por trás da iniciativa."

# obtém o diretório atual do script
current_dir = os.path.dirname(os.path.abspath(__file__))

# monta o caminho para o arquivo PDF
pdf_path = os.path.join(current_dir, 'dados', 'peticao.pdf')

# abre o arquivo PDF
pdf_file = open(pdf_path, 'rb')

# crie um objeto PDFReader e extraia o texto do PDF
pdf_reader = PyPDF4.PdfFileReader(pdf_file)
pdf_text = ''
for page_num in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_num)
    pdf_text += page.extractText()

# feche o arquivo PDF
pdf_file.close()

# faça a solicitação à API da OpenAI para gerar o relatório
response1 = openai.Completion.create(
   engine=model_engine,
   prompt=prompt1 + '\n\n' + pdf_text,
   max_tokens=max_tokens,
   temperature=0.5,
   n=1,
   stop=None,
   frequency_penalty=0,
   presence_penalty=0
)

response2 = openai.Completion.create(
   engine=model_engine,
   prompt=prompt2 + '\n\n' + pdf_text,
   max_tokens=max_tokens,
   temperature=0.5,
   n=1,
   stop=None,
   frequency_penalty=0,
   presence_penalty=0
)

response3 = openai.Completion.create(
   engine=model_engine,
   prompt=prompt3 + '\n\n' + pdf_text,
   max_tokens=max_tokens,
   temperature=0.5,
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
doc.save('relatorio.docx')
