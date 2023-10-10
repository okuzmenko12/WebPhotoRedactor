<template>
  <navbar-comp />
  <div class="main-container">
    <div class="main-page">
      <div class="whatis-block white">
        <p class="brand_text">About us</p>
        <p class="fs--50 fw--700 header_text align_center_text no-top">What is FlexFi Upscale?</p>
        <div class="whatis-about">
          <h1 class="fs--25 fw--400 whatis-text-desc small_text">It's a website where you have all tools in your hand. From upscaling to removing bacgkrounds.</h1>
          <div class="whatis-block-block">
            <router-link v-if="!isAuthenticated" class="main_signup_btn" to="/signup">Start upscaling</router-link>
            <router-link v-else class="main_signup_btn" to="/pricing">Buy tarrif</router-link>
          </div>
        </div>
      </div>
      <div class="tools-usage-block">
        <p class="brand_text">Our tools</p>
        <p class="fs--50 fw--700 header_text no-top align_center_text">We have many tools for your usage</p>
        <div class="tools-cards-block">
          <tool-card name="Upscaling" description="
          Upscale your image resolution and quality just in one click
          "
          :before_img="Img"
          after_img="https://www.meme-arsenal.com/memes/213ea9152c9a595540eed7c536a2d7b5.jpg"
          />
          <tool-card name="Background remove" description="
          Upscale your image resolution and quality just in one click
          "
          before_img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6ddNfEfwkWVEnC0vExOw8OABWGgDIcWGNig&usqp=CAU"
          after_img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ6ddNfEfwkWVEnC0vExOw8OABWGgDIcWGNig&usqp=CAU"
          />
          <tool-card name="Remove JPEG Artifacts" description="
          Upscale your image resolution and quality just in one click
          "
          :before_img="Img"
          after_img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRY_uvokgQMlDBECicro1nnQjkjiKobMlHR-iYjnSVjjB33lcNcq-Ea-qtmhWjiKWsewIY&usqp=CAU"
          />
        </div>
      </div>
      <often-questions />
  </div>
  </div>
  <footer-comp />
</template>

<script>
  import NavbarComp from "@/components/NavbarComp.vue";
  import OftenQuestions from "@/components/OftenQuestion.vue";
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
      },
      data() {
        return {
          Img: require('@/assets/temp_image.jpeg'),
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

@media (min-width: 768px) and (max-width: 991px) {
  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }
}

@media (min-width: 651px) and (max-width: 767px) {
  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
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
}
</style>