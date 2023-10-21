<template>
    <div class="interim-container">
        <div v-show="error" id="success" class="white">
            <p class="align_center_text">{{ message }}</p>
            <p style="color: yellow">You'll be automaticly redirected</p>
        </div>
        <page-loader v-show="!error"/>
    </div>
</template>

<script>
    import axios from 'axios'
    import PageLoader from "@/components/UI/PageLoader.vue";
    import handlePopState from "@/utils/index.js";
    import { getHeaders, fetchToken } from '@/Auth';
    import router from '@/router/router';

    export default {
        components: {
            PageLoader
        },
        async mounted() {
            handlePopState()
            if (await fetchToken() === true) {
                this.createPaypalOrder()
            } else {
                router.push({ path: "/pricing", query: { sub_id: this.$route.query.sub_id } })
            }
            if (this.$route.query.sub_id === undefined)  {
                router.push({ path: "/pricing" })
            }
        },
        data() {
            return {
                paypalCreateOrderLink: `/api/v1/payments/paypal/create_order/${this.$route.query.sub_id}/`,
                message: "",
                error: false
            }
        },
        methods: {
            createPaypalOrder() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.paypalCreateOrderLink}`, {}, { headers: getHeaders() })
                .then(res => {
                    window.location.href = res.data.payment_link
                })
                .catch(err => {
                    this.error = true
                    this.message = 'Transaction failure. ' + (err.response.data.error ? err.response.data.error : err.response.data.detail)
                    const success_window = document.getElementById('success');
                    const loader = document.querySelector('.preload');
                    success_window.style.backgroundColor = 'rgb(255, 000, 100)'
                    success_window.classList.add('visible');
                    loader.classList.add('hide');
                    setTimeout(() => {
                        success_window.classList.remove('visible');
                        loader.classList.remove('hide');
                        router.push({ path: '/pricing' })
                    }, 3000);
                })
            }
        }
    }
</script>

<style>
.interim-container {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center
}
</style>