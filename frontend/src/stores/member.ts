import { defineStore } from 'pinia';

export const useMemberStore = defineStore('member', {
	state: () => ({
		memberInfo: {
			member_id: '',
		},
	}),
	actions: {
		setMemberInfo(member_id: string) {
			this.memberInfo = { member_id };
		},
	},
});
