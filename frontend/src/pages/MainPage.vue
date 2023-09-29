<template>
  <navbar-comp />
  <div class="main-container">
    <div class="main-page">
      <div class="whatis-block white">
        <h1 class="fs--50">What is FlexFi Upscale?</h1>
        <div class="whatis-about">
          <h1 class="fs--25 fw--400 whatis-text-desc">It's a website where you have all tools in your hand. From upscaling to removing bacgkrounds.</h1>
          <div class="whatis-block-block">
            <img class="whatis-img" src="https://www.meme-arsenal.com/memes/934f7ff8a841afd39949a57bde01cc0f.jpg"/>
          </div>
        </div>
      </div>
      <div class="tools-usage-block">
        <h1 class="white">We have many tools for your usage</h1>
        <div class="tools-cards-block">
          <tool-card name="Upscaling" description="
          Upscale your image resolution and quality just in one click
          "/>
          <tool-card name="Background remove" description="
          Upscale your image resolution and quality just in one click
          "/>
          <tool-card name="Remove JPEG Artifacts" description="
          Upscale your image resolution and quality just in one click
          "/>
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
  export default {
      components: {
          NavbarComp,
          ToolCard,
          OftenQuestions,
          FooterComp
      },
      mounted() {
        handlePopState()
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
  gap: 200px;
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

.tools-cards-block {
  display: flex;
  gap: 10px;
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
  width: 50%;
  gap: 30px;
}

.whatis-img {
  width: 100%;
}

.whatis-text-desc {
  width: 45%;
}

.whatis-block-block {
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
  background: #00FFA3;
  border: 0;
  transition: .3s;
}

.check-pricing:hover {
    background: #07c982;
}

.whatis__btn {
  width: 100%;
}

@media (min-width: 768px) and (max-width: 991px) {
  .whatis-about {
    width: 75%;
  }

  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }
}

@media (min-width: 651px) and (max-width: 767px) {
  .whatis-about {
    width: 75%;
  }

  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }
}

@media (min-width: 481px) and (max-width: 650px) {
  .whatis-about {
    width: 75%;
    display: flex;
    flex-direction: column;
  }

  .whatis-block-block {
    width: 85%;
  }

  .whatis-about {
    width: 75%;
  }

  .tools-cards-block {
    flex-direction: column;
    gap: 20px;
  }
}

@media (max-width: 480px) {
  .whatis-text-desc {
    font-size: 20px;
  }

  .whatis-about {
    width: 75%;
    display: flex;
    flex-direction: column;
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