<template>
    <div class="auth-block">
        <div class="question-auth">
            <router-link to="/signup" class="ask__btn">Sign Up</router-link>
            <h5>Don't have an account? Sign Up!</h5>
        </div>
        <form class="auth-form" @submit.prevent>
            <h1>Log In</h1>
            <input-ui max="50" v-model="email" pr="Email"/>
            <input-ui max="50" v-model="password" :passwordType="true" pr="Password"/>
            <button class="auth__authpage__btn" @click="sendLogInRequest">Log in</button>
            <router-link to="/reset_password" class="width--100 fs--12 align_center_text link">Forgot password?</router-link>
            <h5 id="message__auth">{{ message }}</h5>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    import InputUi from "@/components/UI/InputUi.vue";
    import handlePopState from "@/utils/index.js";
    import router from '@/router/router';
    import { setLocalToken, setLocalRefreshToken, fetchToken } from '@/Auth.js';
    export default {
        components: {
            InputUi
        },
        data() {
            return {
                email: "",
                password: "",
                message: ""
            }
        },
        methods: {
            sendLogInRequest() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/token/`, {
                "email": this.email,
                "password": this.password,
                })
                .then(res => {
                    this.message = res.data.message
                    const message = document.getElementById('message__auth')
                    message.style.color = "#00FF00"
                    setLocalToken(res.data.access)
                    setLocalRefreshToken(res.data.refresh)
                    router.push({ path: '/' })
                })
                .catch(err => {
                    if (err.response.data.detail) {
                        this.message = err.response.data.detail
                    }
                    const message = document.getElementById('message__auth')
                    message.style.color = "#FF0000"
                })
            },
            async checkToken() {
                if (await fetchToken()) {
                    router.push({ path: '/' })
                }
            }
        },
        mounted() {
            handlePopState(),
            this.checkToken(),
            document.title = `FlexFi Upscale - Log In`
        }
    }
</script>

<style>
.auth-block {
    position: fixed;
    top: 0;
    left: 0;
    width: 50%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #171921;
    z-index: 1;
}

.question-auth {
    width: auto;
    position: fixed;
    display: flex;
    align-items: center;
    color: #707070;
    gap: 10px;
    top: 20px;
    left: 20px;
}

.question-auth h5 {
    margin: 0;
}

.ask__btn {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    text-decoration: 0;
    background: transparent;
    width: 50%;
    height: 35px;
    border-radius: 10px;
    cursor: pointer;
    background: var(--secondary_color);
    border: 0;
    transition: .3s;
}

.ask__btn:hover {
    background: var(--secondary_hover_color);
}

.auth-form {
    width: 50%;
    display: flex;
    align-items: start;
    flex-direction: column;
    color: #fff;
    gap: 20px;
}

.auth-form input {
	width: 100%;
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

.auth-form input:focus {
	scale: 110%;
}

.auth__authpage__btn {
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
    text-decoration: 0;
    background: transparent;
    width: 100%;
    height: 35px;
    border-radius: 10px;
    cursor: pointer;
    background: var(--secondary_color);
    border: 0;
    transition: .3s;
}

.auth__authpage__btn:hover {
    background: var(--secondary_hover_color);
}
</style>