<template>
    <div class="success_container">
        <template v-if="validURL === true">
            <p>Correct URL</p>
            <div v-if="success === true" id="success_modal" class="white">
                <p class="align_center_text no-margin">{{ message }}</p>
                <p style="color: yellow" class="no-margin">You'll be automaticly redirected</p>
            </div>
        </template>
        <template v-else>
            <p>Invalid URL</p>
        </template>
    </div>
</template>

<script>
    import axios from "axios"
    import router from "@/router/router.js";
    export default {
        mounted() {
            if (this.$route.query.token !== undefined) {
                this.queryToken = this.$route.query.token
                this.validURL = true
                this.success = true
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/paypal/complete_order/${this.queryToken}/`)
                .then(res => {
                    const modal = document.getElementById('success_modal')
                    const status = res.data.status
                    if (status == "COMPLETED") {
                        console.log(status);
                        modal.style.backgroundColor = '#66ff63'
                    }
                })
                .catch(err => {
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
    z-index: 112;
    gap: 10px;
}
</style>