<template>
    <div class="confirm-password-container">
        <template v-if="tokenQuery === undefined && emailQuery === undefined">
            <h1 class="white">Invalid URL</h1>
        </template>
        <template v-else>
            <h1 class="header_text">Password reset confirmation</h1>
            <input-ui max="50" v-model="pass" :passwordType="true" pr="Password"/>
            <input-ui max="50" v-model="pass1" :passwordType="true" pr="Confirm Password"/>
            <button @click="confirmChangingPassword" class="verify_email_button white">Change password</button>
            <p id="message_conf" class="white align_center_text">{{ message }}</p>
        </template>
    </div>
</template>

<script>
    /* eslint-disable */
    import axios from 'axios';
    import router from "@/router/router.js";
    import InputUi from "@/components/UI/InputUi.vue";
    import { setLocalToken, setLocalRefreshToken, fetchToken } from "@/Auth.js";
    export default {
        components: {
            InputUi
        },
        mounted() {
            this.tokenQuery = this.$route.query.token;
            this.emailQuery = this.$route.query.email;
            console.log(this.$route.query.token);
            console.log(this.$route.query.email);
            if(fetchToken() === true) {
                router.push({ path: "/" })
            }
        },
        methods: {
            confirmChangingPassword() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/password_reset/${this.tokenQuery}/${this.emailQuery}/`, {})
                .then(res => {
                    console.log(res);
                    setLocalToken(res.data.access)
                    setLocalRefreshToken(res.data.refresh)
                    this.message = res.data.success + " You will be redirected in 2 seconds."
                    const messageBlock = document.getElementById('message_conf')
                    messageBlock.style.color = "#00FF00"
                    setTimeout(() => {
                        router.push({ path: "/" });
                    }, 2000)
                })
                .catch(err => {
                    console.log(err)
                    this.message = err.response.data.error
                    const messageBlock = document.getElementById('message_conf')
                    messageBlock.style.color = "#FF0000"
                });
            }
        },
        data() {
            return {
                pass: "",
                pass1: "",
                emailQuery: undefined,
                tokenQuery: undefined,
                message: ""
            };
        },
    }
</script>

<style>
.confirm-password-container {
    position: fixed;
    width: 100%;
    height: 100%;
    display: flex;
    box-sizing: border-box;
    background-color: #171921;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 20px;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1;
}

.confirm-password-container .input-container {
    width: 200px;
}

.confirm-password-container .input-container input {
    width: 200px;
    max-width: 200px;
    height: 35px;
    background: transparent;
    padding-left: 20px;
    box-sizing: border-box;
    border: 1px #2e2f35 solid;
    color: #fff;
    outline: none;
    border-radius: 10px;
    transition: .3s;
}

.verify_email_button {
    background-color: #00FF00;
    border: none;
    border-radius: 4px;
    padding: 5px 10px;
    cursor: pointer;
    transition: .3s;
}

.verify_email_button:hover {
    background-color: #00b330;
}
</style>