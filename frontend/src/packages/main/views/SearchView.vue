<template>
  <main class="main">
    <section class="slice slice-sm"></section>
    <section class="spotlight parallax bg-cover bg-size--cover" data-spotlight="fullscreen"
      style="background-image: url('../assets/images/backgrounds/img-1.png')">
      <div class="container d-flex align-items-center no-padding">
        <div class="row justify-content-center">
          <!-- 搜索栏 -->
          <div class="form-group col-md-8">
            <!-- <div class="input-group"> -->
            <div class="input-group">
              <div class="input-group-prepend">
                <select class="selectpicker">
                  <option>ID</option>
                  <option>name</option>
                </select>
              </div>
              <input type="text" class="form-control">
              <div class="input-group-append">
                <span class="input-group-text"><i class="fas fa-search"></i></span>
              </div>
            </div>
          </div>
          <!-- 结果显示 -->
          <div class="col-md-8">
            <table class="table table-hover align-items-center col-md-8">
              <thead>
                <tr>
                  <th scope="col">
                    <div class="custom-control custom-checkbox">
                      <input type="checkbox" class="custom-control-input" id="th_checkbox">
                      <label class="custom-control-label" for="th_checkbox"></label>
                    </div>
                  </th>
                  <th scope="col">Name</th>
                  <th scope="col">Phone</th>
                  <th scope="col">Student Card</th>
                  <th scope="col">Admission</th>
                </tr>
              </thead>
              <tbody>
                <tr class="bg-white" scope="row">
                  <td>
                    <div class="custom-control custom-checkbox">
                      <input type="checkbox" class="custom-control-input" id="td_checkbox_1">
                      <label class="custom-control-label" for="td_checkbox_1"></label>
                    </div>
                  </td>
                  <td>
                    <div class="media align-items-center">
                      <img src="#" class="avatar avatar-lg mr-3">
                      <div class="media-body">
                        <h6 class="h5 font-weight-normal mb-0">Nabiha Armstrong</h6>
                        <span class="font-weight-normal text-muted">Web Developer</span>
                      </div>
                    </div>
                  </td>
                  <td>nabiha.armstrong@example.com</td>
                  <td>Cluj Napoca, RO</td>
                </tr>
                <tr class="bg-white" scope="row">
                  <td>
                    <div class="custom-control custom-checkbox">
                      <input type="checkbox" class="custom-control-input" id="td_checkbox_2">
                      <label class="custom-control-label" for="td_checkbox_2"></label>
                    </div>
                  </td>
                  <td>
                    <div class="media align-items-center">
                      <img src="#" class="avatar avatar-lg mr-3">
                      <div class="media-body">
                        <h6 class="h5 font-weight-normal mb-0">Dan Holding</h6>
                        <span class="font-weight-normal text-muted">Product Designer</span>
                      </div>
                    </div>
                  </td>
                  <td>dan.holding@example.com</td>
                  <td>New York, USA</td>
                </tr>
                <tr class="bg-white" scope="row">
                  <td>
                    <div class="custom-control custom-checkbox">
                      <input type="checkbox" class="custom-control-input" id="td_checkbox_1">
                      <label class="custom-control-label" for="td_checkbox_1"></label>
                    </div>
                  </td>
                  <td>
                    <div class="media align-items-center">
                      <span class="avatar avatar-lg bg-blue mr-3">WS</span>
                      <div class="media-body">
                        <h6 class="h5 font-weight-normal mb-0">Will Smith</h6>
                        <span class="font-weight-normal text-muted">Sales Manager</span>
                      </div>
                    </div>
                  </td>
                  <td>will.smith@example.com</td>
                  <td>Los Angeles, USA</td>
                </tr>
                <tr class="bg-white" scope="row">
                  <td>
                    <div class="custom-control custom-checkbox">
                      <input type="checkbox" class="custom-control-input" id="td_checkbox_1">
                      <label class="custom-control-label" for="td_checkbox_1"></label>
                    </div>
                  </td>
                  <td>
                    <div class="media align-items-center">
                      <span class="avatar avatar-lg bg-pink mr-3">CT</span>
                      <div class="media-body">
                        <h6 class="h5 font-weight-normal mb-0">Charlize Theron</h6>
                        <span class="font-weight-normal text-muted">UI/UX Designer</span>
                      </div>
                    </div>
                  </td>
                  <td>charlize.theron@example.com</td>
                  <td>Bucharest, RO</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>
    <section class="slice slice-xl"></section>
    <section class="spotlight parallax bg-cover bg-size--cover" data-spotlight="fullscreen"
      style="background-image: url('../assets/images/backgrounds/img-3.jpg')">
      <span class="mask bg-tertiary alpha-7"></span>
    </section>
  </main>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>
