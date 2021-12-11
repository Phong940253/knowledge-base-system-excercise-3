<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <meta http-equiv="X-UA-Compatible" content="ie=edge" />

    <meta name="description" content="Mobile Application HTML5 Template" />

    <meta name="copyright" content="MACode ID, https://www.macodeid.com/" />

    <title>Final project</title>

    <link rel="stylesheet" href="../assets/css/maicons.css" />

    <link rel="stylesheet" href="../assets/vendor/animate/animate.css" />

    <link
      rel="stylesheet"
      href="../assets/vendor/owl-carousel/css/owl.carousel.min.css"
    />

    <link rel="stylesheet" href="../assets/css/bootstrap.css" />

    <link rel="stylesheet" href="../assets/css/mobster.css" />
  </head>
  <body>
    <main>
      <div
        class="page-hero-section bg-image hero-mini"
        style="background-image: url(../assets/img/hero_mini.svg)"
      >
        <div class="hero-caption">
          <div class="container fg-white h-100">
            <div
              class="
                row
                justify-content-center
                align-items-center
                text-center
                h-100
              "
            >
              <div class="col-lg-6">
                <h3 class="mb-4 fw-medium">Đồ án cuối kỳ</h3>
                <p>
                  Xây dựng chương trình chuyển đề bài toán hình học phẳng theo
                  ngôn ngữ tự nhiên sang ngôn ngữ đặc tả.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="page-section">
        <div class="container">
          <div class="row">
            <div class="col-lg-8 py-3">
              <form class="blog-entry">
                <div class="post-title">
                  <p>Nhập bài toán</p>
                </div>
                <div class="entry-header">
                  <textarea
                    wrap="hard"
                    style="resize: none"
                    cols="60"
                    rows="15"
                    name="bai_toan"
                  ><?php
                  if(isset($_GET['bai_toan'])){
                    $bai_toan = $_GET['bai_toan'];
                    $output=null;
                    $retval=null;
                    $result = shell_exec('python ../../Specification-Language/model.py "' . $bai_toan . '"');
                    // echo "Returned with status $retval and output:\n";
                    // foreach ($output as $line) {
                    //   echo $line;
                    // }
                    echo $result;
                  }       
                  ?></textarea>
                </div>
                <button class="btn btn-primary">OK</button>
              </form>
            </div>
            <!-- Sidebar -->
            <div class="col-lg-4 py-3">
              <div class="widget-wrap">
                <h3 class="widget-title">Những bài toán mẫu (Bàn luận sau)</h3>
                <ul class="categories">
                  <li>
                    <a href="#"
                      >Cho tam giác ABC, vuông tại A, cạnh BC bằng 5cm, AC bằng 3cm. Tính diện tích tam giác ABC.</a
                    >
                  </li>
                  <li>
                    <a href="#"
                      >Đường tròn ngoại tiếp và đường tròn nội tiếp tam giác ABC có bán kính lần lượt là R và r. Biết rằng BAC - ACB = ABC - BAC. Tính diện tích tam giác ABC theo R và r.</a
                    >
                  </li>
                  <li>
                    <a href="#"
                      >Cho tam giác ABC nhọn có AB > AC nội tiếp đường tròn (O). Gọi H là trực tâm của tam giác và AH vuông góc với BC tại F. Gọi M là trung điểm của BC. Trên đường tròn (O) lấy các điểm Q và K sao cho HQA = HKQ = 90° (Các điểm A, B, C, K, Q theo thứ tự đó trên đường tròn). Chứng minh rằng đường tròn ngoại tiếp tam giác KHQ tiếp xúc với đường tròn ngoại tiếp tam giác MFK.</a
                    >
                  </li>
                  <li>
                    <a href="#"
                      >Cho tam giác ABC có ba đường cao AD, BE, CF. Gọi G, P lần lượt là hình chiếu của D trên AB và AC. Gọi I, K lần lượt là hình chiếu của E trên AB và BC. Gọi M, N lần lượt là hình chiếu của F trên AC và BC. Chứng minh rằng sáu điểm G, P, I, K, M, N cùng nằm trên một đường tròn.</a
                    >
                  </li>
                  <li>
                    <a href="#"
                      >Cho tam giác ABC có BAC = 30°. Đường phân giác trong và phân giác ngoài của góc ABC cắt cạnh AC lần lượt tại B1, B2. Đường phân giác trong và phân giác ngoài của góc ACB cắt cạnh AB lần lượt tại C1, C2. Đường tròn ngoại tiếp tam giác BB1B2 cắt đường tròn ngoại tiếp tam giác CC1C2 tại điểm P ở trong tam giác ABC. Gọi O là trung điểm B1B2. Chứng minh rằng CP vuông góc với BP.</a
                    >
                  </li>
                </ul>
              </div>
            </div>
            <!-- end sidebar -->
          </div>
        </div>
      </div>
    </main>

    <footer class="page-footer-section bg-dark fg-white">
      <div class="container">
        <div class="row mb-5 py-3">
          <div class="col-sm-6 col-lg-2 py-3">
            <h5 class="mb-3">Team</h5>
            <ul class="menu-link">
              <li>
                <a href="#" class="">Lê Tấn Lộc 4501104135</a>
              </li>
              <li><a href="#" class="">Nguyễn Văn Phong 4501104175</a></li>
              <li><a href="#" class="">Huỳnh Thanh Phong 4501104172</a></li>
              <li><a href="#" class="">Lê Văn Trung 4501104259</a></li>
            </ul>
          </div>
        </div>
      </div>

      <hr />

      <div class="container">
        <div class="row">
          <div class="col-12 col-md-6 py-2">
            <ul class="nav justify-content-end">
              <li class="nav-item">
                <a href="#" class="nav-link">Terms of Use</a>
              </li>
              <li class="nav-item">
                <a href="#" class="nav-link">Privacy Policy</a>
              </li>
              <li class="nav-item">
                <a href="#" class="nav-link">Cookie Policy</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </footer>
    <!-- .page-footer -->
    <script src="../assets/js/jquery-3.5.1.min.js"></script>

    <script src="../assets/js/bootstrap.bundle.min.js"></script>

    <script src="../assets/vendor/owl-carousel/js/owl.carousel.min.js"></script>

    <script src="../assets/vendor/wow/wow.min.js"></script>

    <script src="../assets/js/mobster.js"></script>
  </body>
</html>