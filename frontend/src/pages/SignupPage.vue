<template>
    <div class="auth-block">
        <div class="question-auth">
            <router-link to="/login" class="ask__btn">Log In</router-link>
            <h5>Already have an account? Log in!</h5>
        </div>
        <form class="auth-form" @submit.prevent>
            <h1>Sign Up</h1>
            <input-ui maxlength="50" v-model="email" pr="Email"/>
            <input-ui maxlength="50" v-model="password" :passwordType="true" :type="showPassword ? 'text' : 'password'" pr="Password"/>
            <input-ui maxlength="50" v-model="password1" :passwordType="true" :type="showPassword ? 'text' : 'password'" pr="Confirm password"/>
            <button class="auth__authpage__btn" @click="sendSignUpRequest">Sign up</button>
            <h5 id="message__auth">{{ message }}</h5>
        </form>
    </div>
</template>

<script>
    import axios from 'axios';
    import InputUi from "@/components/UI/InputUi.vue";
    import handlePopState from "@/utils/index.js";
    import router from '@/router/router';
    import { fetchToken } from '@/Auth.js';
    export default {
        components: {
            InputUi
        },
        data() {
            return {
                email: "",
                password: "",
                password1: "",
                message: "",
                showPassword: false
            }
        },
        methods: {
            sendSignUpRequest() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/registration/`, {
                "email": this.email,
                "password": this.password,
                "password1": this.password1
                })
                .then(res => {
                    this.message = res.data.message
                    const message = document.getElementById('message__auth')
                    message.style.color = "#00FF00"
                })
                .catch(err => {
                    if (err.response.data.email) {
                        this.message = err.response.data.email[0]
                    } else if (err.response.data.password) {
                        this.message = err.response.data.password[0]
                    } else if (err.response.data.password1) {
                        this.message = err.response.data.password1[0]
                    } else if (err.response.data.non_field_errors) {
                        this.message = err.response.data.non_field_errors[0]
                    }
                    const message = document.getElementById('message__auth')
                    message.style.color = "#FF0000"
                })
            },
            togglePasswordVisibility() {
                this.showPassword = !this.showPassword;
            },
            async checkToken() {
                if (await fetchToken()) {
                    router.push({ path: '/' })
                }
            }
        },
        mounted() {
            document.title = `FlexFi Upscale - Sign Up`
            handlePopState(),
            this.checkToken()
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

#message__auth {
    width: 100%;
    text-align: center;
}

.auth-form {
    width: 50%;
    display: flex;
    align-items: start;
    flex-direction: column;
    color: #fff;
    gap: 20px;
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

@media (min-width: 768px) and (max-width: 991px) {
    .auth-block {
        width: 60%;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .auth-block {
        width: 100%;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .auth-block {
        width: 100%;
    }
}

@media (max-width: 480px) {
    .auth-block {
        width: 100%;
    }
}
</style>