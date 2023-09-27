<template>
    <div class="auth-block">
        <div class="question-auth">
            <router-link to="/login" class="ask__btn">Log In</router-link>
            <h5>Already have an account? Log in!</h5>
        </div>
        <form class="auth-form" @submit.prevent>
            <h1>Sing Up</h1>
            <input-ui maxlength="50" v-model="email" placeholder="Email"/>
            <input-ui maxlength="50" v-model="password" placeholder="Password"/>
            <input-ui maxlength="50" v-model="password1" placeholder="Confirm password"/>
            <button class="auth__authpage__btn" @click="sendSingUpRequest">Sing up</button>
        </form>
    </div>
</template>

<script>
    import axios from 'axios'
    import InputUi from "@/components/UI/InputUi.vue"
    export default {
        components: {
            InputUi
        },
        data() {
            return {
                email: "",
                password: "",
                password1: ""
            }
        },
        methods: {
            sendSingUpRequest() {
                axios.post(`${this.$backendDomain}/api/v1/auth/registration/`, {
                "email": this.email,
                "password": this.password,
                "password1": this.password1
                })
            }
        }
    }
</script>

<style>
.auth-block {
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
    background: #00FFA3;
    border: 0;
    transition: .3s;
}

.ask__btn:hover {
    background: #07c982;
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
    background: #00FFA3;
    border: 0;
    transition: .3s;
}

.auth__authpage__btn:hover {
    background: #07c982;
}
</style>