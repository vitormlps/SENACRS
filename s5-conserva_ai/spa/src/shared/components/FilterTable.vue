<template>
	<div class="container-filter d-flex justify-content-around align-items-center pt-10">
		<slot></slot>
	</div>
</template>
<script>
export default {};
</script>
<style scoped>
.container-filter {
	gap: 30px;
	max-width: 100vw;
}

.v-text-field >>> .v-input__control .v-input__slot {
	min-height: 0 !important;
	padding: 0 8px !important;
	margin-bottom: 2px !important;
	display: flex !important;
	align-items: center !important;
}

.v-text-field >>> .v-input__control .v-input__slot .v-input__prepend-inner .v-icon {
	color: var(--v-primary-base) !important;
	font-size: 20px !important;
}

.v-text-field >>> .v-label {
	font-size: 12px !important;
}
</style>
