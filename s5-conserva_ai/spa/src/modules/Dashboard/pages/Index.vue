<template>
  <div>
    <h1>Ola {{ nome_usu }}</h1>

    <!-- Seção de Lotes -->
    <div>
      <h2>Lotes</h2>
      <div class="Conteiner">
        <!-- Lotes a Vencer -->
        <v-card v-for="lote in lotesAVencer.slice(0, 2)" :key="lote.id">
          <v-sheet class="Avencer ma-2 pa-2">
            <div class="icon">
              <v-icon icon="mdi-package-variant-closed">
                mdi-package-variant-closed
              </v-icon>
            </div>
            <div class="cabecario">A Vencer</div>
          </v-sheet>
          <v-sheet class="boxAvencer ma-2 pa-2">
            <div class="lote">
              <div>Lote: {{ lote.id }}</div>
              <div>Nome: {{ getProductName(lote.productId) }}</div>
              <div>Min Qty: {{ getBatchInfo(lote.productId).minQty }}</div>
              <div>Qty: {{ lote.quantity }}</div>
              <div>Expira em: {{ daysUntilExpiration(lote.expirationDate) }} dias</div>
            </div>
          </v-sheet>
        </v-card>

        <!-- Lotes Vencidos -->
        <v-card v-for="lote in lotesVencidos.slice(0, 2)" :key="lote.id">
          <v-sheet class="Vencido ma-2 pa-2">
            <div class="icon">
              <v-icon icon="mdi-package-variant-closed">
                mdi-package-variant-closed
              </v-icon>
            </div>
            <div class="cabecario"> Vencidos</div>
          </v-sheet>
          <v-sheet class="boxvencer ma-2 pa-2">
            <div class="lote">
              <div>Lote: {{ lote.id }}</div>
              <div>Nome: {{ getProductName(lote.productId) }}</div>
              <div>Min Qty: {{ getBatchInfo(lote.productId).minQty }}</div>
              <div>Qty: {{ lote.quantity }}</div>
              <div>Vencido há: {{ daysSinceExpiration(lote.expirationDate) }} dias</div>
            </div>
          </v-sheet>
        </v-card>
      </div>
    </div>
    <div class="ponto">
          <v-btn class="pontos" @click="">...</v-btn>
    </div>
        <!-- linha divisoria de lote e produtos -->
        <div class="linha"></div>
        <h2>Produtos</h2>
    <!-- Seção de Produtos -->
    <div class="Conteiner">
      <!-- Produtos que estão Acabando -->
      <v-card v-for="produto in produtosAcabando.slice(0, 2)" :key="produto.id">
        <v-sheet class="Acabando ma-2 pa-2">
          <div class="icon">
            <v-icon icon="mdi-food-turkey">mdi-food-turkey</v-icon>
          </div>
          <div class="cabecario"> Acabando</div>
        </v-sheet>
        <v-sheet class="boxAcabando ma-2 pa-2">
          <div class="lote">
            <div>Lotes: {{ produto.id }}</div>
            <div>Nome: {{ produto.name }}</div>
            <div>Min Qty: {{ produto.minQty }}</div>
            <div>Qty: {{ getQuantidadeTotal(produto.id) }}</div>
          </div>
        </v-sheet>
      </v-card>

      <!-- Produtos que Acabaram -->
      <v-card v-for="produto in produtosAcabaram.slice(0, 2)" :key="produto.id">
        <v-sheet class="Acabaram ma-2 pa-2">
          <div class="icon">
            <v-icon icon="mdi-food-turkey">mdi-food-turkey</v-icon>
          </div>
          <div class="cabecario"> Acabou</div>
        </v-sheet>
        <v-sheet class="boxAcabaram ma-2 pa-2">
          <div class="lote">
            <div>Lotes: {{ produto.id }}</div>
            <div>Nome: {{ produto.name }}</div>
            <div>Min Qty: {{ produto.minQty }}</div>
            <div>Qtd:{{ produto.quantity }}</div>
            <div>Qty: {{ getQuantidadeTotal(produto.id) }}</div>
          </div>
        </v-sheet>
      </v-card>
    </div>
    <div class="ponto">
          <v-btn class="pontos" @click="">...</v-btn>
    </div>
  </div>
</template>

<script>
import Products from "@/services/Products";
import Batches from "@/services/Batches";

export default {
  data() {
    return {
      nome_usu: "Gabi",
      produtos: [],
      lotes: [],
    };
  },
  computed: {
    lotesAVencer() {
      const hoje = new Date();
      return this.lotes.filter((lote) => new Date(lote.expirationDate) > hoje);
    },
    lotesVencidos() {
      const hoje = new Date();
      return this.lotes.filter((lote) => new Date(lote.expirationDate) <= hoje);
    },
    
    produtosAcabando() {
      return this.produtos.filter((produto) => {
        const lotesProduto = this.lotes.filter((lote) => lote.productId === produto.id);
        const quantidadeTotal = lotesProduto.reduce((total, lote) => total + lote.quantity, 0);
        return quantidadeTotal > 0 && quantidadeTotal <= produto.minQty;
      });
    },
    produtosAcabaram() {
      return this.produtos.filter((produto) => {
        const lotesProduto = this.lotes.filter(
          (lote) => lote.productId === produto.id && lote.quantity === 0
        );
        return lotesProduto.length > 0;
      });
    },
  },
  mounted() {
    this.fetchProducts();
    this.fetchBatches();
  },
  methods: {
        async fetchProducts() {
          const { data } = await Products().show();
          this.produtos = data;
        },
        async fetchBatches() {
          const { data } = await Batches().show();
          this.lotes = data;
        },
        getProductName(productId) {
          const product = this.produtos.find((produto) => produto.id === productId);
          return product ? product.name : "Produto não encontrado";
        },
        getBatchInfo(productId) {
          const batch = this.produtos.find((produto) => produto.id === productId);
          return batch ? { minQty: batch.minQty} : { minQty: 0};
        },
        daysUntilExpiration(expirationDate) {
          const today = new Date();
          const expiration = new Date(expirationDate);
          const timeDiff = expiration.getTime() - today.getTime();
          const daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));
          return daysDiff;
        },
        daysSinceExpiration(expirationDate) {
        const today = new Date();
        const expiration = new Date(expirationDate);
        const timeDiff = today.getTime() - expiration.getTime();
        const daysDiff = Math.ceil(timeDiff / (1000 * 3600 * 24));
        return daysDiff;
      },
      getQuantidadeTotal(productId) {
      const lotesProduto = this.lotes.filter((lote) => lote.productId === productId);
      return lotesProduto.reduce((total, lote) => total + lote.quantity, 0);
    },
        
  },
};
</script>


	<style scoped>
	
  h1 {
      height: 2px;
      font-family: inter;
      margin: 50px;
      margin-top: 20px;
    }
     h2 {
      font-family: inter;
      margin: 10px;
      padding-left: 40px;
      margin-right: 20px;	
      margin-top: 20px;
     }
     /* conteiner da pagina dois Conteiner */
     .Conteiner{
      display: flex;
      border: 0;
      padding: 0;
      margin: 20px;
    }
    .icon{
      padding: 0 0 0 30px;
  
    }
    .cabecario{
      padding: 0 0 0 18px;
      font-family: semi bold inter;
      font-size: px ;
    }
    .lote{
      padding:  0 0 0 50px;
    }
    /* lote de produtos a vencer */
    .theme--light.v-sheet.Avencer {
      display: flex;
      background-color: #f4b849f3;
      border-color: #fff;
      color: rgba(0,0,0,.87);
  }
  .theme--light.v-sheet.boxAvencer {
      background-color: #f4b8497e;
      border-color: #fff;
  }
    /* lote de produtos vencido  */
    .theme--light.v-sheet.boxvencer {
      background-color: #f5767650;
      border-color: #fff;
  }
    .theme--light.v-sheet.Vencido {
      display: flex;
      background-color: #d66565b7;
      border-color: #fff;
      color: rgba(0,0,0,.87);
  }
    /* lote de produtos a vencer */
    .theme--light.v-sheet.Acabando {
      display: flex;
      background-color: #f4b849f3;
      border-color: #fff;
      color: rgba(0,0,0,.87);
  }
  .theme--light.v-sheet.boxAcabando {
      background-color: #f4b8497e;
      border-color: #fff;
  }
  /* lote de produtos que Acabaram */
  .theme--light.v-sheet.boxAcabaram {
      background-color: #f5767650;
      border-color: #fff;
  }
    .theme--light.v-sheet.Acabaram {
      display: flex;
      background-color: #d66565b7;
      border-color: #fff;
      color: rgba(0,0,0,.87);
  }
    /* botaõ de gerecimento de listagem dos produtos */
    .theme--light.v-btn.pontos{
      font-size: 24px;
      margin-left: 12px;
      margin: 0;
      padding: 0;
      margin-left: 77%;
      border-radius: 20%;
      width: 6%;
      height: 9%;
      background-color: rgb(183, 185, 187);
    }
    /* linha divisoria de lotes de produtos  */
    div.linha{
       border-top:  0.4px solid #347025 ;
       margin: 20px;
       margin-left: 50px;
       width: 78%;
    }
  
  /* tamanho dos crad da tela  */
    .v-sheet.v-card {
      border-radius: 30px;
      width: 20%;
      height: 40%;
      margin: 10px;
      background-color:  #f1ebeb00;;
  }
  ;
	</style>
	