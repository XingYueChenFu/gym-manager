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
      <div class="form-group">
        <div class="input-group d-flex align-items-center">
          <div class="input-group-prepend">
              <button class="btn btn-sm btn-outline-primary dropdown-toggle me-2" type="button"
              data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              <i class="icon-search"></i>
              <span class="p-1">{{ selectedOpt }}</span>
            </button>
              <div class="dropdown-menu">
                <a class="dropdown-item" href="#" @click.prevent="selectOpt(0)">student card</a>
                <a class="dropdown-item" href="#" @click.prevent="selectOpt(1)">nickname</a>
                <a class="dropdown-item" href="#" @click.prevent="selectOpt(2)">phone number</a>
              </div>
          </div>
          <input type="text" v-model="inputValue" @keyup.enter="handleEnter" class="form-control form-control-sm"
            aria-label="Text input with dropdown button" placeholder="Search now">
        </div>
      </div>

      <div class="col-lg-12 grid-margin stretch-card">
        <div class="card">
          <div class="card-body">

            <h4 class="card-title">Member List</h4>
            <p class="card-description"> Add class <code>.table-striped</code>
            </p>
            <div class="table-responsive">
              <table class="table table-striped">
                <thead>
					<tr>
						<th> Member </th>
						<th> name </th>
						<th> ID </th>
						<th> phone number </th>
						<!-- <th> Status </th> -->
					</tr>
                </thead>
                <tbody>
                  <!-- 批量生成列表 -->
                  <tr v-for="(item, index) in items" :key="index"  @click="goToMemberDetail(item.member_id)">
                      <td> {{ item.member_id }} </td>
                      <td> {{ item.nickname }} </td>
                      <td> {{ item.student_card }} </td>
                      <td> {{ item.phone_number }} </td>
                      <!-- <td><label class="badge badge-warning">{{ item.state }}</label></td> --> <!-- 状态信息 -->
                  </tr>
                </tbody>
              </table>
            </div>
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
// 定义查询选项
const Opt: string[] = ['student card', 'nickname', 'phone number'];
let optIndex = 0;

// 定义当前选中的日期文本
const selectedOpt = ref(Opt[optIndex]); // ref('IDcard');

// 处理日期切换的函数
const selectOpt = (opt: number) => {
  if (opt >= 0 && opt < Opt.length) {
      optIndex = opt;
      // 确保 opt 在有效范围内，并更新按钮显示的日期
      selectedOpt.value = Opt[opt];
      console.log(optIndex, Opt[opt]);
    } else {
      console.error('Invalid option index:', opt);
    }
};

// 定义表格项的接口
interface Item {
  member_id: string;
  nickname: string;
  student_card: number;
  phone_number: number;
  // state: string,
}

// 定义响应式数据存储表格项
const items = ref<Item[]>([]);

// 响应式数据
const inputValue = ref(''); // 绑定输入框的内容
interface SearchArgs {
  page: number;
  per_page: number;
  student_card?: string;
  nickname?: string;
  phone_number?: string;
}
// 处理回车事件并发送请求
const handleEnter = async () => {
  if (!inputValue.value.trim()) {
    console.log('输入内容不能为空！');
    return;
  }
  try {
    // 发送请求
    const searchArgs: SearchArgs = {
      page: 1,
      per_page: 10,
    };
    if (optIndex === 0) {
      searchArgs.student_card = inputValue.value;
    } else if (optIndex === 1) {
      searchArgs.nickname = inputValue.value;
    } else if (optIndex === 2) {
      searchArgs.phone_number = inputValue.value;
    }
    console.log('发送查询请求……');
    const response = await axios.post(
      'http://localhost:5000/staff/query/members',
      searchArgs,
      {
        headers: {
          'Content-Type': 'application/json',
        },
      }
	  );
	  if (response.data.code === 200) {
		  console.log('查询成功……');
		  // 更新响应信息
		  items.value = response.data.data.items; // 将返回数据赋值给 items
		  console.log('查询结果:', response.data);
		  console.log('查询结果更新！');
	  }
  } catch (error) {
    console.error('请求失败:', error);
  }
};

const goToMemberDetail = (memberId: string) => {
    const memberStore = useMemberStore();
    memberStore.setMemberInfo(memberId); // 保存 member_id，便于member detail页面的获取信息
    router.push('/member/detail');
};
</script>