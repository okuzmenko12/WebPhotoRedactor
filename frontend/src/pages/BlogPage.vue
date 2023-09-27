<template>
    <navbar-comp />
    <div class="blog-container">
    </div>
<footer-comp />
</template>

<script>
    import NavbarComp from "@/components/NavbarComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    import handlePopState from "@/utils/index.js";
    export default {
        components: {
            NavbarComp,
            FooterComp
        },
        mounted() {
        handlePopState()
        }
    }
</script>

<style>
.blog-container {
  width: 100%;
  height: auto;
  display: flex;
  padding-top: 200px;
  box-sizing: border-box;
  justify-content: center;
  flex-direction: column;
}
</style>