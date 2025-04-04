import { createToastInterface } from "vue-toastification";
import "vue-toastification/dist/index.css";

const pluginOptions = { timeout: 3000 };
const toast = createToastInterface(pluginOptions);

export default (response, messages = {}) => {
  const statusCode = response?.status;

  if (statusCode >= 200 && statusCode < 300) {
    const successMessage = messages.success || "Operação realizada com sucesso.";
    toast.success(successMessage);
    return true;
  } else {
    const errorMessage = messages.error || "Ocorreu um erro ao realizar a operação.";
    toast.error(errorMessage);
    return false;
  }
};
