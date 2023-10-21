<template>
    <div class="success_container">
        <page-loader v-if="validURL === true && success === false" />
        <div v-show="validURL === true && success === true" id="success_modal" class="white">
            <p class="align_center_text no-margin">{{ message }}</p>
            <p style="color: yellow" class="no-margin">You'll be automaticly redirected</p>
        </div>
        <p v-show="validURL === false">Invalid URL</p>
    </div>
</template>

<script>
    import axios from "axios"
    import router from "@/router/router.js";
    import PageLoader from "@/components/UI/PageLoader.vue";
    import handlePopState from "@/utils/index.js";

    export default {
        components: {
            PageLoader
        },
        mounted() {
            handlePopState()
            if (this.$route.query.token !== undefined) {
                this.queryToken = this.$route.query.token
                this.validURL = true
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/stripe/foreign/cancel_order/${this.queryToken}/`, {})
                .then(res => {
                    this.success = true
                    const modal = document.getElementById('success_modal')
                    this.message = res.data.success
                    if (window.location.href.includes('/payment/stripe/notified_cancel')) {
                        modal.style.backgroundColor = 'rgb(255, 000, 121)';
                    } else {
                        modal.style.backgroundColor = '#66ff63'
                    }
                    modal.style.backgroundColor = '#66ff63'
                    setTimeout(() => {
                        router.push({ path: "/" })
                    }, 2000)
                })
                .catch(err => {
                    this.success = true
                    const modal = document.getElementById('success_modal')
                    this.message = err.response.data.error
                    modal.style.backgroundColor = 'rgb(255, 000, 121)';
                    setTimeout(() => {
                        router.push({ path: "/" })
                    }, 2000)
                })
            }
        },
        data() {
            return{
                queryToken: "",
                message: "",
                success: false,
                validURL: false,
            }
        }
    }
</script>

<style>
.success_container {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 112;
    background-color: #171921;
}


#success_modal {
    position: fixed;
    width: 20%;
    height: auto;
    border-radius: 20px;
    padding: 50px 20px;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    display: flex;
    transition: .3s;
    gap: 10px;
}
</style>