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
    import router from '@/router/router';

    export default {
        components: {
            PageLoader
        },
        async mounted() {
            this.loadStripeSDK()
            this.ext_id = this.$route.query.ext_id;
            this.amount = this.$route.query.amount;
            this.currency = this.$route.query.currency;
            this.success_url = this.$route.query.success_url;
            this.cancel_url = this.$route.query.cancel_url;
            this.notify_url = this.$route.query.notify_url;

            if (this.$route.query.email !== undefined) {
                this.email = this.$route.query.email;
            }

            if (this.$route.query.description !== undefined) {
                this.description = this.$route.query.description;
            }
            handlePopState()
            this.createStripeOrder()
        },
        data() {
            return {
                stripeCreateOrderLink: `/api/v1/payments/stripe/foreign/create_checkout_session/`,
                message: "",
                error: false,

                ext_id: undefined,
                amount: undefined,
                currency: undefined,
                email: undefined,
                description: undefined,
                success_url: undefined,
                cancel_url: undefined,
                notify_url: undefined,
                params: [],
            }
        },
        methods: {
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
            createStripeOrder() {
                const data = {};
                data.ext_id = this.ext_id;
                data.amount = this.amount;
                data.currency = this.currency;
                data.success_url = this.success_url;
                data.cancel_url = this.cancel_url;
                data.notify_url = this.notify_url;
                if (this.email !== undefined) {
                    data.email = this.email;
                }
                if (this.description !== undefined) {
                    data.description = this.description;
                }
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.stripeCreateOrderLink}`, data)
                .then(res => {
                    console.log(res)
                    return this.stripe.redirectToCheckout({sessionId: res.data.checkout_session_id})
                })
                .catch(err => {
                    console.log(err);
                    this.error = true
                    if (err.response.data.cancel_url) {
                        this.message = 'Transaction failure. ' + err.response.data.cancel_url[0]
                    } else if (err.response.data.notify_url) {
                        this.message = 'Transaction failure. ' + err.response.data.notify_url[0]
                    } else if (err.response.data.success_url) {
                        this.message = 'Transaction failure. ' + err.response.data.success_url[0]
                    }

                    const success_window = document.getElementById('success');
                    const loader = document.querySelector('.preload');
                    success_window.style.backgroundColor = 'rgb(255, 000, 121)'
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
    z-index: 112;
    align-items: center
}
</style>