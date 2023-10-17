<template>
    <div id="payment-container">
            <div v-show="svg_elem === true" id="success" class="white">
                {{ message }}
                <p style="color: yellow">You'll be automaticly redirected</p>
            </div>
        <div v-if="isLoaded" id="payment-block">
            <div class="payment_methods_block">
                <template v-if="authEd === false">
                    <div class="not-authed-user">
                        <p class="header_text fs--33 fw--700">Create an account</p>
                        <div class="payment_info_block email_block_handler">
                            <div class="not-authed-user-inputs">
                                <input-ui max="50" inputId="name_input_field" v-model="values[0].name" pr="Full name"/>
                                <input-ui max="50" inputId="email_input_field" v-model="values[0].email" pr="Email"/>
                                <p id="email_message_msg" class="align_center_text no-margin">{{ messages[0].email }}</p>
                                <p id="name_message_msg" class="align_center_text no-margin">{{ messages[0].name }}</p>
                            </div>
                            <button @click="handleEmailSendRequest" id="save_email__btn">Save email</button>
                        </div>
                    </div>
                    <p class="header_text fs--33 fw--700">Payment methods</p>
                    <PaymentModel :auth="authEd" name="PayPal" v-model:email="messages[0].email" v-model:name="messages[0].name" description="ahhaahhahaahaha" method='paypal'/>
                    <PaymentModel :auth="authEd" name="Credit card" v-model:email="messages[0].email" v-model:name="messages[0].name" description="hohohohohoohoho" :func="stripeRedirect" url="https://google.com/dsadasdasdasdSdasda" method='stripe'/>
                </template>
                <template v-else>
                    <p class="header_text fs--33 fw--700">Payment methods</p>
                        <PaymentModel :auth="authEd" name="PayPal" :func="paypalRedirect" description="ahhaahhahaahaha" method='paypal'/>
                        <PaymentModel :auth="authEd" name="Credit card" description="hohohohohoohoho" :func="stripeRedirect" url="https://google.com/dsadasdasdasdSdasda" method='stripe'/>
                </template>
            </div>
            <div @click="returnToPricing" id="close_modal">
                <svg height="15px" style="transform: rotate(180deg);" viewBox="0 0 5 9">
                    <path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path>
                </svg>
                To Pricing
            </div>
            <div class="info-group-1">
                <p class="header_text fs--33 fw--700">Plan info</p>
                <div class="payment_info_block">
                    <p class="no-margin fw--900 fs--33">{{ plan.name }}</p>
                    <p class="no-margin fw--900 fs--25">{{ plan.price }}$</p>
                    <div class="card-desc payment_card_desc">
                        <p class="fs--15 fw--700 no-margin desc-elem">
                            {{ plan.up_scales_count }} upscales
                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 21 21" fill="none">
                                <path d="M0 4.56165H16.2162V21" stroke="white" stroke-width="2"/>
                                <path d="M19.46 18.2603H3.24377V1.8219" stroke="white" stroke-width="2"/>
                                <path d="M3.50391 17.9945L20.0005 1" stroke="white" stroke-width="2"/>
                            </svg>
                        </p>
                        <div class="hor-line payment_desc_hor_line"></div>
                        <p class="fs--15 fw--700 no-margin desc-elem">
                            {{ plan.bg_deletions_count }} background removings
                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="13" viewBox="0 0 30 27" fill="none">
                                <path d="M27.5 26.3927H14.25M1 26.3927H8.5M14.25 26.3927H8.5M14.25 26.3927L22.3879 18.3927M8.5 26.3927L1 18.8927L11.6857 7.89271M22.3879 18.3927C22.3879 18.3927 26.3378 14.7503 29 11.8927C31.6622 9.03514 20.5 -1.10727 18 1.39272C15.5 3.8927 11.6857 7.89271 11.6857 7.89271M22.3879 18.3927L11.6857 7.89271" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            </svg>
                        </p>
                        <div class="hor-line payment_desc_hor_line"></div>
                        <p class="fs--15 fw--700 no-margin desc-elem">
                            {{ plan.jpg_artifacts_deletions_count }} JPEG artifacts removings
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22" fill="none">
                                <path d="M6.25584 8.23742C6.55519 7.31611 7.8586 7.3161 8.15795 8.23742L8.60043 9.59922C8.73431 10.0112 9.11826 10.2902 9.55149 10.2902H10.9834C11.9521 10.2902 12.3549 11.5298 11.5712 12.0992L10.4127 12.9409C10.0623 13.1955 9.9156 13.6469 10.0495 14.0589L10.4919 15.4207C10.7913 16.342 9.73682 17.1081 8.95311 16.5387L7.79468 15.6971C7.44419 15.4425 6.9696 15.4425 6.61911 15.6971L5.46069 16.5387C4.67698 17.1081 3.62249 16.342 3.92185 15.4207L4.36432 14.0589C4.4982 13.6469 4.35154 13.1955 4.00105 12.9409L2.84263 12.0992C2.05892 11.5298 2.46169 10.2902 3.43041 10.2902H4.8623C5.29553 10.2902 5.67949 10.0112 5.81336 9.59922L6.25584 8.23742Z" fill="white"/>
                                <path d="M15.4551 1.46353C15.6048 1.00287 16.2565 1.00287 16.4062 1.46353L16.8403 2.79967C16.9072 3.00568 17.0992 3.14516 17.3158 3.14516H18.7207C19.2051 3.14516 19.4065 3.76497 19.0146 4.04967L17.878 4.87546C17.7028 5.00278 17.6295 5.22846 17.6964 5.43447L18.1305 6.77062C18.2802 7.23128 17.753 7.61434 17.3611 7.32964L16.2245 6.50385C16.0493 6.37653 15.812 6.37653 15.6367 6.50385L14.5001 7.32964C14.1083 7.61434 13.581 7.23128 13.7307 6.77062L14.1649 5.43447C14.2318 5.22846 14.1585 5.00278 13.9832 4.87546L12.8466 4.04967C12.4548 3.76497 12.6562 3.14516 13.1405 3.14516H14.5454C14.762 3.14516 14.954 3.00568 15.021 2.79967L15.4551 1.46353Z" fill="white"/>
                                <path d="M16.9727 14.3601C17.1224 13.8994 17.7741 13.8994 17.9237 14.3601L18.3579 15.6962C18.4248 15.9022 18.6168 16.0417 18.8334 16.0417H20.2383C20.7227 16.0417 20.9241 16.6615 20.5322 16.9462L19.3956 17.772C19.2204 17.8993 19.147 18.125 19.214 18.331L19.6481 19.6672C19.7978 20.1278 19.2706 20.5109 18.8787 20.2262L17.7421 19.4004C17.5669 19.2731 17.3296 19.2731 17.1543 19.4004L16.0177 20.2262C15.6259 20.5109 15.0986 20.1278 15.2483 19.6672L15.6824 18.331C15.7494 18.125 15.676 17.8993 15.5008 17.772L14.3642 16.9462C13.9724 16.6615 14.1737 16.0417 14.6581 16.0417H16.063C16.2796 16.0417 16.4716 15.9022 16.5385 15.6962L16.9727 14.3601Z" fill="white"/>
                            </svg>
                        </p>
                    </div>
                    <div class="hor-line payment_desc_hor_line"></div>
                    <div class="total_price_block fs--25">
                    <p class="brand_text fw--900 no-margin" style="width: auto">Total:</p>
                    <p class="fw--900 no-margin" style="width: auto">{{ plan.price }}$</p>
                </div>
                </div>
            </div>
        </div>
        <div v-else class="fs--50 fw--900 header_text"><page-loader /></div>
    </div>
</template>

<script>
import axios from 'axios';
import { getHeaders, fetchToken, setLocalToken, setLocalRefreshToken } from '@/Auth';
import router from '@/router/router';
import handlePopState from "@/utils/index.js";
import PaymentModel from "@/components/UI/PaymentModel";
import InputUi from "@/components/UI/InputUi.vue";
import PageLoader from "@/components/UI/PageLoader.vue";

/* eslint-disable */
export default {
    components: {
        PaymentModel,
        InputUi,
        PageLoader
    },
    async mounted() {
        const subId = this.$route.query.sub_id;
        this.loadStripeSDK();
        handlePopState();
        axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/plans/${subId}/`)
        .then(res => {
            console.log(res);
            this.plan = res.data
            this.stripeId = this.plan.stripe_price_id
            this.sub_id = this.plan.id
        })
        .catch(err => {
            this.handlePageLoad(false)
        })
        this.loadPaypal()
        if (await fetchToken()) {
            this.authEd = true
        } else {
            this.authEd = false
        }
    },
    data() {
        return {
            svg_elem: false,
            plan: "",
            message: "",
            sub_id: "",
            stripe: "",
            stripeId: "",
            paypalRedirectLink: "",
            isLoaded: false,
            authEd: false,
            values: [
                { name: "", email: "" }
            ],
            messages: [
                { name: "", email: "" }
            ],
            paypalCreateOrderLink: `/api/v1/payments/paypal/create_order/${this.$route.query.sub_id}/`,
            stripeCreateOrderLinl: "/api/v1/payments/stripe/create_checkout_session/"
        }
    },
    methods: {
        stripeRedirect() {
            console.log();
            axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.stripeCreateOrderLinl + this.sub_id}/`, {}, { headers: getHeaders() })
            .then(res => {
                return this.stripe.redirectToCheckout({sessionId: res.data.checkout_session_id})
            })
            .catch(err => {
                console.log(err);
                this.message = 'Transaction failure. ' + (err.response.data.error ? err.response.data.error : err.response.data.detail)
                const success_window = document.getElementById('success');
                const payment_block = document.getElementById('payment-block');
                success_window.style.backgroundColor = 'rgb(255, 000, 121)'
                success_window.classList.add('visible');
                payment_block.classList.add('hide');
                setTimeout(() => {
                    success_window.classList.remove('visible');
                    payment_block.classList.remove('hide');
                    router.push({ path: '/pricing' })
                }, 3000);
            })
        },
        paypalRedirect() {
            window.location.href = this.paypalRedirectLink
        },
        handleEmailSendRequest() {
            const input = document.getElementById('email_input_field')
            const msg = document.getElementById('email_message_msg')
            const input2 = document.getElementById('name_input_field')
            const msg2 = document.getElementById('name_message_msg')
            if (input.value.length < 1) {
                input.style.border = '1px solid #FF0000'
                msg.style.color = '#FF0000'
                msg.style.opacity = "1"
                this.messages[0].email = "This field is required"
                setTimeout(() => {
                    msg.style.opacity = "0"
                    input.style.border = '1px #2e2f35 solid'
                }, 2000)
            } else {
                msg.style.opacity = "0"
                input.style.border = '1px #2e2f35 solid'
            }

            if (input2.value.length < 1) {
                input2.style.border = '1px solid #FF0000'
                msg2.style.color = '#FF0000'
                msg2.style.opacity = "1"
                this.messages[0].name = "This field is required"
                setTimeout(() => {
                    msg2.style.opacity = "0"
                    input2.style.border = '1px #2e2f35 solid'
                }, 2000)
            } else {
                msg2.style.opacity = "0"
                input2.style.border = '1px #2e2f35 solid'
            }

            if (input2.value.length > 1 && input.value.length > 1) {
                axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/create_user_for_subscription/`, {
                    "full_name": this.values[0].name,
                    'email': this.values[0].email
                })
                .then(res => {
                    console.log(res);
                    setLocalToken(res.data.access)
                    setLocalRefreshToken(res.data.refresh)
                    this.authEd = true
                })
                .catch(err => {
                    console.log(err);
                    const input = document.getElementById('email_input_field')
                    const msg = document.getElementById('email_message_msg')
                    const input2 = document.getElementById('name_input_field')
                    const msg2 = document.getElementById('name_message_msg')
                    if (err.response.data.email) {
                        input.style.border = '1px solid #FF0000'
                        msg.style.color = '#FF0000'
                        msg.style.opacity = "1"
                        this.messages[0].email = err.response.data.email[0]
                        setTimeout(() => {
                            msg.style.opacity = "0"
                            input.style.border = '1px #2e2f35 solid'
                        }, 2000)
                    }
                })
            }
        },
        handlePageLoad(value) {
            this.isLoaded = value
        },
        loadStripeSDK() {
            return new Promise((resolve, reject) => {
                const script = document.createElement('script');
                script.src = "https://js.stripe.com/v3/";
                script.async = true;
                script.onload = () => {
                    axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/payments/stripe/config/`)
                    .then(res => {
                        console.log(res)
                        this.stripe = Stripe(res.data.public_key);
                    })
                    resolve();
                };
                script.onerror = reject;
                document.body.appendChild(script);
            });
        },
        loadPaypal() {
            axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.paypalCreateOrderLink}`, {}, { headers: getHeaders() })
            .then(res => {
                console.log(res)
                this.paypalRedirectLink = res.data.payment_link
                this.handlePageLoad(true);
            })
            .catch(() => {
                this.handlePageLoad(true);
            })
        },
        returnToPricing() {
            router.push({ path: '/pricing' })
        },
        beforeDestroy() {
            window.removeEventListener('load', this.handlePageLoad(false));
        },
    }
};
</script>

<style>
#payment-container {
    position: fixed;
    width: 100%;
    height: 100%;
    display: flex;
    box-sizing: border-box;
    align-items: center;
    justify-content: center;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1;
}

#payment-block {
    width: 100%;
    height: 100%;
    background-color: #171921;
    display: flex;
    padding: 100px;
    align-items: flex-start;
    justify-content: space-between;
    box-sizing: border-box;
    color: #fff;
    gap: 20px;
    overflow-y: auto;
    overflow-x: hidden;
}

#email_message_msg {
    transition: .3s;
    opacity: 0
}

.payment_methods_block {
    width: 50%;
    max-width: 80%;
    overflow-x: hidden;
    overflow-y: auto;
}

.not-authed-user {
    width: auto;
    display: flex;
    align-items: flex-start;
    flex-direction: column;
}

.email_block_handler {
    display: flex !important;
    flex-direction: row !important;
    align-items: center !important;
    justify-content: space-between !important;
}

.not-authed-user-inputs {
    width: 80%;
    display: flex;
    gap: 20px;
    align-items: center;
}

.not-authed-user-inputs .input-container {
    max-width: 350px;
}

.not-authed-user-inputs .input-container input {
    width: 100%;
    height: 35px;
    background: transparent;
    padding-left: 10px;
    box-sizing: border-box;
    border: 1px #2e2f35 solid;
    color: #fff;
    outline: none;
    border-radius: 10px;
    transition: .3s;
}

#save_email__btn {
    color: #fff;
    background-color: var(--secondary_color);
    border-radius: 4px;
    border: none;
    height: 35px;
    cursor: pointer;
    transition: .3s
}

#save_email__btn:hover {
    background-color: var(--secondary_hover_color);
}

#payment-block p {
    text-wrap: wrap;
    text-align: start;
    overflow-wrap: break-word;
    width: 100%;
}

.payment_info_block {
    width: 100%;
    max-width: 100%;
    padding: 20px;
    box-sizing: border-box;
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
    border-radius: 20px;
    display: flex;
    justify-content: flex-start;
    flex-direction: column;
    overflow-x: hidden;
    overflow-y: auto;
    gap: 20px
}

.info-group-1 {
    width: 40%;
    max-height: 80%;
    display: flex;
    justify-content: flex-start;
    align-items: center;
    flex-direction: column;
}

.info-group-1 p {
    text-wrap: wrap;
    text-align: start;
    overflow-wrap: break-word;
    width: 100%;
}

.total_price_block {
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: center;
}

.payment_info_block p {
    text-align: start;
}

.payment_desc_hor_line {
    width: 100%
}

.payment_card_desc {
    width: 50%
}

#close_modal {
    position: absolute;
    top: 20px;
    left: 20px;
    background: transparent;
    color: #fff;
    stroke: #fff;
    fill: #fff;
    stroke-width: 1px;
    align-items: center;
    font-size: 20px;
    font-weight: 900;
    cursor: pointer;
    z-index: 2;
    transition: .3s;
}

#close_modal:hover {
    color: var(--secondary_color) !important;
    stroke: var(--secondary_color) !important;
    fill: var(--secondary_color) !important;;
}

.stripe__btn {
    background: #fff center center;
    background-size: contain;
    background-repeat: no-repeat;
    border-radius: 4px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 150px;
    height: 25px;
    cursor: pointer
}

#success {
    position: fixed;
    width: 20%;
    height: auto;
    border-radius: 20px;
    padding: 50px 20px;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    display: none;
    transition: .3s;
    z-index: 112;
    gap: 10px;
}

.checkmark {
    fill: #fff;
}

@media (min-width: 1200px) and (max-width: 1399px) {
    .not-authed-user-inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: center;
    }

    .email_block_handler {
        flex-direction: column !important;
    }
}

@media (min-width: 992px) and (max-width: 1199px) {
    .not-authed-user-inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: center;
    }

    .email_block_handler {
        flex-direction: column !important;
    }
}

@media (min-width: 768px) and (max-width: 991px) {
    #payment-block {
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 50px;
        padding: 20px
    }

    .payment_methods_block {
        width: 90%
    }

    .not-authed-user-inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: center;
    }

    .email_block_handler {
        flex-direction: column !important;
    }


    #success {
        width: 75%;
    }

    .info-group-1 {
        width: 90%;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    #payment-block {
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 50px;
        padding: 20px
    }

    .not-authed-user-inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: center;
    }

    .email_block_handler {
        flex-direction: column !important;
    }

    .payment_methods_block {
        width: 90%
    }

    #success {
        width: 75%;
    }

    .info-group-1 {
        width: 90%;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    #payment-block {
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 50px;
        padding: 20px
    }

    .not-authed-user-inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: center;
    }

    .email_block_handler {
        flex-direction: column !important;
    }

    .payment_methods_block {
        width: 90%
    }

    #success {
        width: 75%;
    }

    .info-group-1 {
        width: 90%;
    }
}

@media (max-width: 480px) {
    #payment-block {
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 20px;
        padding: 20px
    }

    .payment_methods_block {
        width: 90%
    }

    .not-authed-user-inputs {
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: 20px;
        align-items: center;
    }

    .email_block_handler {
        flex-direction: column !important;
    }

    .info-group-1 {
        width: 90%;
    }

    #success {
        width: 75%;
    }

    .total_price_block p {
        font-size: 15px;
    }
}
</style>