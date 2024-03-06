from openai import OpenAI #Importa a classe OpenAI (Que é a classe que faz a comunicação com a API da OpenAI)
from dotenv import load_dotenv #Importa a função load_dotenv (Que carrega as variáveis de ambiente)
import os  #Importa o módulo os (Sistema Operacional)

load_dotenv() #Carrega as variáveis de ambiente 
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) #Criação do cliente OpenAI
modelo = "gpt-3.5-turbo-1106" #Modelo do GPT-3.5 que será utilizado

def categoriza_produto(nome_produto, lista_categorias_possíveis):
    prompt_sistema = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        #Lista de Categorias Válidas
        {lista_categorias_possíveis.split(",")}

        #Formato de saída:
        Produto: *nome do produto*
        Categoria: *categoria do produto*

        #Exemplo de saida:
        Produto: Escova de dentes de bambu
        Categoria: Higiene Pessoal

    """

    resposta = cliente.chat.completions.create( #Criação de uma conversa
        messages=[
            {
                "role":"system", #Quem está falando
                "content" : prompt_sistema
            },
            {
                "role" : "user", #Quem está falando
                "content" : nome_produto
            }
        ],
        model= modelo, #Qual modelo do GPT a OpenAI deve usar
        temperature = 0, #Criatividade de resposta 
        max_tokens = 200, #Tamanho máximo da resposta
        #n = 3, Quantidade de respostas
        
    )

    return resposta.choices[0].message.content

#for contador in range(0,3):
#print(resposta.choices[0].message.content)#Imprime a resposta da OpenAI
categorias_validas = input("Informe as categorias válidas separadas por vírgula: ")


while True:
    nome_produto = input("Informe o nome do produto: ")
    texto_resposta = categoriza_produto(nome_produto, categorias_validas)
    print(texto_resposta)
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != "s":
        break