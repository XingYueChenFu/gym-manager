<template>
	<nav class="sidebar"></nav>
	<nav class="sidebar sidebar-offcanvas" id="sidebar" style="position: fixed !important;">
		<ul class="nav">
			<li class="nav-item">
				<router-link to="/main" class="nav-link">
					<i class="icon-grid menu-icon"></i>
					<span class="menu-title">Dashboard</span>
				</router-link>
			</li>
			<li class="nav-item">
				<router-link to="/Activity" class="nav-link">
					<i class="bi bi-fire menu-icon"></i>
					<span class="menu-title">Activity</span>
				</router-link>
			</li>
			<li class="nav-item">
				<router-link to="/search" class="nav-link">
					<i class="icon-search menu-icon"></i>
					<span class="menu-title">Search</span>
				</router-link>
			</li>
			<li class="nav-item">
				<router-link to="/member/add" class="nav-link">
					<i class="bi bi-person-plus-fill menu-icon"></i>
					<span class="menu-title">Add new member</span>
				</router-link>
			</li>

			<li class="nav-item">
				<a class="nav-link" data-bs-toggle="collapse" href="#ui-basic" aria-expanded="false"
					aria-controls="ui-basic">
					<i class="bi bi-person-square menu-icon"></i>
					<span class="menu-title">Member</span>
					<i class="menu-arrow"></i>
				</a>
				<div class="collapse" id="ui-basic">
					<ul class="nav flex-column sub-menu">
						<li class="nav-item">
							<router-link to="/member/detail" class="nav-link">Details</router-link>
						</li>
						<li class="nav-item">
							<router-link to="/member/record" class="nav-link">Record</router-link>
						</li>
						<li class="nav-item">
							<router-link to="/member/recharge" class="nav-link">Recharge</router-link>
						</li>
					</ul>
				</div>
			</li>
		</ul>
	</nav>

  <!-- partial -->
  <div class="main-panel">
    <div class="content-wrapper">
      <div class="col-12 grid-margin row">
        <div class="col-lg-12 grid-margin stretch-card">
                <div class="card">
                  <div class="card-body">
                    <h4 class="card-title">Activity Table</h4>
                    <p class="card-description"> Click an option to <code>Recharge for Member {{ memberId }}</code>
                    </p>
                    <div class="table-responsive">
                      <table class="table">
                        <thead>
                          <tr>
                            <th>Activity</th>  <!-- activity_name -->
                            <th>No.</th>       <!-- plan_id -->
                            <th>Content</th>    <!-- recharge_conut/lifespan - recharge_day -->
                            <th>Amount</th>    <!-- amount -->
                          </tr>
                        </thead>
                        <tbody>
						  	<tr v-for="(opt, index) in opts" :key="index" @click="memberRecharge(index)">
								<td>{{ opt.activity_name }}</td>
								<td>{{ opt.plan_id }}</td>
								<td>{{ opt.obtain }}</td>
								<td>{{ opt.amount }}元</td>
							</tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
      </div>
    </div>
  </div>

</template>


<script lang='ts' setup>
import { ref } from 'vue';
import axios from "axios";
import { useRouter } from 'vue-router';
import { useMemberStore } from '../stores/member';

// 获取 router 实例
const router = useRouter();
const memberStore = useMemberStore();
const memberId = memberStore.$state.memberInfo.member_id;
// console.log(memberStore.$state.memberInfo.member_id);  // 要展示的 member_id

// 定义表格项的接口
interface opt {
//   id: string;        // 充值的时间
//   : string;    // 截止的时间 or none
    'activity_id': number,
	'plan_id': number,
	'activity_name': string,
	'start_time': string,
	'end_time': string,
	'recharge_type': string,
	'recharge_count': number,
	'lifespan': number,
	'recharge_day': number,
	'amount': string,
	'activity_remark': string
	'obtain': string,
}
const opts = ref<opt[]>([]);

const fetchDealForm = async () => {
	try {
		// 发送请求
		const response = await axios.post(
		'http://localhost:5000/staff/query/deal/now',
		{
			headers: {
			'Content-Type': 'application/json',
			},
		});
		// 响应处理
		console.log("活动号：", response.data);
		if (response.data.code === 200) {
			opts.value = response.data.data;
			opts.value.forEach((opt) => {
				if (opt.recharge_type === 'count') {
					opt.obtain = opt.recharge_count + '次 / ' + opt.lifespan + '天';
				} else {
					opt.obtain = opt.recharge_day + '天';
				}
			});
		} else {
			console.log("获取活动信息失败");
			return;
		}
	} catch (error) {
		console.error("获取活动信息失败:", error);
		alert("获取活动信息失败，请稍后再试！");
	}
};
fetchDealForm()


const memberRecharge = async (index:number) => {
	try {
		// 发送请求
		const response = await axios.post(
			'http://localhost:5000/staff/recharge',
			{
				"member_id": memberId,
				"activity_id": opts.value[index].activity_id,
				"plan_id": opts.value[index].plan_id,
			},
			{
				headers: {
				'Content-Type': 'application/json',
				},
			});
		// 响应处理
		if (response.data.code === 200) {
			alert("充值成功，即将返回充值记录页面");
			router.push('/member/record');
		} else {
			console.log("充值失败");
			return;
		}
	} catch (error) {
		console.error("充值失败:", error);
		alert("充值失败，请稍后再试！");
	}
};
</script>