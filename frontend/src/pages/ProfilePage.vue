<template>
    <div @click="navbarToggle" id="mobile__btn"></div>
    <div @click="navbarToggle" id="mobile__btn_close">✖</div>
    <div class="profile-container">
        <div @click="redirectToMain" id="close_modal" class="profile_close_page" style="z-index: 4;">
            <svg height="15px" style="transform: rotate(180deg);" viewBox="0 0 5 9">
                <path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path>
            </svg>
            To Main
        </div>
        <div id="profile_bar" class="profile_bar">
            <div class="white user_info">
                <p class="no-margin">Hello,</p>
                <p class="no-margin" style="overflow-wrap: anywhere;">{{ username }}!</p>
            </div>
            <div class="profile_buttons">
                <router-link id="prbtn-1" class="profile_button" :class="{ 'active': isActive('#profile') }" to="#profile">
                    Profile
                </router-link>
                <router-link id="prbtn-2" class="profile_button" :class="{ 'active': isActive('#credits') }" to="#credits">
                    Credits
                </router-link>
                <router-link id="prbtn-3" class="profile_button" :class="{ 'active': isActive('#plan') }" to="#plan">
                    Transaction
                </router-link>
            </div>
        </div>
        <div class="tab_info-block">
            <template v-if="$route.hash === '#profile'">
                <div class="basic_user_info white">
                    <div class="flex-block column gp--15">
                        <div class="flex-block baseline gp--15">
                            <h1 class="fs--25 header_text fw--900">Personal information</h1>
                            <h5 class="edit_button" @click="changeInputStatus('username-profile-info')">Edit</h5>
                        </div>
                        <input-ui max="25" enableReadonly="true" inputId="username-profile-info" @change="handleUsernameChange" v-model="username" />
                        <button v-if="showUsernameButton" class="change-pass-btn" @click="changeUsername">Change username</button>
                        <p id="user_message" class="fs--15">{{ user_message }}</p>
                    </div>
                    <div class="flex-block column gp--15">
                        <div class="flex-block baseline gp--15">
                            <h1 class="fs--25 header_text fw--900">Email</h1>
                            <h5 class="edit_button" @click="changeInputStatus('email-profile-info')">Edit</h5>
                        </div>
                        <input-ui max="50" @change="handleEmailChange" enableReadonly="true" inputId="email-profile-info" v-model="email" />
                        <button v-if="showEmailButton" class="change-pass-btn" @click="changeEmail">Change email</button>
                        <p id="email_message" class="fs--15">{{ email_message }}</p>
                    </div>
                    <div class="flex-block column gp--15">
                        <h1 class="fs--25 header_text fw--900">Password reset</h1>
                        <button class="change-pass-btn" @click="sendChangePasswordRequest">Reset password</button>
                        <p id="pass_message" class="fs--15">{{ pass_message }}</p>
                    </div>
                </div>
            </template>
            <template v-else-if="$route.hash === '#credits'">
                <div></div>
            </template>
            <template v-else-if="$route.hash === '#plan'">
                <div></div>
            </template>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import { getHeaders } from '@/Auth.js';
    import handlePopState from "@/utils/index.js";
    import router from "@/router/router.js";
    import InputUi from "@/components/UI/InputUi.vue";
    export default {
        components: {
            InputUi
        },
        data() {
            return {
                username: "",
                email: "",
                Stusername: "",
                Stemail: "",
                user_message: "",
                email_message: "",
                pass_message: "",
                showEmailButton: false,
                showUsernameButton: false,
            }
        },
        async mounted() {
            axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/user/`, { headers: await getHeaders() })
            .then(res => {
                document.title = `FlexFi Upscale - ${res.data.username}`
                this.username = res.data.username
                this.email = res.data.email
                this.Stusername = res.data.username
                this.Stemail = res.data.email
            })
            .catch(() => {
                router.push({ path: "/" })
            })
            handlePopState()
        },
        methods: {
            navbarToggle() {
                    const navbar = document.getElementById('profile_bar')
                    const button = document.getElementById('mobile__btn')
                    const redirectToMainBtn = document.getElementById('close_modal')
                    const closeButton = document.getElementById('mobile__btn_close')
                    navbar.classList.toggle('visible')
                    redirectToMainBtn.classList.toggle('visible')
                    closeButton.classList.toggle('visible')
                    button.classList.toggle('hide')
            },
            redirectToMain() {
                router.push({ path: "/" })
            },
            handleEmailChange() {
                if (this.Stemail == this.email) {
                    this.showEmailButton = false;
                } else {
                    this.showEmailButton = true;
                }
            },
            handleUsernameChange() {
                if (this.Stusername == this.username) {
                    this.showUsernameButton = false;
                } else {
                    this.showUsernameButton = true;
                }
            },
            changeEmail() {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/change_email/`, { 'email': this.email }, { headers: getHeaders() })
                .then(res => {
                    this.email_message = res.data.success
                    const passObj = document.getElementById('email_message')
                    passObj.style.color = "#00FF00"
                })
                .catch(() => {
                    if (this.Stemail == this.email) {
                        this.showEmailButton = false;
                        this.email_message = 'Please write a new one!'
                        const passObj = document.getElementById('email_message')
                        passObj.style.color = "#FF0000"
                    }
                })
            },
            changeUsername() {
                axios.patch(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/user/`, { 'username': this.validateUsername() }, { headers: getHeaders() })
                .then(res => {
                    console.log(res);
                    this.user_message = `Username was successfuly change to ${res.data.username}`
                    this.Stusername = res.data.username
                    const passObj = document.getElementById('user_message')
                    passObj.style.color = "#00FF00"
                })
                .catch(() => {
                    if (this.Stusername == this.username) {
                        this.showUsernameButton = false;
                        this.user_message = 'Please write a new one!'
                        const passObj = document.getElementById('user_message')
                        passObj.style.color = "#FF0000"
                    }
                })
            },
            changeInputStatus(id) {
                const input = document.getElementById(id);
                console.log(input.readOnly);
                if (input.hasAttribute('readonly')) {
                    input.removeAttribute('readonly');
                } else {
                    input.setAttribute('readonly', true);
                }
            },
            generateId(length) {
                const characters = 'abcdefghijklmnopqrstuvwxyz0123456789';
                let id = '';
                for (let i = 0; i < length; i++) {
                    const randomIndex = Math.floor(Math.random() * characters.length);
                    id += characters[randomIndex];
                }
                return id;
            },
            validateUsername() {
                const usrnm = this.username.split("")
                if (usrnm[0] !== "@") {
                    return "@" + usrnm.join("")
                } else if (usrnm.length < 4) {
                    return "@user"
                } else {
                    return usrnm.join("")
                }
            },
            isActive(hash) {
                return this.$route.hash === hash;
            }
        }
    }
</script>

<style>
.profile-container {
    position: fixed;
    width: 100%;
    height: auto;
    display: flex;
    box-sizing: border-box;
    justify-content: left;
    align-items: center;
    z-index: 1;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background-color: #171921;
}

.profile_bar {
    position: relative;
    width: 300px;
    height: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
    gap: 50px;
    background-color: #1b1e29;
    overflow-y: auto;
    overflow-x: hidden;
}

.user_info {
    display: flex;
    justify-content: start;
    flex-direction: column;
    padding: 70px 20px 20px 20px;
    width: 100%;
    box-sizing: border-box;
}

.profile_buttons {
    width: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
}

.profile_button {
    color: #fff;
    width: 100%;
    display: flex;
    justify-content: center;
    text-decoration: none;
    align-items: center;
    padding: 10px 20px;
    background-color: transparent;
    border-radius: 4px;
    cursor: pointer;
    gap: 10px;
    transition: .3s;
}

.profile_button.active {
    background-color: #0000006b;
    scale: 110%
}

.profile_button:hover {
    background-color: #0000006b;
    scale: 110%
}

.tab_info-block {
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

.basic_user_info {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: 100px;
    box-sizing: border-box;
    gap: 50px;
    overflow-y: auto;
}

.basic_user_info .input-container {
    max-width: 200px;
    height: 35px;
}

.basic_user_info .input-container input {
    width: 100%;
    height: 100%;
    background: transparent;
    padding-left: 20px;
    box-sizing: border-box;
    border: 1px #2e2f35 solid;
    color: #fff;
    outline: none;
    border-radius: 10px;
    transition: .3s;
}

.basic_user_info input:focus {
	scale: 105%;
}

.edit_button {
    color: var(--secondary_color);
    cursor: pointer;
    transition: .3s;
}

.edit_button:hover {
    color: var(--secondary_hover_color)
}

.change-pass-btn {
    color: #fff;
    width: 150px;
    height: 35px;
    background-color: #242B38;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: .3s;
}

.change-pass-btn:hover {
    background-color: #181c24;
}

@media (min-width: 768px) and (max-width: 991px) {
    .profile_bar {
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        display: none;
        align-items: center;
        flex-direction: column;
        gap: 50px;
        background-color: #1b1e29;
        overflow-y: auto;
        overflow-x: hidden;
        z-index: 3;
    }

    #mobile__btn {
        display: flex;
    }

    .profile_close_page {
        display: none
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .profile_bar {
        position: fixed;
        width: 100%;
        height: 100%;
        display: none;
        align-items: center;
        flex-direction: column;
        gap: 50px;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        background-color: #1b1e29;
        overflow-y: auto;
        overflow-x: hidden;
        z-index: 3;
    }

    .profile_close_page {
        display: none
    }

    #mobile__btn {
        display: flex;
    }

    .profile_close_page {
        display: none
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .profile_bar {
        position: fixed;
        width: 100%;
        height: 100%;
        display: none;
        align-items: center;
        flex-direction: column;
        gap: 50px;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        background-color: #1b1e29;
        overflow-y: auto;
        overflow-x: hidden;
        z-index: 3;
    }

    #mobile__btn {
        display: flex;
    }

    .profile_close_page {
        display: none
    }
}

@media (max-width: 480px) {
    .profile_bar {
        position: fixed;
        width: 100%;
        height: 100%;
        display: none;
        align-items: center;
        flex-direction: column;
        gap: 50px;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
        background-color: #1b1e29;
        overflow-y: auto;
        overflow-x: hidden;
        z-index: 3;
    }

    .basic_user_info {
        padding: 100px 0 100px 0;
    }

    #mobile__btn {
        display: flex;
    }

    .profile_close_page {
        display: none
    }
}
</style>