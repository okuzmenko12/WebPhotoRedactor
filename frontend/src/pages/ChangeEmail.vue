<template>
    <div class="confirm-email-container">
        <template v-if="tokenQuery === undefined && emailQuery === undefined">
            <h1 class="white">Invalid URL</h1>
        </template>
        <template v-else>
            <h1 class="header_text">Change email confirmation</h1>
            <button @click="changeEmailRequest" class="change_email_button white">Changle email</button>
            <p id="message_conf" class="white align_center_text">{{ message }}</p>
        </template>
    </div>
</template>

<script>
    /* eslint-disable */
    import axios from 'axios';
    import router from "@/router/router.js";
    import { setLocalToken, setLocalRefreshToken, fetchToken, getHeaders } from "@/Auth.js";
    export default {
        mounted() {
            this.tokenQuery = this.$route.query.token;
            this.emailQuery = this.$route.query.email;
            if(fetchToken() === false) {
                router.push({ path: "/" })
            }
        },
        methods: {
            changeEmailRequest() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/change_email_confirm/${this.tokenQuery}/${this.emailQuery}/`, {}, { headers: getHeaders() })
                .then(res => {
                    this.message = res.data.success + " You will be redirected in 2 seconds."
                    const messageBlock = document.getElementById('message_conf')
                    messageBlock.style.color = "#00FF00"
                    setTimeout(() => {
                        router.push({ path: "/" });
                    }, 2000)
                })
                .catch(err => {
                    this.message = err.response.data.error
                    const messageBlock = document.getElementById('message_conf')
                    messageBlock.style.color = "#FF0000"
                });
            }
        },
        data() {
            return {
                tokenQuery: undefined,
                emailQuery: undefined,
                message: ""
            };
        },
    }
</script>

<style>
.confirm-email-container {
    position: fixed;
    width: 100%;
    height: 100%;
    display: flex;
    box-sizing: border-box;
    background-color: #171921;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1;
}

.change_email_button {
    background: var(--secondary_color);
    border: none;
    border-radius: 4px;
    padding: 5px 10px;
    cursor: pointer;
    transition: .3s;
}

.change_email_button:hover {
    background: var(--secondary_hover_color);
}
</style>