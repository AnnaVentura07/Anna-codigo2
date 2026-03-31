from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Dizendo pro Flask onde salvar o arquivo do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mercadinho.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Criando a conexão com o banco
db = SQLAlchemy(app)

# --- MODELO DO PRODUTO ---
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True) # RG do produto
    nome = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)

    # Converte o produto em um formato que o app entende (JSON)
    def para_dicionario(self):
        return {"id": self.id, "nome": self.nome, "preco": self.preco}

# Cria o banco e as tabelas se ainda não existirem
with app.app_context():
    db.create_all()

# --- FUNÇÕES DA API ---

@app.route('/produtos', methods=['GET'])
def listar_tudo():
    # Puxa a lista completa do banco
    todos = Produto.query.all()
    # Mostra tudo na tela
    return jsonify([p.para_dicionario() for p in todos])

@app.route('/produtos', methods=['POST'])
def criar_novo():
    dados = request.json
    
    # Prepara o novo produto com o que o usuário mandou
    novo = Produto(nome=dados['nome'], preco=dados['preco'])
    
    # Salva no banco de vez
    db.session.add(novo)
    db.session.commit()
    
    return jsonify(novo.para_dicionario()), 201

@app.route('/produtos/<int:id>', methods=['DELETE'])
def remover_item(id):
    # Tenta achar o item pelo ID ou dá erro se não existir
    item = Produto.query.get_or_404(id)
    
    # Apaga e salva a mudança
    db.session.delete(item)
    db.session.commit()
    
    return jsonify({"status": "Já era! Apagado."}), 200

if __name__ == '__main__':
    # Liga o servidor
    app.run(debug=True)