import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
	state: () => ({
		userInfo: {
			name: '',
			passwasd: '',
			level: 0,
		},
	}),
	actions: {
		setUserInfo(name: string, passwasd: string, level: number) {
			this.userInfo = { name, passwasd, level };
		},
	},
});
