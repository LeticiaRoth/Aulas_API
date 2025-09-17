#Importação do FasAPI e suas dependências
from fastapi import FastAPI, HTTPException, status, Response, Depends

#Pego o modelo criado
from models import PersonagensTLOU, PersonagensTLOUUpdate

from typing import Optional, Any

#Criação da instância do FastAPI
app = FastAPI(title='API de Personagens do The Last of US', version='0.0.1', description='API responsável pro apresentar os personagens da jogo The Last Of Us')

#Criação do banco de personagens
personagens = {
    1: {
        'nome': 'Joel Miller',
        'faccao': 'Rebeldes',
        'frase': 'A sobrevivência é o que importa. Não importa o preço.',
        'idade': 40,
        'foto_game': 'https://static.wikia.nocookie.net/thelastofus/images/2/27/The_Last_of_Us_Part_I_Joel.png/revision/latest?cb=20220905023610&path-prefix=es,',
        'foto_serie' :'https://i0.wp.com/imgs.hipertextual.com/wp-content/uploads/2023/04/joel-the-last-of-us-scaled.jpg?fit=2560%2C1440&quality=70&strip=all&ssl=1'
    },
    2: {
        'nome': 'Ellie',
        'faccao': 'Vagalumes',
        'frase': 'Eu não sou uma garotinha pra você proteger.',
        'idade': 14,
        'foto_game': 'https://static.wikia.nocookie.net/thelastofus/images/8/8e/Part_I_Ellie_infobox.webp/revision/latest?cb=20230216184044&path-prefix=pt-br',
        'foto_serie' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR9oW1m-5THzdfx3H1i7w5k-Uizj5oOjvMhe_SjHQxPKWHGfTi2Aml5FyTBVQqYM6aK65s&usqp=CAU'
    },
    3: {
        'nome': 'Tess',
        'faccao': 'Sobrevivente/Parceira do Joel',
        'frase': 'Se for para morrer, morre lutando',
        'idade': 35,
        'foto_game': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRVYGTWJ7B7wBLi9GTTwy3Dw3zR-HdiChHzLg&s',
        'foto_serie' : 'https://i.pinimg.com/736x/fd/28/2e/fd282e607d0183ea4acf2c6ec7a15f12.jpg'
    },
    4:{
        'nome': 'Tommy',
        'faccao': 'Sobrevivente/Irmão do Joel',
        'frase': 'É melhor a gente manter a cabeça no lugar, ou não vamos durar muito.',
        'idade': 38,
        'foto_game': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSxycO8Rqz4GK4vT1hUPgnjqy-Qq08dt1izSA&s',
        'foto_serie' : 'https://assets.portalleodias.com/2024/04/Joel-e-Tommy-em-The-Last-Of-Us.jpg'
    },
    5:{
        'nome' : 'Marlene',
        'faccao': 'Líder do Vagalumes',
        'frase': 'Estamos lutando por um futuro que valha a pena.',
        'idade': 35,
        'foto_game': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3oY3JvU3cujSvHAHRkgpje28oAtPYln1Y-g&s',
        'foto_serie' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT_WN4EvoV3n24g0lSbQwSs5W4zhM3gRqHPZYv8-x-lUNT_5lK3kSfqI6CBhsA9tN3LJGk&usqp=CAU'
    },
    6: {
        'nome': 'Bill',
        'faccao': 'Sobrevivente solitário',
        'frase': 'Se não quer morrer, não faça barulho',
        'idade': 55,
        'foto_game' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRKFUBrOQxTdL7a8-FG7S_KRVpf1X_TuDpFTw&s',
        'foto_serie' : 'https://noticiasdatv.uol.com.br/media/uploads/artigos_2021/hbo-max-the-last-of-us-bill-nick-offerman-divulgacao-hbo-27-1-23.jpg'
    },
    7: {
        'nome': 'David',
        'faccao': 'Líder de um grupo canibal',
        'frase' : 'Às vezes, para sobreviver, você tem que se tornar pior do que eles',
        'idade': 40,
        'foto_game' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKX4trFuetI__6WSNN4wLd3JZoRKDVgVQJ6Q&s',
        'foto_serie' : 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS58MjM75JW0PPM1v02F3_4JDNYnX2cg3_XWA&s'
    },
    8: {
        'nome': 'Abby',
        'faccao' : 'Grupo de Seatle',
        'frase' : 'A vingança nunca termina. Isso não é vida',
        'idade': 28,
        'foto_game': 'https://i.pinimg.com/736x/9e/9a/9c/9e9a9ca5633e7711f600f27a60e745f4.jpg',
        'foto_serie' : 'https://p2.trrsf.com/image/fget/cf/1200/900/middle/images.terra.com/2024/09/26/abby-tlous-serie-1h7lgp71tnn1d.jpg'
    }
}



#Método GET 
@app.get("/personagens/{personagem_id}", description='Retorna o personagem TLOU com o ID') #Documentacao de requisição feita
async def get_personagens(personagem_id: int):
    try:
        personagem = personagens[personagem_id]
        return personagem
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Personagem de The Last Of Us não foi encontrado')
    
#Método POST
@app.post('/personagens',status_code=status.HTTP_201_CREATED, description='Criação de um novo persoagem',summary='Personagem criado') #Documetação de criaçao
async def posto_personagens(personagem: Optional[PersonagensTLOU]= None):
    try:   
        nex_id = len(personagens) + 1
        personagens[nex_id]= personagem

        del personagem.personagem
        return personagem
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Erro ao adicionar personagem: {str(e)}"
        )
    

#Método PUT - atualização
@app.put('/personagens/{personagem_id}', status_code=status.HTTP_202_ACCEPTED, description='Atualização da lista de personagens The Last Of Us')
async def put_personagens(personagem_id: int, personagem: PersonagensTLOU):
    if personagem_id in personagens:
        personagens[personagem_id] = personagem
        personagem.id = personagem_id
        del personagem.id
        return
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Personagem TLOU não encontrado!')

#Método DEL - remoção
@app.delete('personagens/{personagens_id}', status_code=status.HTTP_204_NO_CONTENT, description='Deletar personagem de The Last Of Us')
async def delete_personagem(personagem_id: int):
    if personagem_id in personagens:
        del personagens[personagem_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT, detail='Personagem deletado.')

   
#Método PATCH
@app.patch('/personagens/{pesonagem_id}', status_code=status.HTTP_202_ACCEPTED, description='Atualização parcial dos personagens')
async def patch_personagem(personagem_id:int,personagem_data:PersonagensTLOUUpdate):

    #Personagem data:json com os campos que irão ser modificado
    if personagem_id not in personagens:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Personagem TLOU não encontrado')
    
    #Atualiza os campos passados na requisição, como o pedido
    personagem_existente = personagens[personagem_id]
    dados_atualizar = personagem_data.model_dump(exclude_unset=True)
    personagem_existente.update(dados_atualizar)

    return personagem_existente


"""
if __name__ == 'main':
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8001, log_level="info", reload=True)
"""