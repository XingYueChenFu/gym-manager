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
							<router-link to="/member/add" class="nav-link">Add new member</router-link>
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
			<!-- 问候语 + 日期选择 -->
			<div class="row">
				<div class="col-md-12 grid-margin">
					<div class="row">
						<div class="col-12 col-xl-8 mb-4 mb-xl-0">
							<h3 class="font-weight-bold">Welcome</h3> <!-- 管理员姓名 -->
							<!-- <h6 class="font-weight-normal mb-0">All systems are running smoothly! You have
						<span class="text-primary">3 unread alerts!</span>
					</h6> -->
						</div>
						<div class="col-12 col-xl-4">
							<div class="justify-content-end d-flex">
								<div class="dropdown flex-md-grow-1 flex-xl-grow-0">
									<button class="btn btn-sm btn-light bg-white dropdown-toggle" type="button"
										id="dropdownMenuDate2" data-bs-toggle="dropdown" aria-haspopup="true"
										aria-expanded="true">
										<i class="mdi mdi-calendar"></i>{{ selectedDate }}</button>
									<div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuDate2">
										<!-- <a class="dropdown-item" href="#" @click.prevent="selectDate(1)">{{ today }}</a>
										<a class="dropdown-item" href="#" @click.prevent="selectDate(2)">{{ yesterday }}</a>
										<a class="dropdown-item" href="#" @click.prevent="selectDate(3)">{{ week }}</a>
										<a class="dropdown-item" href="#" @click.prevent="selectDate(4)">{{ month }}</a> -->
										<a class="dropdown-item" href="#" @click.prevent="selectDate(0)">{{ today }}</a>
										<a class="dropdown-item" href="#" @click.prevent="selectDate(1)">{{ yesterday }}</a>
										<a class="dropdown-item" href="#" @click.prevent="selectDate(2)">{{ week }}</a>
										<a class="dropdown-item" href="#" @click.prevent="selectDate(3)">{{ month }}</a>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<!-- 柱状图 / 卡片栏 -->
			<div class="row">
				<!-- 活动轮播图 -->
				<div class="col-md-6 grid-margin stretch-card">
					<div class="card position-relative">
						<div class="card-body">
							<div id="detailedReports"
								class="carousel slide detailed-report-carousel position-static pt-2"
								data-bs-ride="carousel">
								<div class="carousel-inner">
									<div class="carousel-item active">
										<div class="row">
										</div>
									</div>
									<div class="carousel-item">
										<div class="row">
											<div class="col-md-12 col-xl-3 d-flex flex-column justify-content-start">
												<div class="ml-xl-4 mt-3">
													<p class="card-title">Detailed Reports</p>
													<h1 class="text-primary">$34040</h1>
													<h3 class="font-weight-500 mb-xl-4 text-primary">North America</h3>
													<p class="mb-2 mb-xl-0">The total number of sessions within the date
														range.
														It is the
														period time a user is actively engaged with your website, page
														or
														app,
														etc</p>
												</div>
											</div>
											<div class="col-md-12 col-xl-9">
												<div class="row">
													<div class="col-md-6 border-right">
														<div class="table-responsive mb-3 mb-md-0 mt-3">
															<table class="table table-borderless report-table">
																<tr>
																	<td class="text-muted">Illinois</td>
																	<td class="w-100 px-0">
																		<div class="progress progress-md mx-4">
																			<div class="progress-bar bg-primary"
																				role="progressbar" style="width: 70%"
																				aria-valuenow="70" aria-valuemin="0"
																				aria-valuemax="100"></div>
																		</div>
																	</td>
																	<td>
																		<h5 class="font-weight-bold mb-0">713</h5>
																	</td>
																</tr>
																<tr>
																	<td class="text-muted">Washington</td>
																	<td class="w-100 px-0">
																		<div class="progress progress-md mx-4">
																			<div class="progress-bar bg-warning"
																				role="progressbar" style="width: 30%"
																				aria-valuenow="30" aria-valuemin="0"
																				aria-valuemax="100"></div>
																		</div>
																	</td>
																	<td>
																		<h5 class="font-weight-bold mb-0">583</h5>
																	</td>
																</tr>
																<tr>
																	<td class="text-muted">Mississippi</td>
																	<td class="w-100 px-0">
																		<div class="progress progress-md mx-4">
																			<div class="progress-bar bg-danger"
																				role="progressbar" style="width: 95%"
																				aria-valuenow="95" aria-valuemin="0"
																				aria-valuemax="100"></div>
																		</div>
																	</td>
																	<td>
																		<h5 class="font-weight-bold mb-0">924</h5>
																	</td>
																</tr>
																<tr>
																	<td class="text-muted">California</td>
																	<td class="w-100 px-0">
																		<div class="progress progress-md mx-4">
																			<div class="progress-bar bg-info"
																				role="progressbar" style="width: 60%"
																				aria-valuenow="60" aria-valuemin="0"
																				aria-valuemax="100"></div>
																		</div>
																	</td>
																	<td>
																		<h5 class="font-weight-bold mb-0">664</h5>
																	</td>
																</tr>
																<tr>
																	<td class="text-muted">Maryland</td>
																	<td class="w-100 px-0">
																		<div class="progress progress-md mx-4">
																			<div class="progress-bar bg-primary"
																				role="progressbar" style="width: 40%"
																				aria-valuenow="40" aria-valuemin="0"
																				aria-valuemax="100"></div>
																		</div>
																	</td>
																	<td>
																		<h5 class="font-weight-bold mb-0">560</h5>
																	</td>
																</tr>
																<tr>
																	<td class="text-muted">Alaska</td>
																	<td class="w-100 px-0">
																		<div class="progress progress-md mx-4">
																			<div class="progress-bar bg-danger"
																				role="progressbar" style="width: 75%"
																				aria-valuenow="75" aria-valuemin="0"
																				aria-valuemax="100"></div>
																		</div>
																	</td>
																	<td>
																		<h5 class="font-weight-bold mb-0">793</h5>
																	</td>
																</tr>
															</table>
														</div>
													</div>
													<div class="col-md-6 mt-3">
														<div class="daoughnutchart-wrapper">
															<canvas id="south-america-chart"></canvas>
														</div>
														<div id="south-america-chart-legend"></div>
													</div>
												</div>
											</div>
										</div>
									</div>
								</div>
								<a class="carousel-control-prev" href="#detailedReports" role="button"
									data-bs-slide="prev">
									<span class="carousel-control-prev-icon" aria-hidden="true"></span>
								</a>
								<a class="carousel-control-next" href="#detailedReports" role="button"
									data-bs-slide="next">
									<span class="carousel-control-next-icon" aria-hidden="true"></span>
								</a>
							</div>
						</div>
					</div>
				</div>
				<!-- 数据卡片 -->
				<div class="col-md-6 grid-margin transparent">
					<div class="row">
						<div class="col-md-6 mb-4 stretch-card transparent">
							<div class="card card-tale">
								<div class="card-body">
									<div class="row">
										<div class="col">
											<p class="mb-4">Member Traffic</p>
											<div class="d-flex align-items-center justify-content-center">
												<i class="bi bi-people-fill fa-5x"></i>
												<span style="width: 15px;"></span>
												<p class="mr-3 pl-2 pt-3" style="font-size: 50px;">{{ memberTraffic }}</p>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col-md-6 mb-4 stretch-card transparent">
							<div class="card card-dark-blue">
								<div class="card-body">
									<div class="row">
										<div class="col">
											<p class="mb-4">New Member</p>
											<div class="d-flex align-items-center justify-content-center">
												<i class="bi bi-person-fill-add fa-5x"></i>
												<span style="width: 15px;"></span>
												<p class="mr-3 pl-2 pt-3" style="font-size: 50px;">{{ newMember }}</p>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
					<div class="row">
						<div class="col-md-6 mb-4 mb-lg-0 stretch-card transparent">
							<div class="card card-light-blue">
								<div class="card-body">
									<div class="row">
										<div class="col">
											<p class="mb-4">Recharge Amount</p>
											<div class="d-flex align-items-center justify-content-center">
												<i class="bi bi-currency-yen fa-5x"></i>
												<p class="mr-3 pl-2 pt-3" style="font-size: 50px;">{{ rechargeAmount}}</p>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col-md-6 mb-4 mb-lg-0 stretch-card transparent">
							<div class="card tale-bg">
								<div class="card-people mt-auto">
									<img src="../../public/assets_skydash/images/dashboard/people.svg" alt="people">
									<div class="weather-info">
										<div class="d-flex">
											<div>
												<h2 class="mb-0 font-weight-normal">
													<i class="icon-sun me-2"></i>6<sup>C</sup>
												</h2>
											</div>
											<div class="ms-2">
												<h4 class="location font-weight-normal">成都</h4>
												<h6 class="font-weight-normal">江安</h6>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="col-md-6 grid-margin stretch-card">
					<div class="card">
						<div class="card-body">
							<p class="card-title">Order Details</p>
							<p class="font-weight-500">The total number of sessions within the date range. It is the
								period
								time
								a user is actively engaged with your website, page or app, etc</p>
							<div class="d-flex flex-wrap mb-5">
								<div class="me-5 mt-3">
									<p class="text-muted">Order value</p>
									<h3 class="text-primary fs-30 font-weight-medium">12.3k</h3>
								</div>
								<div class="me-5 mt-3">
									<p class="text-muted">Orders</p>
									<h3 class="text-primary fs-30 font-weight-medium">14k</h3>
								</div>
								<div class="me-5 mt-3">
									<p class="text-muted">Users</p>
									<h3 class="text-primary fs-30 font-weight-medium">71.56%</h3>
								</div>
								<div class="mt-3">
									<p class="text-muted">Downloads</p>
									<h3 class="text-primary fs-30 font-weight-medium">34040</h3>
								</div>
							</div>
							<canvas id="order-chart"></canvas>
						</div>
					</div>
				</div>
				<div class="col-md-6 grid-margin stretch-card">
					<div class="card">
						<div class="card-body">
							<div class="d-flex justify-content-between">
								<p class="card-title">Sales Report</p>
								<a href="#" class="text-info">View all</a>
							</div>
							<p class="font-weight-500">The total number of sessions within the date range. It is the
								period
								time
								a user is actively engaged with your website, page or app, etc</p>
							<div id="sales-chart-legend" class="chartjs-legend mt-4 mb-2"></div>
							<canvas id="sales-chart"></canvas>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue';
import axios from "axios";
// 格式化日期函数
function formatDate(date: Date): string {
	const options: Intl.DateTimeFormatOptions = { day: '2-digit', month: 'short', year: 'numeric' };
	return date.toLocaleDateString('en-US', options);
}

// 计算日期范围
const todayDate = new Date();
const yesterdayDate = new Date(todayDate);
yesterdayDate.setDate(todayDate.getDate() - 1);

// 本周开始和结束日期（假设周一为一周的开始）
const startOfWeek = new Date(todayDate);
startOfWeek.setDate(todayDate.getDate() - 7);

// 上个月开始和结束日期
const startOfPast30Days = new Date(todayDate);
startOfPast30Days.setDate(todayDate.getDate() - 30);

// 响应式字符串
const today = ref(`Today (${formatDate(todayDate)})`);
const yesterday = ref(`Yesterday (${formatDate(yesterdayDate)})`);
const week = ref(`Last Week (${formatDate(startOfWeek)} - `); // ref(`Last Week (${formatDate(startOfWeek)} - ${formatDate(endOfWeek)})`);
const month = ref(`Last Month (${formatDate(startOfPast30Days)} - `); // ref(`Last Week (${formatDate(startOfWeek)} - ${formatDate(endOfWeek)})`);

// 明确定义 datas 数组类型
const datas: Ref<string>[] = [today, yesterday, week, month];
const start_times = [
	formatDate(todayDate),
	formatDate(yesterdayDate),
	formatDate(startOfWeek),
	formatDate(startOfPast30Days),
];

const end_times = [
	formatDate(todayDate),
	formatDate(yesterdayDate),
	formatDate(todayDate),
];

const time_slots  =  [
	{
		start_time: start_times[0],
		end_time: end_times[0],
	},
	{
		start_time: start_times[1],
		end_time: end_times[1],
	},
	{
		start_time: start_times[2],
		end_time: end_times[2],
	},
	{
		start_time: start_times[3],
		end_time: end_times[3],
	},
];
// 定义当前选中的日期文本
const selectedDate: Ref<string> = ref(today.value);
const time_slot  =  ref({
	start_time: start_times[0],
	end_time: end_times[0],
});
// 处理日期切换的函数
const selectDate = (opt: number) => {
    if (opt >= 0 && opt < datas.length) {
        // 确保 opt 在有效范围内，并更新按钮显示的日期
		selectedDate.value = datas[opt].value;
		time_slot.value = time_slots[opt];
    } else {
        console.error('Invalid option index:', opt);
	}
	console.log(time_slot);
	fetchNewMember();
};

const newMember :Ref<number> = ref(0);
const memberTraffic :Ref<number> = ref(0);
const rechargeAmount: Ref<number> = ref(0);
interface Item {
	time: string;        // 时间
	value: number;       // 值
}
const newMemberData: Ref<Item[]> = ref([]);
const memberTrafficData: Ref<Item[]> = ref([]);
const rechargeAmountData: Ref<Item[]> = ref([]);
// 获取用户充值和消费记录的函数
const fetchNewMember = async () => {
  try {
    // 发送请求
    const response = await axios.post(
		`http://localhost:5000/staff/statements/new_consume`,
		time_slot,
		{
			headers: {
			'Content-Type': 'application/json',
			},
		});
    // 响应处理
    console.log(response.data.data);
	  if (response.data.code === 200) {
		// 填充用户信息
		newMember.value = response.data.data.total;
		newMemberData.value = response.data.data.items;
		console.log("用户信息已填充！");
    } else {
      	alert("不存在该会员！");
    }
  } catch (error) {
    console.error("获取用户信息失败:", error);
    alert("获取用户信息失败，请稍后再试！");
  }
};
</script>

