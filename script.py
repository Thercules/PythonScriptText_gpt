#PRIMEIRO CÓDIGO FEITO EM PYTHON PARA GERAR TEXTO COM CHATGPT
import openai

# Autenticação
openai.api_key = "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"

# Definindo o modelo a ser usado
model_engine = "text-davinci-002"

# Parâmetros da solicitação de resposta
prompt = "Escreva para mim um artigo sobre a época da escravidão no brasil para o meu blog"
max_tokens = 1000
n_gen = 1
temperature = 0.7
stop = None

# Solicitação de resposta
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    n=n_gen,
    stop=stop
)

print(response.choices[0].text)

