
#Importação do FastAPI
from fastapi import FastAPI, HTTPException, status, Response, Depends
#Importo o modelo para fazer o post
from models import PersonagensToyStory

from typing import Optional, Any

from routes import curso_router, usuario_router

import requests

#Cria uma instancia, uma variavel do tipo FasAPI
app = FastAPI(title="API de Personagens do Toy Story,", version="0.0.1", description="API segredos de menina jane e lele")

#Curso e usuários do router
app.include_router(curso_router.router, tags=['Cursos'])
app.include_router(usuario_router.router, tags=['Usuários'])


@app.get('/pokemon/{name}')
def get_pokemon(name:str):
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')
    if response.status_code == 200:
        return response.json()
    return {'Message': 'Pokemon not found'}

#Exemplo de injeção
def fake_db():
    try:
        print("Conectando com o bando de dados")
    finally:
        print("Fechando o banco")

personagens = {
    1: {
        "nome": "Wood",
        "dono": "Andy",
        "tamanho": "Pequeno",
        "foto": "https://www.google.com/imgres?q=foto%20do%20woody%20do%20toy%20story&imgurl=https%3A%2F%2Flumiere-a.akamaihd.net%2Fv1%2Fimages%2Fb_toystory_characterbanner_woody_mobile_gradient_v2_32211a98.jpeg%3Fregion%3D0%2C0%2C640%2C480&imgrefurl=https%3A%2F%2Fcharacters.disney.com%2Ftoy-story%2Fwoody&docid=DnLM7WrakhU7UM&tbnid=nqzKbN3QjHIEYM&vet=12ahUKEwi8jsmIppmPAxUiLLkGHS2xGtUQM3oECC4QAA..i&w=640&h=480&hcb=2&ved=2ahUKEwi8jsmIppmPAxUiLLkGHS2xGtUQM3oECC4QAA",
        "frase": "Amigo estou aqui"
    },

    2: {
        "nome": "Buzz Lighter",
        "dono": "Bonnie",
        "tamanho": "Pequeno",
        "foto": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.guiadoscuriosos.com.br%2Fcultura-e-entretenimento%2Fpor-que-buzz-lightyear-ganhou-esse-nome%2F&psig=AOvVaw20QtZpnwQQMde6EqcjPj2a&ust=1755776300741000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCPDI7cemmY8DFQAAAAAdAAAAABAK",
        "frase": "Ao infinito e além"
    }
}

#Decorator, indica para a função que está abaixo dela que terá outra
#@app.get("/")

#Cria funções assincronas dentro do python, faz varias coisas ao mesmo tempo

@app.get("/") 
async def raiz():
    return {"Hello its me!"}


#Exemplo de injeção, para funcionar ele faria isso
@app.get("/personagens")
async def get_personagens(db: Any = Depends(fake_db)):
    return personagens

#Método GET, procura, puxando
#Busca de personagens por ID
@app.get("/personagens/{personagem_id}", description="Retorna o personagem com um ID específico", summary="Retorna um personagem") #Consigo estilizar colocando summary e description
async def get_personagem(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado") #Preciso colocar o try, exception, raise e details para determinar o erro
    

#Cria dentro da seção e não dentro do banco de dados
#Caminho dentro do parenteses
#Método POST, criação
@app.post("/personagens", status_code=status.HTTP_201_CREATED) #Status usdo para documentação
async def post_personagem(personagem: Optional[PersonagensToyStory]= None):

    #Pega o tamanho do meu dicionario e soma mais um
    nex_id = len(personagens) + 1
    personagens[nex_id] = personagem
    #Para não aparecer duas vezes o id
    del personagem.id
    return personagem


#Método PUT, atualização 
@app.put("/personagens/{personagem_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_personagem(personagem_id: int, personagem: PersonagensToyStory):
    if personagem_id in personagens:
        #Verifica e sobrescreve por algo melhor
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return personagem
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Personagem não encontrado") 


#Método DEL, delete
@app.delete("personagens/{personagens_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_personagem(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        #Não há conteúdo por isso é melhor
        return Response(status_code=status.HTTP_204_NO_CONTENT, detail="Personagem deletado")


@app.get("/calcular")
async def calcular(a: int, b: int):
    soma = a + b
    return soma


#Injeção de dependedncia, vá depende de alguma função ou algo do gênero para funcionar corretamente, para 
#resolber isso usamos o que chamamso de injeção de dependências



#Executar o arquivo do python, fazendo a execução 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8001, log_level="info", reload=True)


