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
              <h4 class="card-title">Consumption And Recharge Records</h4>
              <div class="table-responsive pt-3">
                 <table class="table table-bordered"> <!-- table-bordered -->
                  <thead>
                    <tr>
                      <th> # </th>  <!-- index -->
                      <th> Recharge time </th>
					  <th> Deadline </th>
                      <!-- <th> Time elapsed </th> -->
                      <th> Count </th>
					  <th> Consumption rate </th>
					  <th> Amount </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
						<td> 1 </td>
						<td> 2025-07-16 22:09:441 </td>
						<td> 2027-07-16 22:09:441 </td>
                        <td> 20 </td>
					  	<td>
							<div class="progress" style="height: 20px;">
								<div class="progress-bar bg-primary" role="progressbar" style="width: 30%;">30</div>
								<div class="progress-bar bg-success" role="progressbar" style="width: 40%;">70</div>
							</div>
						</td>
						<td> $ 77.99 </td>
                    </tr>
                    <tr v-for="(item, index) in items" :key="index">
						<td>{{ `${index+1}` }}</td>
						<td>{{ item.time }}</td>           <!-- 充值时间 -->
						<td>{{ item.deadline }}</td>
						<td>{{ item.count }}</td>
						<td>
							<div class="progress" style="height: 20px;">
								<div class="progress-bar" :class="item.rate.c1 ? 'bg-primary' : 'bg-success'" role="progressbar" :style="`width: ${item.rate.r1}%;`">{{item.rate.r1}}%</div>
								<div class="progress-bar" :class="item.rate.c2 ? 'bg-primary' : 'bg-success'" role="progressbar" :style="`width: ${item.rate.r2 - item.rate.r1}%;`">{{item.rate.r2}}%</div>
							</div>
						</td>
						<td>{{ item.amount }}</td>
                    </tr>
                    details
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
console.log(memberStore.$state.memberInfo.member_id);  // 要展示的 member_id
// 定义表格项的接口
interface Rate {
  c1: boolean;
  r1: number;
  c2: boolean;
  r2: number;
}
interface Item {
  time: string;
  deadline: string;
  count: number;       // 充值得到的总数量
  count_used: number;  // 未使用数量
  rate: Rate;
  amount: number;
}
// 定义响应式数据存储表格项
// const items = ref<Item[]>([]);
const counts = ref<Item[]>([
  {
    time: '2025-07-16 22:09:441',
    deadline: '2027-07-16 22:09:441',
	count: 20,
	count_used: 10,
    rate: {
      c1: true,
      r1: 30,
      c2: false,
      r2: 50,
    },
    amount: 77.99,
  },
]);

const times = ref<Item[]>([
  {
    time: '2025-07-16 22:09:441',
    deadline: '2027-07-16 22:09:441',
    rate: {
      c1: true,
      r1: 30,
      c2: false,
      r2: 50,
    },
    amount: 77.99,
  },
]);

const calculateTimeRatio = (time:string, deadline:string) => {
  // 将时间字符串解析为 Date 对象
  const startTime = new Date(time).getTime();;
  const endTime = new Date(deadline).getTime();;
  const now = Date.now() // new Date().getTime(); // 当前时间

  // 检查时间有效性
  if (now < startTime) {
    return 0; // 如果当前时间早于起始时间，返回 0%
  }
  if (now > endTime) {
    return 100; // 如果当前时间晚于截止时间，返回 100%
  }

  // 计算时间差（毫秒）
  const totalDuration = endTime - startTime; // 总时间跨度
  const elapsedDuration = now - startTime; // 已经过的时间

  // 计算比例
  const ratio = (elapsedDuration / totalDuration) * 100;

  return ratio; // 返回保留两位小数的百分比
};

// 示例输入
const time = '2025-07-16 22:09:44';
const deadline = '2027-07-16 22:09:44';

// 调用函数
const ratio = calculateTimeRatio(time, deadline);
console.log(typeof(ratio));
console.log(`已过时间的比例：${ratio}%`);

// const calculateRate = (count: number, count_used: number, time:string, deadline:string) => {
// 	let rate1 :number = Math.floor((count_used / count) * 100);
// 	let rate2 :number = Math.floor(calculateTimeRatio(time, deadline));
// 	console.log(rate1, rate2);
// 	const d_rate :number = rate1 - rate2;
// 	if (d_rate < 0) {
// 		rate2 = -d_rate;
// 	} else {
// 		rate1 = rate2;
// 		rate2 = d_rate;
// 	}
// 	return {
// 		c1: d_rate > 0,
// 		r1: rate1,
// 		c2: d_rate < 0,
// 		r2: rate1 + rate2,
// 	};
// };


// 获取用户充值和消费记录的函数
const fetchMemberReCharge = async () => {
  try {
    if (memberId === '') {
      console.log("memberId is empty");
      alert("请先搜索！");
      router.push('/search');
      return;
    }

    // 发送请求
    const response = await axios.post(
      `http://localhost:5000/staff/query/record/${memberId}`,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      });
    // 响应处理
    console.log(response.data.data);
    if (response.data.code === 200) {
		items.value = response.data.data;  // 将返回数据赋值给 items
		items.value.forEach((item) => {
			item.rate = calculateRate(item.count, item.count_used, item.time, item.deadline);
		});
      	console.log("用户信息已填充！");
    } else {
      	alert("不存在该会员！");
    }
  } catch (error) {
    console.error("获取用户信息失败:", error);
    alert("获取用户信息失败，请稍后再试！");
  }
};
fetchMemberReCharge();
</script>