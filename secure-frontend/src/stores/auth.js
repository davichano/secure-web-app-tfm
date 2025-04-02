import {defineStore} from 'pinia';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        accessToken: null,
        userPermissions: [],
    }),
    actions: {
        setAccessToken(token) {
            this.accessToken = token;
        },
        clearAccessToken() {
            this.accessToken = null;
        },
        setUserPermissions(permissions) {
            this.userPermissions = permissions;
        },
    },
    getters: {
        isAuthenticated: (state) => !!state.accessToken,
        hasPermission: (state) => (permission) => state.userPermissions.includes(permission),
    },
});
