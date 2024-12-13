<template>
  <!-- <div class="about"> -->
  <div class="d-flex" style="background-image: url('./public/assets/images/backgrounds/man-5886574_1920.jpg');
    position: absolute; top: 0; left: 0; width: 100%; height: 100%;">
    <span class="mask alpha-6 bg-dark"></span>
    <div class="container d-flex align-items-center justify-content-center no-padding">
      <div class="col">
        <div class="row justify-content-center">
          <div class="col-lg-4">
            <div class="card bg-darkblue text-white">
              <div class="card-body">
                <!-- <button type="button" class="btn btn-primary btn-nobg btn-zoom--hover mb-5">
                      <span class="btn-inner--icon"><i class="fas fa-arrow-left"></i></span>
                    </button>
                    <span class="clearfix"></span> -->
                <ul class="navbar-nav ml-auto align-items-lg-end">
                  <i class="fa-solid fa-dumbbell fa-4x"></i>
                </ul>
                <h4 class="heading h3 text-white pb-4">Welcome back,<br> login to your account.</h4>

                <form @submit.prevent="handleSubmit" class="form-primary">
                  <div class="form-group">
                    <input type="text" v-model="username" class="form-control bg-dark" id="input_Username"
                      placeholder="Username" />
                  </div>
                  <div class="form-group">
                    <input type="password" v-model="password" class="form-control bg-dark" id="input_password"
                      placeholder="Password" />
                  </div>
                  <button type="submit" class="btn btn-block btn-lg bg-white mt-4 ab" style="opacity: 1"
                    :disabled="loading"> {{ loading ? '正在登录...' : '登录' }}</button>
                  <div class="text-white" :style="{ visibility: showTooltip ? 'visible' : 'hidden' }"> {{ errorMessage
                    }} </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- </div> -->
</template>

<script lang="ts" setup>
import { ref } from 'vue'; // 引入 Vue 3 组合式 API 中的 ref
import axios from 'axios'; // 你也可以使用 fetch，但这里使用 axios 举例
// import { useRouter } from 'vue-router'; // 引入 useRouter

// 定义响应式数据
const username = ref('');
const password = ref('');
const errorMessage = ref('123');
const loading = ref(false); // 定义登录状态
const showTooltip = ref(false); // 定义是否显示提示信息
// const router = useRouter(); // 获取 router 实例
// 处理表单提交

// sleep函数
function sleep(ms: number): Promise<void> {
  console.log(ms);
  return new Promise(resolve => setTimeout(resolve, ms));
}

const handleSubmit = async () => {
  // 清空错误信息
  errorMessage.value = '123';
  showTooltip.value = false;
  // 输入验证
  if (!username.value || !password.value) {
    showTooltip.value = true;
    errorMessage.value = '用户名或密码不能为空！';
    return;
  }
  await sleep(500);
  // 设置 loading 状态为 true
  loading.value = true;
  // window.location.href = '/main'; // 测试用：跳转到管理系统页
  try {
    // 模拟发送登录请求
    // console.log(username.value, password.value);
    const response = await axios.post(
      'http://localhost:5000/staff/login',
      {
        username: username.value,
        password: password.value,
      },
      {
        headers: {
          'Content-Type': 'application/json', // 显式设置请求头
        },
      }
    );

    console.log('登陆中', username.value, password.value);
    // 根据返回的数据处理登录成功
    if (response.data.code === 200) {
      // 处理成功的逻辑，例如跳转页面、存储 token 等
      window.location.href = '/main'; // 跳转到管理系统页 router.push({ name: 'main' });
    } else {
      console.log(username.value, password.value, '用户名或密码错误！');
      errorMessage.value = '用户名或密码错误！';
      showTooltip.value = true;
    }
  } catch (error) {
    // 捕获请求失败的错误
    console.error('登录请求失败:', error);
    errorMessage.value = '登录失败，请稍后再试！';
    showTooltip.value = true;
  } finally {
    // 请求完成后，重置 loading 状态
    loading.value = false;
    // showTooltip.value = false;
  }
};
</script>
