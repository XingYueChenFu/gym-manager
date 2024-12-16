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
      <div class="card">
        <div class="card-body">
          <div class="row">
              <h4 class="col-4 card-title">Member Information</h4>
              <div class="col-8">
                <div class="justify-content-end d-flex">
                  <button class="btn btn-light" @click="handleCancel">Cancel</button>
                  <span style="width: 2vh;"></span>
                  <button type="button" class="btn btn-primary" @click="handleSave">Save</button>
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
                      <input type="text" class="form-control" v-model="formData.realname" @input="handleInputChange" />
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
                    <label class="col-sm-3 col-form-label"> Student Card</label>
                    <div class="col-sm-9">
                      <div class="form-control" style="border: none !important;">{{ formData.student_card }}</div>
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
                      <div class="form-control" style="border: none !important;">{{ formData.gender }}</div>
                    </div>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="form-group row">
                    <label class="col-sm-3 col-form-label">Membership</label>
                    <div class="col-sm-9">
                      <div class="form-control" style="border: none !important;">{{ formData.membership }}</div>
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
// 表单数据
const formData = ref({
  realname: "Zhang San",
  nickname: "fake name",
  student_card: "007",
  phone_number: "10086",
  gender: "male",
  membership: "member",
  campus: "江安",
  address: "江安西园XX舍XX单元XX室",
});

const formDataCopy = ref({
  realname: "Zhang San",
  nickname: "fake name",
  student_card: "007",
  phone_number: "10086",
  gender: "male",
  membership: "member",
  campus: "江安",
  address: "江安西园XX舍XX单元XX室",
});

// 初始化标志位，表示表单是否被修改
let isFormModified = ref(false);

// 获取用户信息的函数
const fetchMemberInfo = async () => {
  isFormModified = ref(false);
  try {
    if (memberId === '') {
      console.log("memberId is empty");
      alert("请先搜索！");
      router.push('/search');
      return;
    }

    // 发送请求
    const response = await axios.post(
      `http://localhost:5000/staff/query/member/${memberId}`,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      });
    // 响应处理
    console.log(response.data.data);
    if (response.data.code === 200) {
      if (response.data.data.gender === 'F') response.data.data.gender = 'female';
      else response.data.data.gender = 'male';
      Object.assign(formData.value, response.data.data);
      Object.assign(formDataCopy.value, response.data.data);
      console.log("用户信息已填充！");
    } else {
      alert("不存在该会员！");
    }
  } catch (error) {
    console.error("获取用户信息失败:", error);
    alert("获取用户信息失败，请稍后再试！");
  }
};
fetchMemberInfo();

// 监听输入框的变化，检测用户是否修改了表单
const handleInputChange = () => {
  isFormModified.value = true;
};

// 拒绝：回溯表单时重置标志位
const handleCancel = () => {
  console.log('Form Cancel:', formData.value);
  isFormModified.value = false;  // 提交后重置为未修改状态
  Object.assign(formData.value, formDataCopy.value);
};

// 保存：提交表单时重置标志位
const handleSave = async () => {
  console.log('Form submitted:', formData.value);
  try {
    const response = await axios.post(
      `http://localhost:5000/staff/modify/member/${memberId}`,
        formData.value,
        {
          headers: {
            'Content-Type': 'application/json',
          },
      });
    if (response.data.code === 200) {
      alert("修改成功！");
      isFormModified.value = false;  // 提交后重置为未修改状态
      Object.assign(formDataCopy.value, formData.value);
    } else {
      alert("修改失败！");
    }
  } catch (error) {
    // 请求失败的处理逻辑
    console.error('Error while saving:', error);
    alert('Failed to Save.');
  }
};
</script>
