<template>
    <div>
        <div class="d-flex ml-4">
            <!-- <v-icon class="mr-4" size="30" @click="backToPage">mdi-chevron-left</v-icon> -->

            <h1 class="pl-4">{{ categoryTitle }} &#8226&nbsp</h1>
            <h1 class="title-color">{{ $route.name }}</h1>
        </div>

        <BaseTableService :parentCategory="categoryTitle" :service="service" />
    </div>
</template>

<script>
import BaseTableService from "@/shared/components/BaseTableService.vue";

export default {
  components: {
    BaseTableService,
  },
  data() {
    return {
      service: this.$route.path.split("/")[2].charAt(0).toUpperCase() + this.$route.path.split("/")[2].slice(1),
      categoryTitle: "Gerenciamento",
      backPage: "Gerenciamento"
    };
  },
  methods: {
        backToPage() {
            this.$router.push({ name: this.backPage })
        },
    },
};
</script>

<style scoped>
.title-color {
  color: #5F9551;
}
</style>
