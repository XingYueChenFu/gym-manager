import { defineStore } from 'pinia';

export const useMemberStore = defineStore('member', {
	state: () => ({
		memberInfo: {
			member_id: '0010',
		},
	}),
	actions: {
		setMemberInfo(member_id: string) {
			this.memberInfo = { member_id };
		},
	},
});
