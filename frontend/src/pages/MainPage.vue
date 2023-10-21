<template>
  <navbar-comp />
  <div class="main-container">
    <div class="main-page">
      <div class="whatis-block white">
        <p class="brand_text">About us</p>
        <p class="fs--50 fw--700 header_text align_center_text no-top few-padding">What is FlexFi Upscale?</p>
        <div class="whatis-about">
          <h1 class="fs--25 fw--400 whatis-text-desc small_text">It's a website where you have all tools in your hand. From upscaling to removing bacgkrounds.</h1>
          <div class="whatis-block-block">
            <router-link v-if="!isAuthenticated" class="main_signup_btn" to="/signup">Start upscaling</router-link>
            <router-link v-else class="main_signup_btn" to="/pricing">Buy plan</router-link>
          </div>
        </div>
      </div>
      <div class="tools-usage-block">
        <p class="brand_text">Our tools</p>
        <p class="fs--50 fw--700 header_text no-top align_center_text few-padding">We have many tools for your usage</p>
        <div class="tools-cards-block">
          <tool-card name="Upscaling" description="
          Upscale your image resolution and quality just in one click
          "
          :before_img="Img"
          :after_img="Img2"
          />
          <tool-card name="Background remove" description="
          Remove background instantly from your photo
          "
          :before_img="Bg"
          :after_img="Bg2"
          />
          <tool-card name="Remove JPEG Artifacts" description="
          Remove JPEG artifacts from your photo and forget about them
          "
          :before_img="JPEG"
          :after_img="JPEG2"
          />
        </div>
      </div>
      <div class="why-us-block">
          <p class="brand_text">Preferences</p>
          <p class="fs--50 fw--700 header_text no-top align_center_text few-padding">Why would you choose us?</p>
          <div class="why-us-block">
            <div class="why-us-table-features">
              <div class="why-item">
                <p class="fs--33 fw--700 white">Minimalistic and simple</p>
                <p class="fs--15 fw--400 small_text">sfdsffffffffffffffffffffffffffffffffffffffffffffffff</p>
              </div>
              <div class="line-vertical-1"></div>
              <div class="why-item">
                <p class="fs--33 fw--700 white">Minimalistic and simple</p>
                <p class="fs--15 fw--400 small_text">s</p>
              </div>
            </div>
            <div class="horizontal-line"></div>
            <div class="why-us-table-features">
              <div class="why-item">
                <p class="fs--33 fw--700 white">Minimalistic and simple</p>
                <p class="fs--15 fw--400 small_text">s</p>
              </div>
              <div class="line-vertical-2"></div>
              <div class="why-item">
                <p class="fs--33 fw--700 white">Minimalistic and simple</p>
                <p class="fs--15 fw--400 small_text">s</p>
              </div>
            </div>
          </div>
      </div>
      <use-cases-block />
      <often-questions />
      <div class="get-started-main-block payment_info_block flex-block column center white gp--50">
        <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTAwIiBoZWlnaHQ9Ijk5IiB2aWV3Qm94PSIwIDAgMTAwIDk5IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8Y2lyY2xlIGN4PSI1MC4zNTc0IiBjeT0iNDkuNSIgcj0iNDkuMTUxNCIgc3Ryb2tlPSIjOTAyRUYyIiBzdHJva2Utd2lkdGg9IjAuNjk3MTgzIi8+CjxwYXRoIGQ9Ik02Ni42MjEgMjkuOTc5SDYwLjExNzRDNTkuMjUzNSAyOS45NzkgNTguNDI3MiAzMC4zMjQ4IDU3LjgxNjQgMzAuOTM1MUM1Ny4yMDU2IDMxLjU0NTQgNTYuODYyNSAzMi4zNzIzIDU2Ljg2MDQgMzMuMjM2N1YzOS43Mzk2QzU2Ljg2MDQgNDAuMTY2NiA1Ni43NzY3IDQwLjU5MTUgNTYuNjEzNiA0MC45ODUyQzU2LjQ1MDQgNDEuMzc4OCA1Ni4yMTE5IDQxLjczOTIgNTUuOTA4NiA0Mi4wNDEyQzU1LjYwNzQgNDIuMzQzMiA1NS4yNDc2IDQyLjU4MjggNTQuODUyMiA0Mi43NDczQzU0LjQ1NjkgNDIuOTExOSA1NC4wMzQzIDQyLjk5NTIgNTMuNjA3NiA0Mi45OTUySDQ3LjA5NzdDNDYuMjMzOCA0Mi45OTUyIDQ1LjQwNzUgNDIuNjQ5NCA0NC43OTg4IDQyLjAzOTFDNDQuMTkwMSA0MS40Mjg4IDQzLjg0NyA0MC41OTk4IDQzLjg0NyAzOS43Mzc1VjMzLjIzNjdDNDMuODQ3IDMyLjM3NDQgNDMuNTA0IDMxLjU0NTQgNDIuODk1MiAzMC45MzUxQzQyLjI4NjUgMzAuMzI0OCA0MS40NjAyIDI5Ljk3OSA0MC41OTYzIDI5Ljk3OUgzNC4wODY1QzMzLjIyNDYgMjkuOTc5IDMyLjM5ODMgMzAuMzI0OCAzMS43ODc1IDMwLjkzNTFDMzEuMTc4OCAzMS41NDU0IDMwLjgzNTcgMzIuMzc0NCAzMC44MzU3IDMzLjIzNjdWMzkuNzM5NkMzMC44MzU3IDQwLjE2NjYgMzAuOTE5NCA0MC41OTE1IDMxLjA4MjYgNDAuOTg1MkMzMS4yNDU3IDQxLjM4MDkgMzEuNDg0MiA0MS43MzkyIDMxLjc4NzUgNDIuMDQxMkMzMi4wODg3IDQyLjM0MzIgMzIuNDQ4NSA0Mi41ODI4IDMyLjg0MzkgNDIuNzQ3M0MzMy4yMzkzIDQyLjkxMTkgMzMuNjYxOCA0Mi45OTUyIDM0LjA4ODUgNDIuOTk1Mkg0MC41OTg0QzQxLjQ2MDIgNDIuOTk1MiA0Mi4yODg2IDQzLjMzNjggNDIuODk3MyA0My45NDcxQzQzLjUwODEgNDQuNTU3NCA0My44NDkxIDQ1LjM4NDMgNDMuODQ5MSA0Ni4yNDY2VjUyLjc1NTdDNDMuODQ5MSA1My42MTgxIDQzLjUwNiA1NC40NDUgNDIuODk3MyA1NS4wNTUzQzQyLjI4NjUgNTUuNjY1NiA0MS40NjAyIDU2LjAwNzIgNDAuNTk4NCA1Ni4wMDcySDM0LjA4NjVDMzMuMjI0NiA1Ni4wMDcyIDMyLjM5NjIgNTYuMzQ4OCAzMS43ODc1IDU2Ljk1OTFDMzEuMTc4OCA1Ny41NzE0IDMwLjgzNTcgNTguMzk4NCAzMC44MzU3IDU5LjI2MDdWNjUuNzY5OEMzMC44MzU3IDY2LjYzMjEgMzEuMTc4OCA2Ny40NTkxIDMxLjc4NzUgNjguMDY5NEMzMi4zOTgzIDY4LjY3OTcgMzMuMjI0NiA2OS4wMjEzIDM0LjA4NjUgNjkuMDIxM0g0MC41OTYzQzQxLjQ1ODEgNjkuMDIxMyA0Mi4yODY1IDY4LjY3OTcgNDIuODk1MiA2OC4wNjk0QzQzLjUwNiA2Ny40NTkxIDQzLjg0NyA2Ni42MzIxIDQzLjg0NyA2NS43Njk4VjU5LjI2MDdDNDMuODQ3IDU4LjM5ODQgNDQuMTkwMSA1Ny41NzE0IDQ0Ljc5ODggNTYuOTYxMUM0NS40MDk2IDU2LjM1MDkgNDYuMjM1OSA1Ni4wMDkzIDQ3LjA5NzcgNTYuMDA5M0g1My42MDc2QzU0LjQ2OTQgNTYuMDA5MyA1NS4yOTc4IDU2LjM1MDkgNTUuOTA2NSA1Ni45NjExQzU2LjUxNzMgNTcuNTcxNCA1Ni44NTgzIDU4LjM5ODQgNTYuODU4MyA1OS4yNjA3VjY1Ljc2OThDNTYuODU4MyA2Ni42MzIxIDU3LjIwMzUgNjcuNDU5MSA1Ny44MTQzIDY4LjA2OTRDNTguNDI1MSA2OC42Nzk3IDU5LjI1MzUgNjkuMDIxMyA2MC4xMTUzIDY5LjAyMTNINjYuNjE4OUM2Ny4wNDU2IDY5LjAyMTMgNjcuNDcwMyA2OC45Mzc5IDY3Ljg2NTYgNjguNzc1NUM2OC4yNjEgNjguNjEzIDY4LjYyMDggNjguMzczNSA2OC45MjIgNjguMDcxNEM2OS4yMjUzIDY3Ljc2OTQgNjkuNDYzOCA2Ny40MTEyIDY5LjYyOSA2Ny4wMTU0QzY5Ljc5MjIgNjYuNjIxNyA2OS44NzggNjYuMTk2OCA2OS44NzggNjUuNzY5OFY1OS4yNjA3QzY5Ljg3OCA1OC44MzM3IDY5Ljc5NDMgNTguNDEwOSA2OS42MjkgNTguMDE1MUM2OS40NjU5IDU3LjYyMTQgNjkuMjI1MyA1Ny4yNjExIDY4LjkyMiA1Ni45NTkxQzY4LjYxODcgNTYuNjU3IDY4LjI2MSA1Ni40MTc1IDY3Ljg2NTYgNTYuMjU1QzY3LjQ3MDMgNTYuMDkyNiA2Ny4wNDc3IDU2LjAwOTMgNjYuNjE4OSA1Ni4wMDkzSDYwLjExNTNDNTkuMjUxNCA1Ni4wMDkzIDU4LjQyNTEgNTUuNjY3NyA1Ny44MTQzIDU1LjA1NzRDNTcuMjAzNSA1NC40NDcxIDU2Ljg2MDQgNTMuNjIwMSA1Ni44NTgzIDUyLjc1NzhWNDYuMjQ4N0M1Ni44NTgzIDQ1LjM4NjQgNTcuMjAzNSA0NC41NTk0IDU3LjgxNDMgNDMuOTQ5MUM1OC40MjUxIDQzLjMzODkgNTkuMjUzNSA0Mi45OTczIDYwLjExNTMgNDIuOTk3M0g2Ni42MTg5QzY3LjA0NzcgNDIuOTk3MyA2Ny40NzAzIDQyLjkxMzkgNjcuODY1NiA0Mi43NTE1QzY4LjI2MSA0Mi41ODkgNjguNjIwOCA0Mi4zNDc0IDY4LjkyNDEgNDIuMDQ1NEM2OS4yMjc0IDQxLjc0MzMgNjkuNDY1OSA0MS4zODMgNjkuNjI5IDQwLjk4NzJDNjkuNzkyMiA0MC41OTE1IDY5Ljg3NTkgNDAuMTY4NiA2OS44NzU5IDM5LjczOTZWMzMuMjM2N0M2OS44NzU5IDMyLjM3MjMgNjkuNTMyOCAzMS41NDMzIDY4LjkyMiAzMC45MzNDNjguMzExMiAzMC4zMjI3IDY3LjQ4MjggMjkuOTc5IDY2LjYxODkgMjkuOTc5SDY2LjYyMVoiIGZpbGw9InVybCgjcGFpbnQwX2xpbmVhcl8xNTI5Xzc3MzMxKSIvPgo8ZGVmcz4KPGxpbmVhckdyYWRpZW50IGlkPSJwYWludDBfbGluZWFyXzE1MjlfNzczMzEiIHgxPSIyOS4wNzY1IiB5MT0iNDcuMzYzMSIgeDI9IjcxLjYzNTYiIHkyPSI1MS42NzM2IiBncmFkaWVudFVuaXRzPSJ1c2VyU3BhY2VPblVzZSI+CjxzdG9wIHN0b3AtY29sb3I9IiM5MDJFRjIiLz4KPHN0b3Agb2Zmc2V0PSIxIiBzdG9wLWNvbG9yPSIjRkY2MkI3Ii8+CjwvbGluZWFyR3JhZGllbnQ+CjwvZGVmcz4KPC9zdmc+Cg==">
        <p class="no-margin fw--900 fs--50 align_center_text">Get started</p>
        <p class="no-margin fw--400 fs--15 width--30 align_center_text">Sign up for a free attemps, you can upgrade to a plan that suits your needs</p>
        <router-link v-if="!isAuthenticated" class="main_signup_btn" to="/signup">Get started</router-link>
          <router-link v-else class="main_signup_btn" to="/pricing">Get started</router-link>
      </div>
    </div>
  </div>
  <footer-comp />
</template>

<script>
  import NavbarComp from "@/components/NavbarComp.vue";
  import OftenQuestions from "@/components/OftenQuestion.vue";
  import UseCasesBlock from "@/components/UseCasesBlock.vue";
  import ToolCard from "@/components/UI/ToolCard.vue";
  import FooterComp from "@/components/FooterComp.vue";
  import handlePopState from "@/utils/index.js";
  import { fetchToken } from '@/Auth.js';
  export default {
      components: {
          NavbarComp,
          ToolCard,
          OftenQuestions,
          FooterComp,
          UseCasesBlock
      },
      data() {
        return {
          Img: require('@/assets/car.jpg'),
          Img2: require('@/assets/car2.png'),
          Bg: require('@/assets/car.jpg'),
          Bg2: require('@/assets/car.jpg'),
          JPEG: require('@/assets/car.jpg'),
          JPEG2: require('@/assets/car.jpg'),
          isAuthenticated: false
        }
      },
      async created() {
        const result = await fetchToken();
        this.isAuthenticated = result;
      },
      mounted() {
        handlePopState()
        document.title = `FlexFi Upscale - Main`
      }
  }
</script>

<style>
.main-container {
  width: 100%;
  height: auto;
  display: flex;
  padding-top: 200px;
  box-sizing: border-box;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.main-page {
  display: flex;
  align-items: center;
  flex-direction: column;
  gap: 250px;
  z-index: 1;
}

.tools-usage-block {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  gap: 10px;
}

.whatis-about h1 {
  width: 90%;
}

.tools-cards-block {
  display: flex;
  gap: 20px;
}

.whatis-block {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  text-align: center;
  gap: 10px;
}

.whatis-about {
  display: flex;
  align-items: center;
  flex-direction: column;
  width: 100%;
  gap: 30px;
}

.whatis-img {
  width: 90%;
  background: linear-gradient(white, white) padding-box,
  linear-gradient(to right, var(--first_color), var(--secondary_color)) border-box;
  border-radius: 20px;
  border: 4px solid transparent;
}

.whatis-text-desc {
  width: 45%;
}

.whatis-block-block {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 50%;
}


.check-pricing {
  width: auto;
  height: 35px;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
  text-decoration: 0;
  background: transparent;
  border-radius: 10px;
  cursor: pointer;
  background: var(--secondary_color);
  border: 0;
  transition: .3s;
}

.check-pricing:hover {
    background: var(--secondary_hover_color);
}

.whatis__btn {
  width: 100%;
}

.why-us-block {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.why-us-table-features {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.line-vertical-1 {
    width: 2px;
    opacity: 0.3;
    background: linear-gradient(0deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.line-vertical-2 {
    width: 2px;
    opacity: 0.3;
    background: linear-gradient(180deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.horizontal-line {
    height: 2px;
    width: 100%;
    opacity: 0.3;
    background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #fff 50%, rgba(255, 255, 255, 0) 100%);
}

.why-item {
  padding: 24px;
  width: 50%;
  overflow-wrap: anywhere;
  align-items: center;
  justify-content: center;
}

.main_signup_btn {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    text-decoration: 0;
    background: transparent;
    padding: 0 10px;
    width: 50%;
    height: 35px;
    border-radius: 10px;
    cursor: pointer;
    background: var(--secondary_color);
    border: 0;
    transition: .3s;
}

.main_signup_btn:hover {
    background: var(--secondary_hover_color);
}

.get-started-main-block {
  width: 90% !important;
}

@media (min-width: 768px) and (max-width: 991px) {
  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
}

@media (min-width: 651px) and (max-width: 767px) {
  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
}

@media (min-width: 481px) and (max-width: 650px) {
  .whatis-block h1 {
    margin: 0;
  }

  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .main-page {
    padding: 20px
  }

  .whatis-block h1 {
    margin: 0;
  }

  .whatis-text-desc {
    font-size: 15px;
  }

  .whatis-block-block {
    width: 100%;
  }

  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }

  .line-vertical-1 {
    display: none;
  }

  .line-vertical-2 {
    display: none;
  }

  .horizontal-line {
    display: none;
  }

  .why-us-table-features {
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
}
</style>