let produto = require('./produto');

class Database {
    constructor() {
        this.db = new Map()
    }

    inserir(nome, preco) {
        if ("string" == typeof nome && "number" == typeof preco) {
            let prod = new produto.Produto(nome, preco)
            let id = 0

            while (this.db.has(id)) {
                id++
            }

            this.db.set(id, prod)
        } else {
            console.log("Erro. Conteúdo não aceito.")
        }
    }

    listar() {
        for (let [id, produto] of this.db) {
            console.log(`${id} | ${produto.get_nome()} | R$ ${produto.get_preco()}`)
        }
    }

    buscar_id(id) {
        if (this.db.has(id)) {
            return [this.db.get(id).get_nome(), this.db.get(id).get_preco()]
        }
        console.log("Erro. ID não encontrada.")
    }

    atualizar(id, nome, preco) {
        if (this.db.has(id)) {
            this.db.get(id).set_nome(nome)
            this.db.get(id).set_preco(preco)
        } else {
            console.log("Erro. ID não encontrada.")
        }
    }

    deletar(id) {
        if (this.db.has(id)) {
            this.db.delete(id)
        } else {
            console.log("Erro. ID não encontrada.")
        }
    }
}

module.exports = { Database }