import { defineStore } from 'pinia';

export const useMemberStore = defineStore('member', {
	state: () => ({
		memberInfo: {
			member_id: '',
		},
		memberAdd: {
			type: -1,
			value: '',
		}
	}),
	actions: {
		setMemberInfo(member_id: string) {
			this.memberInfo = { member_id };
		},
		setMemberAddInfo(type: number, value: string) {
			this.memberAdd = { type, value };
		},
	},
});
