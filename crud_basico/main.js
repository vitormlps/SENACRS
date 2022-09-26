let database = require('./produtos/cadastro_produtos');

function main(){
    let db = new database.Database()

    let nomes = ["Queijo Prato, 200g", "Sorvete, Sabor Uva", "Café 3 Corações", "Coca, 2L", "Dado Bier Light"]
    let precos = [10.10, 19.32, 14.66, 5.76, 2.98]

    //Inserir produtos
    for (let prod = 0; prod < nomes.length; prod++) {
        db.inserir(nomes[prod], precos[prod])
    }

    //Listar produtos
    db.listar()

    //Buscar produtos por ID
    let prod_encontrado = db.buscar_id(2)
    console.log(`\n${prod_encontrado[0]} | R$ ${prod_encontrado[1]}\n`)

    //Atualizar produtos
    db.atualizar(1, "Tupiniquim Weiss, 1L", 7.72)

    //Deletar produtos
    db.deletar(4)

    // Mostrar produtos atualizados
    db.listar()
}

main()