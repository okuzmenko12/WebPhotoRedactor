<template>
  <navbar-comp />
  <div class="pricing-container">
    <div class="pricing-block">
        <div class="tarrifs-row">
            <card Upcount="100" BgRemcount="100" JPEGcount="100" name="Starter plan" price="12$" time="month" v-model="modalVisible"/>
            <card Upcount="300" BgRemcount="300" JPEGcount="300" name="Smart plan" price="30$" time="3 monthes" v-model="modalVisible"/>
            <card Upcount="600" BgRemcount="600" JPEGcount="600" name="Pro plan" price="50$" time="6 monthes" v-model="modalVisible"/>
            <card Upcount="1000" BgRemcount="1000" JPEGcount="1000" name="Fancy plan" price="90$" time="year" v-model="modalVisible"/>
        </div>
    </div>
    <sub-modal-wind v-if="modalVisible" v-model="modalVisible" />
  </div>
  <footer-comp />
</template>

<script>
  import Card from "@/components/UI/TarrifCard.vue";
  import NavbarComp from "@/components/NavbarComp.vue";
  import FooterComp from "@/components/FooterComp.vue";
  import handlePopState from "@/utils/index.js";
  import SubModalWind from "@/components/SubscriptionModalWindow.vue"
  export default {
    components: {
      Card,
      NavbarComp,
      FooterComp,
      SubModalWind
    },
    mounted() {
      handlePopState()
    },
    data() {
      return {
          modalVisible: false
      };
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
  align-items: center;
  flex-direction: column;
}

.pricing-block {
  width: 90%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.tarrifs-row {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 40px;
}
</style>