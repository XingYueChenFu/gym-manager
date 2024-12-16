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
				<router-link to="/search" class="nav-link">
					<i class="icon-search menu-icon"></i>
					<span class="menu-title">Search</span>
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
							<router-link to="/member/add" class="nav-link">Add new member</router-link>
						</li>
						<li class="nav-item">
							<router-link to="/member/recharge" class="nav-link">Recharge</router-link>
						</li>
					</ul>
				</div>
			</li>
			<li class="nav-item">
				<a class="nav-link" data-bs-toggle="collapse" href="#form-elements" aria-expanded="false"
					aria-controls="form-elements">
					<i class="icon-columns menu-icon"></i>
					<span class="menu-title">Form elements</span>
					<i class="menu-arrow"></i>
				</a>
				<div class="collapse" id="form-elements">
					<ul class="nav flex-column sub-menu">
						<li class="nav-item"><a class="nav-link" href="../../pages/forms/basic_elements.html">Basic
								Elements</a></li>
					</ul>
				</div>
			</li>
			<li class="nav-item">
				<a class="nav-link" data-bs-toggle="collapse" href="#charts" aria-expanded="false"
					aria-controls="charts">
					<i class="icon-bar-graph menu-icon"></i>
					<span class="menu-title">Charts</span>
					<i class="menu-arrow"></i>
				</a>
				<div class="collapse" id="charts">
					<ul class="nav flex-column sub-menu">
						<li class="nav-item"> <a class="nav-link" href="../../pages/charts/chartjs.html">ChartJs</a>
						</li>
					</ul>
				</div>
			</li>
			<li class="nav-item">
				<a class="nav-link" data-bs-toggle="collapse" href="#tables" aria-expanded="false"
					aria-controls="tables">
					<i class="icon-grid-2 menu-icon"></i>
					<span class="menu-title">Tables</span>
					<i class="menu-arrow"></i>
				</a>
				<div class="collapse" id="tables">
					<ul class="nav flex-column sub-menu">
						<li class="nav-item"> <a class="nav-link" href="../../pages/tables/basic-table.html">Basic
								table</a>
						</li>
					</ul>
				</div>
			</li>
			<li class="nav-item">
				<a class="nav-link" data-bs-toggle="collapse" href="#icons" aria-expanded="false" aria-controls="icons">
					<i class="icon-contract menu-icon"></i>
					<span class="menu-title">Icons</span>
					<i class="menu-arrow"></i>
				</a>
				<div class="collapse" id="icons">
					<ul class="nav flex-column sub-menu">
						<li class="nav-item"> <a class="nav-link" href="../../pages/icons/mdi.html">Mdi icons</a></li>
					</ul>
				</div>
			</li>
			<li class="nav-item">
				<a class="nav-link" data-bs-toggle="collapse" href="#auth" aria-expanded="false" aria-controls="auth">
					<i class="icon-head menu-icon"></i>
					<span class="menu-title">User Pages</span>
					<i class="menu-arrow"></i>
				</a>
				<div class="collapse" id="auth">
					<ul class="nav flex-column sub-menu">
						<li class="nav-item"> <a class="nav-link" href="../../pages/samples/login.html"> Login </a></li>
						<li class="nav-item"> <a class="nav-link" href="../../pages/samples/register.html"> Register
							</a></li>
					</ul>
				</div>
			</li>
			<li class="nav-item">
				<a class="nav-link" data-bs-toggle="collapse" href="#error" aria-expanded="false" aria-controls="error">
					<i class="icon-ban menu-icon"></i>
					<span class="menu-title">Error pages</span>
					<i class="menu-arrow"></i>
				</a>
				<div class="collapse" id="error">
					<ul class="nav flex-column sub-menu">
						<li class="nav-item"> <a class="nav-link" href="../../pages/samples/error-404.html"> 404 </a>
						</li>
						<li class="nav-item"> <a class="nav-link" href="../../pages/samples/error-500.html"> 500 </a>
						</li>
					</ul>
				</div>
			</li>
			<!-- <li class="nav-item">
				<a class="nav-link" href="../../../docs/documentation.html">
				<i class="icon-paper menu-icon"></i>
				<span class="menu-title">Documentation</span>
				</a>
			</li> -->
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
			  <p class="card-description"> Count </p>
              <div class="table-responsive pb-3">
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
                    <tr v-for="(item, index) in counts" :key="index">
						<td>{{ `${index+1}` }}</td>
						<td>{{ item.time }}</td>           <!-- 充值时间 -->
						<td>{{ item.deadline }}</td>
						<td>{{ item.count }}</td>
						<td>
							<div class="progress" style="height: 20px;">
								<div class="progress-bar bg-success" role="progressbar" :style="`width: ${item.rate}%;`">{{item.rate}}%</div>
							</div>
						</td>
						<td>{{ item.amount }}</td>
                    </tr>
                  </tbody>
                </table>
              </div>
			  <p class="card-description"> Times </p>
			  <div class="table-responsive pb-3">
                 <table class="table table-bordered"> <!-- table-bordered -->
                  <thead>
                    <tr>
                      <th> # </th>  <!-- index -->
                      <th> Recharge time </th>
					  <!-- <th> Deadline </th> -->
                      <!-- <th> Time elapsed </th> -->
                      <th> Days </th>
					  <!-- <th> Consumption rate </th> -->
					  <th> Amount </th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(item, index) in times" :key="index">
						<td>{{ `${index+1}` }}</td>
						<td>{{ item.time }}</td>           <!-- 充值时间 -->
						<!-- <td>{{ item.deadline }}</td> -->
						<td>{{ item.count }}</td>
						<!-- <td>
							<div class="progress" style="height: 20px;">
								<div class="progress-bar bg-success" role="progressbar" :style="`width: ${item.rate}%;`">{{item.rate}}%</div>
							</div>
						</td> -->
						<td>{{ item.amount }}</td>
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
console.log(memberStore.$state.memberInfo.member_id);  // 要展示的 member_id
// 定义表格项的接口
interface Item {
  time: string;        // 充值的时间
  deadline: string;    // 截止的时间 or none
  count: number;       // 充值得到的总数量 or 时间
  rate: number;        // 时间过去的比例
  amount: number;      // 充值的金额
}
// 定义响应式数据存储表格项
const total_count = ref<number>(0);
const total_time = ref<number>(0);
// const items = ref<Item[]>([]);
const counts = ref<Item[]>([
  {
    time: '2025-07-16 22:09:441',
    deadline: '2027-07-16 22:09:441',
	count: 20,
    rate: 20,
    amount: 77.99,
  },
]);

const times = ref<Item[]>([
  {
    time: '2025-07-16 22:09:441',
	deadline: '2027-07-16 22:09:441',
	count: 20,
    rate: 30,
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
// const time = '2025-07-16 22:09:44';
// const deadline = '2027-07-16 22:09:44';

// // 调用函数
// const ratio = calculateTimeRatio(time, deadline);
// console.log(typeof(ratio));
// console.log(`已过时间的比例：${ratio}%`);

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
		total_count.value = response.data.data.total_count;  // 将返回数据赋值给 items
		total_time.value = response.data.data.total_time;  // 将返回数据赋值给 items
		counts.value = response.data.data.counts;  // 将返回数据赋值给 items
		times.value = response.data.data.times;  // 将返回数据赋值给 items
		counts.value.forEach((item) => {
			item.rate = calculateTimeRatio(item.time, item.deadline);
		});
		times.value.forEach((item) => {
			item.rate = calculateTimeRatio(item.time, item.deadline);
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