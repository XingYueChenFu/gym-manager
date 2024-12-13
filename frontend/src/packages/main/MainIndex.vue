<script setup lang="ts">
import { RouterView } from 'vue-router'
// import { RouterLink, RouterView } from 'vue-router'
// import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <nav>
      <RouterLink to="/">Home </RouterLink>
      <RouterLink to="/main">dashboard </RouterLink>
      <RouterLink to="/main/search">search </RouterLink>
    </nav>
  </header>
  <!-- <div class="container-fluid page-body-wrapper">
    <nav class="sidebar"></nav>
    <nav class="sidebar sidebar-offcanvas" id="sidebar" style="position: fixed !important;">
      <ul class="nav">
        <li class="nav-item">
          <a class="nav-link" href="./main">
            <i class="icon-grid menu-icon"></i>
            <span class="menu-title">Dashboard</span>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="./main">
            <i class="icon-grid menu-icon"></i>
            <span class="menu-title">Dashboard</span>
          </a>
        </li>
        <li class="nav-item">
          <button class="nav-link" @click="currentComponent = 'dashboard'">
            <i class="icon-grid menu-icon"></i>
            <span class="menu-title">Dashboard b</span>
          </button>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/main/search">
            <i class="icon-paper menu-icon"></i>
            <span class="menu-title">Documentation</span>
          </a>
          <button class="nav-link" @click="currentComponent = 'search'">
            <i class="icon-paper menu-icon"></i>
            <span class="menu-title">Documentation b</span>
          </button>
        </li>
      </ul>
    </nav> -->

  <!-- partial -->
  <!-- <div class="main-panel"> -->
  <RouterView />
  <!-- content-wrapper ends -->
  <!-- partial:../../partials/_footer.html -->
  <!-- partial -->
  <!-- </div> -->
  <!-- main-panel ends -->
  <!-- </div> -->

</template>
