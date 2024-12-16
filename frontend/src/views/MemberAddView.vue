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
      <div class="col-12 grid-margin">
        <div class="card">
          <div class="card-body">
            <div class="row">
              <h4 class="col-4 card-title">Add new member</h4>
              <div class="col-8">
                <div class="justify-content-end d-flex">
                  <button type="button" class="btn btn-primary mb-2" @click="handleSubmit">Submit</button>
                </div>
              </div>
            </div>
            <form class="form-sample">
              <p class="card-description"> Personal info </p>
              <!-- 姓名 + 昵称 -->
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Name</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" v-model="formData.realname" />
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Neck Name</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" v-model="formData.nickname" />
                    </div>
                  </div>
                </div>
              </div>
              <!-- 学生卡 + 手机号 -->
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Student Card</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" v-model="formData.student_card" />
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Phone Number</label>
                    <div class="col-sm-9">
                      <input type="text" class="form-control" v-model="formData.phone_number" />
                    </div>
                  </div>
                </div>
              </div>
              <!-- 性别 + 会员类型 -->
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Gender</label>
                    <div class="col-sm-9">
                      <select class="form-select form-select-lg" v-model="formData.gender">
                        <option value="M">Male</option>
                        <option value="F">Female</option>
                      </select>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Membership</label>
                    <div class="col-sm-9">
                      <select class="form-select form-select-lg" v-model="formData.membership">
                        <option value="member">Member</option>
                        <option value="administrator">Administrator</option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>
              <!-- 地址 + 校区 -->
              <p class="card-description"> Address </p>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Campus</label>
                    <div class="col-sm-9">
                      <select class="form-select form-select-lg" v-model="formData.campus">
                        <option value="江安">江安</option>
                        <option value="望江">望江</option>
                        <option value="华西">华西</option>
                      </select>
                    </div>
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Address</label>
                    <div class="col-sm-9">
                      <!-- <input type="text" class="form-control" v-model="formData.address" /> -->
                      <textarea class="form-control" row="4" v-model="formData.address" />
                    </div>
                  </div>
                </div>
              </div>

            </form>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script lang="ts" setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useMemberStore } from '../stores/member';
// 获取 router 实例
const router = useRouter();
// 响应式表单数据
const formData = ref({
  realname: '',
  nickname: '',
  student_card: '',
  phone_number: '',
  gender: 'Male',
  membership: 'member',
  address: '',
  campus: '江安',
});

// 提交按钮的处理逻辑
const handleSubmit = async () => {
  try {
    const payload = { ...formData.value }; // 提交前的表单数据
    console.log('Sending data:', payload);
    // router.push('/member/detail');
    // 发送 POST 请求
    const response = await axios.post(
      'http://localhost:5000/staff/add/member',
      payload,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    console.log('Response:', response.data);
    // 请求成功后的处理逻辑
    if (response.data.code === 200) {
      alert('Member added successfully!');
      const memberStore = useMemberStore();
      memberStore.setMemberInfo(response.data.data.member_id); // 保存 member_id，便于member detail页面的获取信息
      router.push('/member/detail');
    }
    else {
      alert('Failed to add member.');
    }
  } catch (error) {
    // 请求失败的处理逻辑
    console.error('Error while adding member:', error);
    alert('Failed to add member.');
  }
};
const search_opt = ref({
  type: 0,
  value: '',
});
const goToMemberAdd = () => {
	const memberStore = useMemberStore();
  search_opt.value = memberStore.$state.memberAdd; // 保存搜索信息，便于member add页面的获取信息
  if (search_opt.value.type === 0) {
    formData.value.student_card = search_opt.value.value;
  }
  else if (search_opt.value.type === 1) {
    formData.value.nickname = search_opt.value.value;
  }
  else if (search_opt.value.type === 2) {
    formData.value.phone_number = search_opt.value.value;
  }
};
goToMemberAdd()
</script>