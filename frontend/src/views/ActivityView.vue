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
					<div class="row">
						<h4 class="col-4 card-title">Activity Table</h4>
						<!-- <div class="col-8 justify-content-end d-flex">
							<button type="button" class="btn btn-primary mb-2" @click="handleSubmit">Submit</button>
						</div> -->
						<div class="justify-content-end d-flex col-8">
							<button class="btn btn-light" @click="handleCancel">Cancel</button>
							<span style="width: 2vh;"></span>
							<button type="button" class="btn btn-primary" @click="handleSubmit">{{bt_name}}</button>
						</div>
					</div>
					 <div class="card "> <!-- v-if="isVisible" -->
						<p class="card-description"> Click one, Modify it; or Add New Activity. <code> {{ warnning }} </code> </p>
						<div class="row pt-2">
							<div class="col-2">
								<div class="form-group">
									<label>Activity</label>
									<input type="text" class="form-control form-control-sm" placeholder="Activity Name" v-model="formData.activity_name">
								</div>
							</div>
							<div class="col-2">
								<div class="form-group">
									<label>Type</label>
									<select class="form-select form-select-lg" v-model="formData.recharge_type">
										<option value="time">Time</option>
										<option value="count">Count</option>
									</select>
								</div>
							</div>
							<div class="col-3">
								<div class="form-group" v-if="isVisible">
									<label>Day</label>
									<input type="text" class="form-control form-control-sm" placeholder="obtain Day" v-model="formData.recharge_day">
								</div>
								<div class="row" v-if="!isVisible">
									<div class="form-group col-md-6">
										<label>Count</label>
										<input type="text" class="form-control form-control-sm" placeholder="obtain Count" v-model="formData.recharge_count">
									</div>
									<div class="form-group col-md-6" >
										<label>Lifespan</label>
										<input type="text" class="form-control form-control-sm" placeholder="period of validity" v-model="formData.lifespan">
									</div>
								</div>
							</div>
							<div class="col-2">
								<div class="form-group">
									<label>Amount</label>
									<input type="text" class="form-control form-control-sm" placeholder="Plan Amount" v-model="formData.amount">
								</div>
							</div>
							<div class="col-3">
								<div class="row">
									<div class="form-group col-md-6">
										<label>Start Time</label>
										<input type="text" class="form-control form-control-sm" placeholder="xxxx-xx-xx" v-model="formData.start_time">
									</div>
									<div class="form-group col-md-6" >
										<label>End Time</label>
										<input type="text" class="form-control form-control-sm" placeholder="year-month-day" v-model="formData.end_time">
									</div>
								</div>
							</div>
						</div>
					</div>

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
						  	<tr v-for="(opt, index) in opts" :key="index" @click="cheakDetail(index)">
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
import { ref, computed } from 'vue';
import axios from "axios";

// 定义表格项的接口
interface opt {
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
// 获取活动详情
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

// 响应式表单数据
const formData = ref({
	'activity_name': '',
	'start_time': '',
	'end_time': '',
	'recharge_type': 'time',
	'recharge_count': null,
	'lifespan': null,
	'recharge_day': null,
	'amount': null,
	'activity_remark': null,
});
// 修改的活动索引
const idx = ref<number>(-1);
// 修改活动的警告
const warnning = ref<string>('');
const bt_name = ref<string>('Add');
// const isVisible = ref<boolean>(false);
const isVisible = computed(() => {
  if (formData.value.recharge_type === 'time') {
    return true;
  } else {
    return false;
  }
});
// 提交按钮的处理逻辑
const handleSubmit = async () => {
  try {
    const payload = { ...formData.value }; // 提交前的表单数据
	  // 发送 POST 请求
	let path = '';
	if (idx.value === -1) {  // 新增
		path = 'http://localhost:5000/staff/add/deal';
	  }
	else {  // 修改
		path = 'http://localhost:5000/staff/modify/deal';
	}

    const response = await axios.post(
      path,
      [payload,],
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    console.log('Response:', response.data);
    // 请求成功后的处理逻辑
    if (response.data.code === 200) {
		alert('Activity added successfully!');
		handleCancel();
      	fetchDealForm();
    }
    else {
      alert('Failed to add Activity.');
    }
  } catch (error) {
    // 请求失败的处理逻辑
    console.error('Error while adding Activity:', error);
    alert('Failed to add Activity.');
  }
};
const cheakDetail = (index: number) => {
	Object.assign(formData.value, opts.value[index]);
	idx.value = index;
	warnning.value = 'Check And Modify The Activity ' + `${index + 1}` + ' !';
	bt_name.value = 'Modify';
};
const handleCancel = () => {
	idx.value = -1;
	warnning.value = '';
	bt_name.value = 'Add';
	Object.assign(formData.value, {
		'activity_name': '',
		'start_time': '',
		'end_time': '',
		'recharge_count': null,
		'lifespan': null,
		'recharge_day': null,
		'amount': null,
		'activity_remark': null,
	});
};
</script>