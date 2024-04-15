# Microservico-Python

# Aqui está a documentação para o microserviço que desenvolvi para gerenciar produtos. Este serviço permite listar, pesquisar, inserir, editar e excluir produtos de um banco de dados.

** O microserviço está disponível em uma URL específica. Você pode acessá-lo utilizando um cliente HTTP ou diretamente pelo navegador. **

URL Base:
http://localhost:8000

Rotas Disponíveis

1. Listar todos os produtos
Esta rota retorna todos os produtos disponíveis.
Método HTTP: GET /todos_os_produtos

2. Pesquisar um produto pelo ID
Esta rota retorna as informações de um produto específico com base no seu ID.
Método HTTP: GET /pesquisar_produtos/{id_produto}
Substitua {id_produto} pelo ID real do produto que deseja pesquisar.

3. Inserir um novo produto
Esta rota permite inserir um novo produto no banco de dados.
Método HTTP: POST /criar-novo-produto

4. Excluir um produto pelo ID
Esta rota permite excluir um produto do banco de dados com base no seu ID.
Método HTTP: DELETE /excluir_produto/{id}
Substitua {id} pelo ID do produto que deseja excluir.

5. Editar um produto pelo ID
Esta rota permite editar as informações de um produto com base no seu ID.
Método HTTP: PUT /editar-produto/{id_produto}
Substitua {id_produto} pelo ID do produto que deseja editar.

Autenticação
Para proteger o acesso ao microserviço, implementei a autenticação básica. As credenciais de acesso são:

Usuário: usuario
Senha: senha

Documentação Interativa

Também é possível interagir com a documentação utilizando o FastAPI, o framework que escolhi. Isso torna mais fácil entender as rotas disponíveis e permite fazer solicitações de teste diretamente na interface.
