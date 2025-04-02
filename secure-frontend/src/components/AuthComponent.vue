<template>
  <div>
    <button @click="login">Iniciar Sesión</button>
    <button @click="logout">Cerrar Sesión</button>
    <p v-if="isAuthenticated">Usuario autenticado</p>
    <p v-else>Por favor, inicie sesión</p>
  </div>
</template>

<script>
import {useAuthStore} from '@/stores/auth';

export default {
  setup() {
    const authStore = useAuthStore();

    const login = () => {
      authStore.setAccessToken('example-jwt-token');
    };

    const logout = () => {
      authStore.clearAccessToken();
    };

    return {
      login,
      logout,
      isAuthenticated: authStore.isAuthenticated,
    };
  },
};
</script>
