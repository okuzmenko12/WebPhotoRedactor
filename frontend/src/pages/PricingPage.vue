<template>
  <navbar-comp />
  <div class="pricing-container">
    <div class="pricing-block">
        <div class="tarrifs-row">
            <card Upcount="100" BgRemcount="100" JPEGcount="100" name="Starter plan" price="12$" time="month"/>
            <card Upcount="300" BgRemcount="300" JPEGcount="300" name="Smart plan" price="30$" time="3 monthes"/>
            <card Upcount="600" BgRemcount="600" JPEGcount="600" name="Pro plan" price="50$" time="6 monthes"/>
            <card Upcount="1000" BgRemcount="1000" JPEGcount="1000" name="Fancy plan" price="90$" time="year"/>
        </div>
    </div>
  </div>
  <footer-comp />
</template>

<script>
  import Card from "@/components/UI/TarrifCard.vue";
  import NavbarComp from "@/components/NavbarComp.vue";
  import FooterComp from "@/components/FooterComp.vue";
  import handlePopState from "@/utils/index.js";
  export default {
    components: {
      Card,
      NavbarComp,
      FooterComp
    },
    mounted() {
      handlePopState()
    }
  }
</script>

<style>
.pricing-container {
  width: 100%;
  height: auto;
  display: flex;
  padding-top: 200px;
  box-sizing: border-box;
  justify-content: center;
  flex-direction: column;
}

.pricing-block {
  display: flex;
  justify-content: center;
  flex-direction: column;
}

.tarrifs-row {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 40px;
}
</style>