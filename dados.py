import sqlite3

#Função para criar e inicializar o banco de dados 'produtos.db'.
def cria_db():
    con = sqlite3.connect('produtos.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS produtos
                (id INTEGER PRIMARY KEY, nome TEXT, descricao TEXT, preco REAL)''')

    cur.execute('''SELECT COUNT(*) FROM produtos''')
    count = cur.fetchone()[0]

    if count == 0:
        cur.execute('''INSERT INTO produtos (id, nome, descricao, preco) VALUES(1, 'Produto 1', 'Este é o produto 1', 50.0)''')
        cur.execute('''INSERT INTO produtos (id, nome, descricao, preco) VALUES(2, 'Produto 2', 'Este é o produto 2', 100.0)''')

    con.commit()
    cur.close()
