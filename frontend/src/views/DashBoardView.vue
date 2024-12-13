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
				<!-- 大图卡片 -->
				<!-- <div class="col-md-6 grid-margin stretch-card">
			<div class="card tale-bg">
				<div class="card-people mt-auto">
					<img src="../../public/assets_skydash/images/dashboard/people.svg" alt="people">
					<div class="weather-info">
						<div class="d-flex">
							<div>
								<h2 class="mb-0 font-weight-normal"><i class="icon-sun me-2"></i>6<sup>C</sup></h2>
							</div>
							<div class="ms-2">
								<h4 class="location font-weight-normal">成都</h4>
								<h6 class="font-weight-normal">江安</h6>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div> -->
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
											<p class="mb-4">Today's Register</p>
											<div class="d-flex align-items-center justify-content-center">
												<i class="bi bi-people-fill fa-5x"></i>
												<span style="width: 15px;"></span>
												<p class="mr-3 pl-2 pt-3" style="font-size: 50px;">1344</p>
											</div>
										</div>
									</div>
								</div>
							</div>
							<!-- <div class="card card-tale">
						<div class="card-body d-flex flex-column justify-content-between">
							<div class="row">
								<div class="col-8">
									<p class="mb-4">Guests Traffic</p>
									<p class="mb-2" style="font-size: 40px;">4006</p>
								</div>
								<div class="col d-flex justify-content-end align-items-end" style="min-height: 150px;">
									<i class="bi bi-people-fill fa-3x ml-auto float-right"></i>
								</div>
							</div>
						</div>
					</div> -->
						</div>
						<div class="col-md-6 mb-4 stretch-card transparent">
							<div class="card card-dark-blue">
								<div class="card-body">
									<div class="row">
										<div class="col">
											<p class="mb-4">New Users</p>
											<div class="d-flex align-items-center justify-content-center">
												<i class="bi bi-person-fill-add fa-5x"></i>
												<span style="width: 15px;"></span>
												<p class="mr-3 pl-2 pt-3" style="font-size: 50px;">44</p>
											</div>
										</div>
									</div>
								</div>
							</div>
							<!-- <div class="card card-dark-blue">
						<div class="card-body d-flex flex-column justify-content-between">
							<div class="row">
								<div class="col-8">
									<p class="mb-4">New Users</p>
									<p class="fs-30 mb-2">61344</p>
									<p>22.00% (30 days)</p>
								</div>
								<div class="col d-flex justify-content-end align-items-end" style="min-height: 150px;">
									<i class="bi bi-person-fill-add fa-3x"></i>
								</div>
							</div>
						</div>
					</div> -->
						</div>
					</div>
					<div class="row">
						<div class="col-md-6 mb-4 mb-lg-0 stretch-card transparent">
							<div class="card card-light-blue">
								<div class="card-body">
									<div class="row">
										<div class="col">
											<p class="mb-4">Today's Register</p>
											<div class="d-flex align-items-center justify-content-center">
												<i class="bi bi-currency-yen fa-5x"></i>
												<p class="mr-3 pl-2 pt-3" style="font-size: 50px;">61344</p>
											</div>
										</div>
										<!-- <div class="col-8">
									<p class="mb-4">Today's Recharge Amount</p>
									<p class="fs-30 mb-2">34040</p>
									<p>2.00% (30 days)</p>
								</div>
								<div class="col d-flex justify-content-end align-items-end" style="min-height: 150px;">
									<i class="bi bi-currency-yen fa-3x"></i>
								</div> -->
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
												<h2 class="mb-0 font-weight-normal"><i
														class="icon-sun me-2"></i>6<sup>C</sup>
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
					<!-- 另一个样式的数据卡片 -->
					<!-- <div class="row">
				<div class="mb-4 mb-lg-0 stretch-card transparent">
					<div class="col-md-6 mb-4 mb-lg-0 stretch-card transparent">
					<div class="card card-light-blue">
						<div class="card-body">
							<div class="row">


								<div class="col">
									<p class="mb-4">Today's Recharge Amount</p>

									<p>2.00% (30 days)</p>
								</div>
								<div class="col d-flex justify-content-end align-items-end">
									<i class="bi bi-currency-yen fa-3x"></i>
									<p class="fs-30 mb-2">34040</p>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div> -->
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
			<!-- 轮播图 -->
			<!-- <div class="row">
		<div class="col-md-12 grid-margin stretch-card">
			<div class="card position-relative">
				<div class="card-body">
					<div id="detailedReports" class="carousel slide detailed-report-carousel position-static pt-2"
						data-bs-ride="carousel">
						<div class="carousel-inner">
							<div class="carousel-item active">
								<div class="row">
									<div class="col-md-12 col-xl-3 d-flex flex-column justify-content-start">
										<div class="ml-xl-4 mt-3">
											<p class="card-title">Detailed Reports</p>
											<h1 class="text-primary">$34040</h1>
											<h3 class="font-weight-500 mb-xl-4 text-primary">North America</h3>
											<p class="mb-2 mb-xl-0">The total number of sessions within the date
												range.
												It is the
												period time a user is actively engaged with your website, page or
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
																	<div class="progress-bar bg-info" role="progressbar"
																		style="width: 60%" aria-valuenow="60"
																		aria-valuemin="0" aria-valuemax="100"></div>
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
													<canvas id="north-america-chart"></canvas>
												</div>
												<div id="north-america-chart-legend">
												</div>
											</div>
										</div>
									</div>
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
												period time a user is actively engaged with your website, page or
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
																	<div class="progress-bar bg-info" role="progressbar"
																		style="width: 60%" aria-valuenow="60"
																		aria-valuemin="0" aria-valuemax="100"></div>
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
						<a class="carousel-control-prev" href="#detailedReports" role="button" data-bs-slide="prev">
							<span class="carousel-control-prev-icon" aria-hidden="true"></span>
						</a>
						<a class="carousel-control-next" href="#detailedReports" role="button" data-bs-slide="next">
							<span class="carousel-control-next-icon" aria-hidden="true"></span>
						</a>
					</div>
				</div>
			</div>
		</div>
	</div> -->
			<div class="row">
				<div class="col-md-7 grid-margin stretch-card">
					<div class="card">
						<div class="card-body">
							<p class="card-title mb-0">Top Products</p>
							<div class="table-responsive">
								<table class="table table-striped table-borderless">
									<thead>
										<tr>
											<th>Product</th>
											<th>Price</th>
											<th>Date</th>
											<th>Status</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>Search Engine Marketing</td>
											<td class="font-weight-bold">$362</td>
											<td>21 Sep 2018</td>
											<td class="font-weight-medium">
												<div class="badge badge-success">Completed</div>
											</td>
										</tr>
										<tr>
											<td>Search Engine Optimization</td>
											<td class="font-weight-bold">$116</td>
											<td>13 Jun 2018</td>
											<td class="font-weight-medium">
												<div class="badge badge-success">Completed</div>
											</td>
										</tr>
										<tr>
											<td>Display Advertising</td>
											<td class="font-weight-bold">$551</td>
											<td>28 Sep 2018</td>
											<td class="font-weight-medium">
												<div class="badge badge-warning">Pending</div>
											</td>
										</tr>
										<tr>
											<td>Pay Per Click Advertising</td>
											<td class="font-weight-bold">$523</td>
											<td>30 Jun 2018</td>
											<td class="font-weight-medium">
												<div class="badge badge-warning">Pending</div>
											</td>
										</tr>
										<tr>
											<td>E-Mail Marketing</td>
											<td class="font-weight-bold">$781</td>
											<td>01 Nov 2018</td>
											<td class="font-weight-medium">
												<div class="badge badge-danger">Cancelled</div>
											</td>
										</tr>
										<tr>
											<td>Referral Marketing</td>
											<td class="font-weight-bold">$283</td>
											<td>20 Mar 2018</td>
											<td class="font-weight-medium">
												<div class="badge badge-warning">Pending</div>
											</td>
										</tr>
										<tr>
											<td>Social media marketing</td>
											<td class="font-weight-bold">$897</td>
											<td>26 Oct 2018</td>
											<td class="font-weight-medium">
												<div class="badge badge-success">Completed</div>
											</td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
					</div>
				</div>
				<div class="col-md-5 grid-margin stretch-card">
					<div class="card">
						<div class="card-body">
							<h4 class="card-title">To Do Lists</h4>
							<div class="list-wrapper pt-2">
								<ul class="d-flex flex-column-reverse todo-list todo-list-custom">
									<li>
										<div class="form-check form-check-flat">
											<label class="form-check-label">
												<input class="checkbox" type="checkbox"> Meeting with Urban Team
											</label>
										</div>
										<i class="remove ti-close"></i>
									</li>
									<li class="completed">
										<div class="form-check form-check-flat">
											<label class="form-check-label">
												<input class="checkbox" type="checkbox" checked> Duplicate a project for
												new
												customer
											</label>
										</div>
										<i class="remove ti-close"></i>
									</li>
									<li>
										<div class="form-check form-check-flat">
											<label class="form-check-label">
												<input class="checkbox" type="checkbox"> Project meeting with CEO
											</label>
										</div>
										<i class="remove ti-close"></i>
									</li>
									<li class="completed">
										<div class="form-check form-check-flat">
											<label class="form-check-label">
												<input class="checkbox" type="checkbox" checked> Follow up of team zilla
											</label>
										</div>
										<i class="remove ti-close"></i>
									</li>
									<li>
										<div class="form-check form-check-flat">
											<label class="form-check-label">
												<input class="checkbox" type="checkbox"> Level up for Antony </label>
										</div>
										<i class="remove ti-close"></i>
									</li>
								</ul>
							</div>
							<div class="add-items d-flex mb-0 mt-2">
								<input type="text" class="form-control todo-list-input" placeholder="Add new task">
								<button class="add btn btn-icon text-primary todo-list-add-btn bg-transparent"><i
										class="icon-circle-plus"></i></button>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="col-md-4 stretch-card grid-margin">
					<div class="card">
						<div class="card-body">
							<p class="card-title mb-0">Projects</p>
							<div class="table-responsive">
								<table class="table table-borderless">
									<thead>
										<tr>
											<th class="ps-0  pb-2 border-bottom">Places</th>
											<th class="border-bottom pb-2">Orders</th>
											<th class="border-bottom pb-2">Users</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td class="ps-0">Kentucky</td>
											<td>
												<p class="mb-0"><span class="font-weight-bold me-2">65</span>(2.15%)</p>
											</td>
											<td class="text-muted">65</td>
										</tr>
										<tr>
											<td class="ps-0">Ohio</td>
											<td>
												<p class="mb-0"><span class="font-weight-bold me-2">54</span>(3.25%)</p>
											</td>
											<td class="text-muted">51</td>
										</tr>
										<tr>
											<td class="ps-0">Nevada</td>
											<td>
												<p class="mb-0"><span class="font-weight-bold me-2">22</span>(2.22%)</p>
											</td>
											<td class="text-muted">32</td>
										</tr>
										<tr>
											<td class="ps-0">North Carolina</td>
											<td>
												<p class="mb-0"><span class="font-weight-bold me-2">46</span>(3.27%)</p>
											</td>
											<td class="text-muted">15</td>
										</tr>
										<tr>
											<td class="ps-0">Montana</td>
											<td>
												<p class="mb-0"><span class="font-weight-bold me-2">17</span>(1.25%)</p>
											</td>
											<td class="text-muted">25</td>
										</tr>
										<tr>
											<td class="ps-0">Nevada</td>
											<td>
												<p class="mb-0"><span class="font-weight-bold me-2">52</span>(3.11%)</p>
											</td>
											<td class="text-muted">71</td>
										</tr>
										<tr>
											<td class="ps-0 pb-0">Louisiana</td>
											<td class="pb-0">
												<p class="mb-0"><span class="font-weight-bold me-2">25</span>(1.32%)</p>
											</td>
											<td class="pb-0">14</td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
					</div>
				</div>
				<div class="col-md-4 stretch-card grid-margin">
					<div class="row">
						<div class="col-md-12 grid-margin stretch-card">
							<div class="card">
								<div class="card-body">
									<p class="card-title">Charts</p>
									<div class="charts-data">
										<div class="mt-3">
											<p class="mb-0">Data 1</p>
											<div class="d-flex justify-content-between align-items-center">
												<div class="progress progress-md flex-grow-1 me-4">
													<div class="progress-bar bg-inf0" role="progressbar"
														style="width: 95%" aria-valuenow="95" aria-valuemin="0"
														aria-valuemax="100"></div>
												</div>
												<p class="mb-0">5k</p>
											</div>
										</div>
										<div class="mt-3">
											<p class="mb-0">Data 2</p>
											<div class="d-flex justify-content-between align-items-center">
												<div class="progress progress-md flex-grow-1 me-4">
													<div class="progress-bar bg-info" role="progressbar"
														style="width: 35%" aria-valuenow="35" aria-valuemin="0"
														aria-valuemax="100"></div>
												</div>
												<p class="mb-0">1k</p>
											</div>
										</div>
										<div class="mt-3">
											<p class="mb-0">Data 3</p>
											<div class="d-flex justify-content-between align-items-center">
												<div class="progress progress-md flex-grow-1 me-4">
													<div class="progress-bar bg-info" role="progressbar"
														style="width: 48%" aria-valuenow="48" aria-valuemin="0"
														aria-valuemax="100"></div>
												</div>
												<p class="mb-0">992</p>
											</div>
										</div>
										<div class="mt-3">
											<p class="mb-0">Data 4</p>
											<div class="d-flex justify-content-between align-items-center">
												<div class="progress progress-md flex-grow-1 me-4">
													<div class="progress-bar bg-info" role="progressbar"
														style="width: 25%" aria-valuenow="25" aria-valuemin="0"
														aria-valuemax="100"></div>
												</div>
												<p class="mb-0">687</p>
											</div>
										</div>
									</div>
								</div>
							</div>
						</div>
						<div class="col-md-12 stretch-card grid-margin grid-margin-md-0">
							<div class="card data-icon-card-primary">
								<div class="card-body">
									<p class="card-title text-white">Number of Meetings</p>
									<div class="row">
										<div class="col-8 text-white">
											<h3>34040</h3>
											<p class="text-white font-weight-500 mb-0">The total number of sessions
												within
												the
												date
												range.It is calculated as the sum . </p>
										</div>
										<div class="col-4 background-icon">
										</div>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
				<div class="col-md-4 stretch-card grid-margin">
					<div class="card">
						<div class="card-body">
							<p class="card-title">Notifications</p>
							<ul class="icon-data-list">
								<li>
									<div class="d-flex">
										<img src="../../public/assets_skydash/images/faces/face1.jpg" alt="user">
										<div>
											<p class="text-info mb-1">Isabella Becker</p>
											<p class="mb-0">Sales dashboard have been created</p>
											<small>9:30 am</small>
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<img src="../../public/assets_skydash/images/faces/face2.jpg" alt="user">
										<div>
											<p class="text-info mb-1">Adam Warren</p>
											<p class="mb-0">You have done a great job #TW111</p>
											<small>10:30 am</small>
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<img src="../../public/assets_skydash/images/faces/face3.jpg" alt="user">
										<div>
											<p class="text-info mb-1">Leonard Thornton</p>
											<p class="mb-0">Sales dashboard have been created</p>
											<small>11:30 am</small>
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<img src="../../public/assets_skydash/images/faces/face4.jpg" alt="user">
										<div>
											<p class="text-info mb-1">George Morrison</p>
											<p class="mb-0">Sales dashboard have been created</p>
											<small>8:50 am</small>
										</div>
									</div>
								</li>
								<li>
									<div class="d-flex">
										<img src="../../public/assets_skydash/images/faces/face5.jpg" alt="user">
										<div>
											<p class="text-info mb-1">Ryan Cortez</p>
											<p class="mb-0">Herbs are fun and easy to grow.</p>
											<small>9:00 am</small>
										</div>
									</div>
								</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
			<div class="row">
				<div class="col-md-12 grid-margin stretch-card">
					<div class="card">
						<div class="card-body">
							<p class="card-title">Advanced Table</p>
							<div class="row">
								<div class="col-12">
									<div class="table-responsive">
										<table id="example" class="display expandable-table" style="width:100%">
											<thead>
												<tr>
													<th>Quote#</th>
													<th>Product</th>
													<th>Business type</th>
													<th>Policy holder</th>
													<th>Premium</th>
													<th>Status</th>
													<th>Updated at</th>
													<th></th>
												</tr>
											</thead>
										</table>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script lang="ts" setup>
import { ref, type Ref } from 'vue';

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

// 定义当前选中的日期文本
const selectedDate: Ref<string> = ref(today.value);

// 处理日期切换的函数
const selectDate = (opt: number) => {
    if (opt >= 0 && opt < datas.length) {
        // 确保 opt 在有效范围内，并更新按钮显示的日期
        selectedDate.value = datas[opt].value;
    } else {
        console.error('Invalid option index:', opt);
    }
};

</script>

