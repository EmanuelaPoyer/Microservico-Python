from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from dados import cria_db
import sqlite3
import uvicorn
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

#Função para verificar as credenciais de autenticação.
#Retorna um erro HTTP 401 se as credenciais forem inválidas.
def verifica_credenciais(credentials: HTTPBasicCredentials = Depends(security)):
    correto_username = "usuario"
    correto_password = "senha"
    if credentials.username != correto_username or credentials.password != correto_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )

app = FastAPI()

class Produto(BaseModel):
    id: int
    nome: str
    descricao: str
    preco: float

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao sistema de produtos"}

# Rota para listar todos os produtos
@app.get("/todos_os_produtos")
def get_todos_os_produtos(credenciais: HTTPBasicCredentials = Depends(verifica_credenciais)):
    con = sqlite3.connect('produtos.db')
    cur = con.cursor()
    cur.execute('''SELECT id, nome, descricao, preco FROM produtos''')
    res = cur.fetchall()
    cur.close()
    return res

# Rota para pesquisar um produto por ID
@app.get("/pesquisar_produtos/{id_produto}")
def get_produto_usando_id(id_produto: int):
    con = sqlite3.connect('produtos.db')
    cur = con.cursor()
    cur.execute('''SELECT id, nome, descricao, preco FROM produtos WHERE id=?''', (id_produto,))
    res = cur.fetchone()
    cur.close()
    if res is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Produto não encontrado")
    return res

# Rota para criar um novo produto
@app.post("/criar-novo-produto")
def insere_produto(produto: Produto, credenciais: HTTPBasicCredentials = Depends(verifica_credenciais)):
    try:
        con = sqlite3.connect('produtos.db')
        cur = con.cursor()
        cur.execute('''INSERT INTO produtos (id, nome, descricao, preco) 
                        VALUES (?, ?, ?, ?)''', (produto.id, produto.nome, produto.descricao, produto.preco))
        con.commit()
        cur.close()
    except sqlite3.Error as error: 
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Erro ao inserir produto")
    return 'Inserido com sucesso'

# Rota para excluir um produto por ID
@app.delete("/excluir_produto/{id}")
def delete_produto(id: int, credenciais: HTTPBasicCredentials = Depends(verifica_credenciais)):
    con = sqlite3.connect('produtos.db')
    cur = con.cursor()
    cur.execute('''DELETE FROM produtos WHERE id=?''', (id,))
    con.commit()
    cur.close()
    return 'Produto excluído com sucesso'

# Rota para editar um produto por ID
@app.put("/editar-produto/{id_produto}")
def editar_produto(id_produto: int, produto: Produto, credenciais: HTTPBasicCredentials = Depends(verifica_credenciais)):
    con = sqlite3.connect('produtos.db')
    cur = con.cursor()
    cur.execute('''UPDATE produtos SET id=?, nome=?, descricao=?, preco=? WHERE id=?''',
                (produto.id, produto.nome, produto.descricao, produto.preco, id_produto))
    con.commit()
    cur.close()
    return 'Produto editado com sucesso'


if __name__=="__main__":
    cria_db()
    uvicorn.run(app, host="localhost", port=8000)