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
                <router-link id="prbtn-3" class="profile_button" :class="{ 'active': isActive('#transactions') }" to="#transactions">
                    Transactions
                </router-link>
            </div>
        </div>
        <div class="tab_info-block">
            <template v-if="$route.hash === '#profile'">
                <div class="basic_user_info white">
                    <div class="flex-block column gp--15">
                        <div class="flex-block baseline gp--15">
                            <h1 class="fs--25 header_text fw--900 width--min">Personal information</h1>
                            <h5 class="edit_button" @click="changeInputStatus('username-profile-info')">Edit</h5>
                        </div>
                        <input-ui max="25" enableReadonly="true" inputId="username-profile-info" @change="handleUsernameChange" v-model="username" />
                        <button v-if="showUsernameButton" class="change-pass-btn" @click="changeUsername">Change username</button>
                        <p id="user_message" class="fs--15">{{ user_message }}</p>
                    </div>
                    <div class="flex-block column gp--15">
                        <div class="flex-block baseline gp--15">
                            <h1 class="fs--25 header_text fw--900 width--min">Email</h1>
                            <h5 class="edit_button" @click="changeInputStatus('email-profile-info')">Edit</h5>
                        </div>
                        <input-ui max="50" @change="handleEmailChange" enableReadonly="true" inputId="email-profile-info" v-model="email" />
                        <button v-if="showEmailButton" class="change-pass-btn" @click="changeEmail">Change email</button>
                        <p id="email_message" class="fs--15">{{ email_message }}</p>
                    </div>
                    <div class="flex-block column gp--15">
                        <h1 class="fs--25 header_text fw--900 width--min">Change password</h1>
                        <input-ui max="50" v-model="old_pass" :passwordType="true" inputId="old_pass_input" pr="Old Password"/>
                        <input-ui max="50" v-model="pass" :passwordType="true" inputId="new_pass_input" pr="Password"/>
                        <input-ui max="50" v-model="pass1" :passwordType="true" inputId="new_passconf_input" pr="Password confirmation"/>
                        <button class="change-pass-btn" @click="sendChangePasswordRequest">Change password</button>
                        <p id="pass_message" class="fs--15">{{ pass_message }}</p>
                    </div>
                </div>
            </template>
            <template v-else-if="$route.hash === '#credits'">
                <div class="basic_user_info white">
                    <div class="flex-block column gp--15">
                        <p class="fs--25 header_text fw--900 width--min">Free credits:</p>
                        <div class="flex-block gp--15 align-items-center">
                            <p class="brand_text width--min">Upscale:</p>
                            <p class="fs--20 no-margin">{{ free_upscale }}</p>
                        </div>
                        <div class="flex-block gp--15 align-items-center">
                            <p class="brand_text width--min">Background removes:</p>
                            <p class="fs--20 no-margin">{{ free_bg }}</p>
                        </div>
                        <div class="flex-block gp--15 align-items-center">
                            <p class="brand_text width--min">JPEG Artifacts removes:</p>
                            <p class="fs--20 no-margin">{{ free_jpeg }}</p>
                        </div>
                    </div>
                    <div class="flex-block column gp--15">
                        <p class="fs--25 header_text fw--900 width--min">Paid credits:</p>
                        <div class="flex-block gp--15 align-items-center">
                            <p class="brand_text width--min">Upscale:</p>
                            <p class="fs--20 no-margin">{{ paid_upscale }}</p>
                        </div>
                        <div class="flex-block gp--15 align-items-center">
                            <p class="brand_text width--min">Background removes:</p>
                            <p class="fs--20 no-margin">{{ paid_bg }}</p>
                        </div>
                        <div class="flex-block gp--15 align-items-center">
                            <p class="brand_text width--min">JPEG Artifacts removes:</p>
                            <p class="fs--20 no-margin">{{ paid_jpeg }}</p>
                        </div>
                    </div>
                </div>
            </template>
            <template v-else-if="$route.hash === '#transactions'">
                <div class="basic_user_info white">
                    <div class="flex-block transactions_container column gp--15">
                        <p class="fs--25 header_text fw--900 width--min">Transactions:</p>
                        <template v-if="transactions.length > 0">
                            <div v-for="transaction in transactions" :key="transaction.id" class="order_block_container width--100 flex-block column" style="border: 1px solid rgb(144, 145, 154); background-color: #1b1e29; border-radius: 20px;">
                                <div class="order_block flex-block space-between">
                                    <div class="flex-block column align_center_text align-items-center width--100">
                                        <p>ORDER ID</p>
                                        <p class="fs--20">#{{ transaction.id }}</p>
                                    </div>

                                    <div class="flex-block column align_center_text align-items-center width--100">
                                        <p>CREATED AT</p>
                                        <p class="fs--20">{{ transaction.parsed_created_at }}</p>
                                    </div>

                                    <div class="flex-block column align_center_text align-items-center width--100">
                                        <p>METHOD</p>
                                        <p class="fs--20">{{ transaction.payment_service }}</p>
                                    </div>

                                    <div class="flex-block column align_center_text align-items-center width--100">
                                        <p>PLAN</p>
                                            <p class="fs--20">{{ transaction.plan.name }}</p>
                                    </div>

                                    <div class="flex-block column align_center_text align-items-center width--100">
                                        <p>PRICE</p>
                                        <p class="fs--20">{{ transaction.plan.price }}$</p>
                                    </div>

                                    <div class="flex-block column align_center_text align-items-center width--100">
                                        <p>STATUS</p>
                                        <p class="fs--20 width--70" style="border-radius: 16px; padding: 0 5px"
                                        :style="transaction.status === 'COMPLETED' ? 'background-color: #66ff63' : transaction.status === 'CANCELED' ? 'background-color: rgb(255, 0, 121)' : transaction.status === 'ACTIVE' ? 'background-color: #fcd056' : ''">
                                            {{ transaction.status }}
                                        </p>
                                    </div>
                                </div>
                            </div>
                        </template>

                        <template v-else>
                            <div class="flex-block column gp--15">
                                <div class="flex-block column gp--15">
                                    <p class="brand_text width--min">No transactions yet</p>
                                </div>
                            </div>
                        </template>
                    </div>
                </div>
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
                old_pass: "",
                pass: "",
                pass1: "",
                userIp: "",

                free_upscale: "",
                free_bg: "",
                free_jpeg: "",

                paid_upscale: "",
                paid_bg: "",
                paid_jpeg: "",

                transactions: [],
                transactions_loaded: false,

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
            axios.get('https://ipapi.co/ip/')
            .then(res => this.userIp = res.data)
            handlePopState()
            this.getUserCredits()
            this.getUserPlan()
        },
        updated() {
            this.getUserCredits()
            this.getUserPlan()
        },
        watch: {
            userIp() {
                this.getUserCredits()
            }
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
            sendChangePasswordRequest() {
                this.pass_message = ""
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/change_password/`, {
                    "old_password": this.old_pass,
                    "new_password": this.pass,
                    "new_password_confirm": this.pass1
                }, { headers: getHeaders() })
                .then(res => {
                    console.log(res)
                })
                .catch(err => {
                    console.log(err);
                    if (err.response.data.new_password) {
                        this.pass_message = err.response.data.new_password[0]
                        const input = document.getElementById('new_pass_input')
                        input.style.border = '1px solid #FF0000'
                        setTimeout(() => {
                            input.style.border = '1px #2e2f35 solid'
                        }, 2000)
                    } 

                    if (err.response.data.new_password_confirm) {
                        this.pass_message = err.response.data.new_password_confirm[0]
                        const input = document.getElementById('new_passconf_input')
                        input.style.border = '1px solid #FF0000'
                        setTimeout(() => {
                            input.style.border = '1px #2e2f35 solid'
                        }, 2000)
                    } 
                    
                    if (err.response.data.error) {
                        this.pass_message = err.response.data.error
                        const input = document.getElementById('old_pass_input')
                        input.style.border = '1px solid #FF0000'
                        setTimeout(() => {
                            input.style.border = '1px #2e2f35 solid'
                        }, 2000)
                    }
                    
                    if (err.response.data.old_password) {
                        this.pass_message = err.response.data.old_password[0]
                        const input = document.getElementById('old_pass_input')
                        input.style.border = '1px solid #FF0000'
                        setTimeout(() => {
                            input.style.border = '1px #2e2f35 solid'
                        }, 2000)
                    }

                    const passObj = document.getElementById('pass_message')
                    passObj.style.color = "#FF0000"
                })
            },
            async getUserCredits() {
                const ip = await this.userIp
                if (this.isActive('#credits') && this.userIp !== "") {
                    axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/user/credits/`, { "ip_address_or_token": ip })
                    .then(res => {
                        console.log(res)
                        this.free_upscale = res.data.free_credits.up_scales_count
                        this.free_bg = res.data.free_credits.bg_deletions_count
                        this.free_jpeg = res.data.free_credits.jpg_artifacts_deletions_count

                        this.paid_upscale = res.data.paid_credits.up_scales_count
                        this.paid_bg = res.data.paid_credits.bg_deletions_count
                        this.paid_jpeg = res.data.paid_credits.jpg_artifacts_deletions_count
                    })
                }
            },
            getUserPlan() {
                if (this.isActive('#transactions') && !this.transactions_loaded) {
                    axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/user_orders/`, { headers: getHeaders() })
                    .then(res => {
                        console.log(res)
                        this.transactions = res.data
                        this.transactions_loaded = true
                    })
                    .catch(err => {
                        console.log(err)
                        this.transactions_loaded = true
                    })
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

@media (min-width: 1400px) and (max-width: 1599px) {
    .order_block .flex-block .fs--20 {
        font-size: 15px;
    }

    .order_block .flex-block p {
        font-size: 15px;
    }
}

@media (min-width: 1200px) and (max-width: 1399px) {
    .order_block .flex-block .fs--20 {
        font-size: 15px;
    }

    .order_block .flex-block p {
        font-size: 15px;
    }
}


@media (min-width: 992px) and (max-width: 1199px) {
    .order_block .flex-block .fs--20 {
        font-size: 10px;
    }

    .order_block .flex-block p {
        font-size: 10px;
    }
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

    .order_block {
        flex-direction: column;
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

    .order_block {
        flex-direction: column;
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

    .order_block {
        flex-direction: column;
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

    .transactions_container {
        align-items: center;
        text-align: left
    }

    .order_block_container {
        width: 90% !important;
    }

    .order_block {
        flex-direction: column;
    }

    .order_block .flex-block .fs--20 {
        font-size: 15px;
    }

    .order_block .flex-block p {
        font-size: 15px;
    }
}
</style>