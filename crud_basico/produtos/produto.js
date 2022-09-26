class Produto{
    constructor(nome, preco){
        this.nome = nome
        this.preco = preco
    }

    get_nome(){
        return this.nome
    }

    set_nome(nome){
        this.nome = nome
    }

    get_preco(){
        return this.preco
    }

    set_preco(preco){
        this.preco = preco
    }
}

module.exports = {Produto}