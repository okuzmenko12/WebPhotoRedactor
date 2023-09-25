<template>
    <div>
        <navbar-comp />
        <div class="tarrifs-row">
            <card Upcount="100" BgRemcount="100" JPEGcount="100" name="Starter plan" price="12$" time="month"/>
            <card Upcount="300" BgRemcount="300" JPEGcount="300" name="Smart plan" price="30$" time="3 monthes"/>
            <card Upcount="600" BgRemcount="600" JPEGcount="600" name="Pro plan" price="50$" time="6 monthes"/>
            <card Upcount="1000" BgRemcount="1000" JPEGcount="1000" name="Fancy plan" price="90$" time="year"/>
        </div>
    </div>
</template>

<script>
  import NavbarComp from "@/components/NavbarComp.vue";
  import Card from "@/components/UI/TarrifCard.vue";
  export default {
    components: {
      NavbarComp,
      Card
    }
  }
</script>

<style>
.tarrifs-row {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 40px;
}
</style>