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
    /* eslint-disable */
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
            await this.loadStripeSDK()
            if (await fetchToken() === true) {
                this.createStripeOrder()
            } else {
                router.push({ path: "/pricing", query: { sub_id: this.$route.query.sub_id } })
            }
            if (this.$route.query.sub_id === undefined)  {
                router.push({ path: "/pricing" })
            }
        },
        data() {
            return {
                stripeCreateOrderLinl: `/api/v1/payments/stripe/create_checkout_session/${this.$route.query.sub_id}/`,
                message: "",
                error: false
            }
        },
        methods: {
            createStripeOrder() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.stripeCreateOrderLinl}`, {}, { headers: getHeaders() })
                .then(res => {
                    return this.stripe.redirectToCheckout({sessionId: res.data.checkout_session_id})
                })
                .catch(err => {
                    console.log(err);
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
            },
            loadStripeSDK() {
                return new Promise((resolve, reject) => {
                    const script = document.createElement('script');
                    script.src = "https://js.stripe.com/v3/";
                    script.async = true;
                    script.onload = () => {
                        axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/stripe/config/`)
                        .then(res => {
                            console.log(res)
                            this.stripe = Stripe(res.data.public_key);
                        })
                        resolve();
                    };
                    script.onerror = reject;
                    document.body.appendChild(script);
                });
            },
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