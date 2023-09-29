<template>
    <navbar-comp />
    <div class="features-container">
        <h1 class="white fs--50 fw--700">FlexFI Upscale features:</h1>
        <article-ui name="Upscaling" article="article text" />
        <article-ui name="Background remove" article="article text" />
        <article-ui name="Remove JPEG Artifacts" article="article text" />
        <article-ui name="Data Cruypto" article="article text" />
    </div>
<footer-comp />
</template>

<script>
    import NavbarComp from "@/components/NavbarComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    import ArticleUi from "@/components/UI/ArticleUi.vue";
    import handlePopState from "@/utils/index.js";
    export default {
        components: {
            NavbarComp,
            FooterComp,
            ArticleUi
        },
        mounted() {
        handlePopState()
        }
    }
</script>

<style>
.features-container {
  width: 100%;
  height: auto;
  display: flex;
  padding-top: 200px;
  box-sizing: border-box;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  z-index: 1;
}
</style>