<template>
  <navbar-comp />
  <div class="pricing-container">
    <div class="pricing-block">
        <div class="tarrifs-row">
          <card v-for="plan in plans"
              :key="plan.id"
              :sub_id="plan.id"
              :Upcount="plan.up_scales_count"
              :BgRemcount="plan.bg_deletions_count"
              :JPEGcount="plan.jpg_artifacts_deletions_count"
              :name="plan.name"
              :price="plan.price + '$'"
              :time="plan.period_in_str"
              :PayPal="plan.paypal_plan_id"
          />
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
  import axios from 'axios';
  export default {
    components: {
      Card,
      NavbarComp,
      FooterComp
    },
    mounted() {
      handlePopState(),
      axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/subscriptions/all`)
      .then(res => {
        console.log(res);
        this.plans = res.data
      })
      document.title = `FlexFi Upscale - Pricing`
    },
    data() {
      return {
          plans: []
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