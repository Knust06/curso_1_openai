from openai import OpenAI #Importa a classe OpenAI (Que é a classe que faz a comunicação com a API da OpenAI)
from dotenv import load_dotenv #Importa a função load_dotenv (Que carrega as variáveis de ambiente)
import os  #Importa o módulo os (Sistema Operacional)

load_dotenv() #Carrega as variáveis de ambiente 
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) #Criação do cliente OpenAI

resposta = cliente.chat.completions.create( #Criação de uma conversa
    messages=[
        {
            "role":"system", #Quem está falando
            "content" : """
            Classifique o produto abaixo em uma das categorias: Higiene, Moda ou Casa e de uma descrição da categoria.
            #Formato de saída: 
            *categoria* - *descrição*
            """
        },
        {
            "role" : "user", #Quem está falando
            "content" : """
            Escova de dentes de bambu
            """
        }
    ],
    model="gpt-3.5-turbo-1106", #Qual modelo do GPT a OpenAI deve usar
    temperature = 0, #Criatividade de resposta 
    n = 3, #Quantidade de respostas
    max_tokens = 200, #Tamanho máximo da resposta
    
)

for contador in range(0,3):
    print(resposta.choices[contador].message.content)#Imprime a resposta da OpenAI