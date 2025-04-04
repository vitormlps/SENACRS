<template>
  <div class="d-flex justify-end pt-5 pr-9" style="gap: 2vw">
    <div>
      <v-text-field
        v-model="searchInput"
        outlined
        prepend-inner-icon="mdi-magnify"
        :label="`Pesquisar ${title}`"
        solo
        clearable
        elevation="1"
      />
    </div>
    <v-btn small class="pt-" color="btn-text primary" elevation="0" @click="openModal">
      <v-icon size="20" color="black">mdi-plus</v-icon>
      {{ labelButton }}
    </v-btn>
  </div>
</template>
<script>
export default {
  name: 'Header',
  props: {
    title: {
      type: String,
      default: '',
    },
    labelButton: {
      type: String,
      default: 'Novo',
    },
  },
  data() {
    return {
      modalForm: false,
      searchInput: '',
    }
  },

  mounted() {
    this.setPageTitle()
  },
  methods: {
    setPageTitle() {
      localStorage.setItem('title', this.title)
    },
    openModal() {
      this.$emit('openModal', true)
    },
  },
  watch: {
    searchInput(value, oldValue) {
      this.$emit('search', value)
    },
  },
}
</script>
<style scoped>
.v-text-field >>> .v-input__control .v-input__slot {
  width: 18vw;
  height: 30px;
  padding: 0 8px !important;
  margin-bottom: 2px !important;
  display: flex !important;
  align-items: center !important;
  font-size: 14px;
}

.v-text-field .v-input__control .v-input__slot .v-input__prepend-inner .v-icon {
  color: var(--v-primary-base) !important;
  font-size: 20px !important;
}

.v-text-field .v-label {
  font-size: 12px !important;
}
</style>
