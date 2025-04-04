<template>
  <v-autocomplete
    :items="items"
    v-bind="$attrs"
    clearable
    dense
    height="32"
    outlined
    v-on="$listeners"
    loading-text="Carregando... Aguarde"
    no-data-text="Sem dados disponíveis"
    @change="onChanged($event)"
  >
  </v-autocomplete>
</template>

<script>
export default {
  name: "BaseSelectService",
  props: {
    service: {
      type: String,
      default: String(),
    },
  },
  data() {
    return {
      items: [],
      itemText: [],
      httpService: {},
    };
  },
  methods: {
    async fetchLocalServices() {
      const service = await import(`../services/${this.service}`);
      this.httpService = service.default();
    },

    async fetchResource() {
      const { data } = await this.httpService.show();
      this.items = data;
    },

    onChanged(item) {
      this.$emit("onChanged", item);
    },
  },
  async mounted() {
    await this.fetchLocalServices();
    await this.fetchResource();
  },
};
</script>

<style scoped>
::v-deep .v-input__append-inner {
  margin-top: 5px !important;
}
</style>