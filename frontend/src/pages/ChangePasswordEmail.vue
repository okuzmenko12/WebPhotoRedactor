<template>
    <div class="confirm-password-container">
        <h1 class="header_text align_center_text">Password reset confirmation</h1>
        <input-ui max="50" v-model="email" pr="Email "/>
        <button @click="sendChangePasswordRequest" class="reset_password_button white">Send mail</button>
        <p id="message_conf" class="white align_center_text">{{ message }}</p>
    </div>
</template>

<script>
    /* eslint-disable */
    import axios from 'axios';
    import router from "@/router/router.js";
    import InputUi from "@/components/UI/InputUi.vue";
    import { setLocalToken, setLocalRefreshToken, fetchToken, getHeaders } from "@/Auth.js";
    export default {
        components: {
            InputUi
        },
        mounted() {
            if(fetchToken() === true) {
                router.push({ path: "/" })
            }
        },
        methods: {
            sendChangePasswordRequest() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/password_reset/`, { 'email': this.email })
                .then(res => {
                    this.message = res.data.success
                    const passObj = document.getElementById('message_conf')
                    passObj.style.color = "#00FF00"
                })
                .catch(err => {
                    if (err.response.data.non_field_errors) {
                        this.message = err.response.data.non_field_errors[0]
                    } else if (err.response.data.email) {
                        this.message = err.response.data.email[0]
                    }
                    const passObj = document.getElementById('message_conf')
                    passObj.style.color = "#FF0000"
                })
            },
        },
        data() {
            return {
                email: "",
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

.reset_password_button {
    background: var(--secondary_color);
    border: none;
    border-radius: 4px;
    padding: 5px 10px;
    cursor: pointer;
    transition: .3s;
}

.reset_password_button:hover {
    background-color: var(--secondary_hover_color);
}
</style>