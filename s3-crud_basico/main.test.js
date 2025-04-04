const main = require('./main');
const { Database } = require('./produtos/cadastro_produtos');
const { Produto } = require('./produtos/produto');

let database = new Database()

test('Criação do banco de dados', () => {
    expect(database).toEqual(new Database);
});

test('Inserção dos produtos', () => {
    database.inserir("prod1", 10.10)

    expect(database.db.has(0)).toBeTruthy();
    expect(database.db.get(0)).toEqual(new Produto("prod1", 10.10));
    expect(database.db.get(0).get_nome()).toMatch("prod1");
    expect(database.db.get(0).get_preco()).toEqual(10.10);

    //exception
    expect(database.inserir(10.10, "prod1")).toBeFalsy();
    expect(database.inserir({}, true)).toBeFalsy();
    expect(database.inserir("prod1", "10.10")).toBeFalsy();
});

// Não consegui testar devidamento o .listar()
// pq ele não retorna conteúdo e fica como "undefined" nos testes.
// E não entendi como capturar o conteúdo do console.log() :(
test('Listar produtos', () => {
    expect(database.listar()).toBe(console.log());
    //expect(database.listar()).toMatch("0 | prod1 | R$ 10.10");
});

test('Buscar produtos', () => {
    expect(database.buscar_id(0)).toEqual(["prod1", 10.10]);

    //exception
    expect(database.buscar_id(1)).toBeFalsy();
    expect(database.buscar_id(1)).toBeUndefined();
});

test('Atualização dos produtos', () => {
    database.atualizar(0, "prod2", 5.79)

    expect(database.db.has(0)).toBeTruthy();
    expect(database.db.get(0)).toEqual(new Produto("prod2", 5.79));
    expect(database.db.get(0).get_nome()).toMatch("prod2");
    expect(database.db.get(0).get_preco()).toEqual(5.79);
    expect(database.buscar_id(0)).toEqual(["prod2", 5.79]);

    //exception
    expect(database.atualizar(1)).toBeFalsy();
});

test('Remoção dos produtos', () => {
    database.deletar(0)

    expect(database.db.has(0)).toBeFalsy();
    expect(database.db.get(0)).toBeUndefined();
    expect(database.buscar_id(0)).toBeUndefined();

    //exception
    expect(database.deletar(1)).toBeFalsy();
});