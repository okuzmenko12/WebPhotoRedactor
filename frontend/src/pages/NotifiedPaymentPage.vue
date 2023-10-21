<template>
    <div id="payment-container">
        <div v-if="isLoaded" id="payment-block">
            <div class="payment_methods_block">
                    <p class="header_text fs--33 fw--700">Payment methods</p>
                    <template v-if="paypalRedirectLink === ''">
                        <page-loader />
                    </template>
                    <template v-else>
                        <PaymentModel :auth="allow" name="PayPal" :func="paypalRedirect" description="ahhaahhahaahaha" method='paypal'/>
                        <PaymentModel :auth="allow" name="Credit card" description="hohohohohoohoho" :func="stripeRedirect" method='stripe'/>
                    </template>
            </div>
            <div class="info-group-1">
                <p class="header_text fs--33 fw--700">Payment info</p>
                <div class="payment_info_block">
                    <p class="no-margin fw--900 fs--25">Pay with FlexFi Upscale</p>
                    <div class="hor-line payment_desc_hor_line"></div>
                    <div class="total_price_block fs--25">
                    <p class="brand_text fw--900 no-margin" style="width: auto">Total:</p>
                    <p class="fw--900 no-margin" style="width: auto">{{ amount + currency }}</p>
                </div>
                </div>
            </div>
        </div>
        <div v-else class="fs--50 fw--900 header_text"><page-loader /></div>
    </div>
</template>

<script>
// import axios from 'axios';
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
    mounted() {
        this.ext_id = this.$route.query.ext_id;
        this.amount = this.$route.query.amount;
        this.currency = this.$route.query.currency;
        this.email = this.$route.query.email;
        this.description = this.$route.query.description;
        this.success_url = this.$route.query.success_url;
        this.cancel_url = this.$route.query.cancel_url;
        this.notify_url = this.$route.query.notify_url;
        handlePopState();
        this.loadPaypal()
        this.loadStripe();

        if (this.ext_id !== undefined && this.amount !== undefined && this.currency !== undefined && this.success_url !== undefined && this.cancel_url !== undefined && this.notify_url !== undefined) {
            this.params.push({'ext_id': this.ext_id})
            this.params.push({'amount': this.amount})
            this.params.push({'currency': this.currency})

            if (this.email !== undefined) {
                this.params.push({'email': this.email})
            }

            if (this.description !== undefined) {
                this.params.push({'description': this.description})
            }

            this.params.push({'success_url': this.success_url})
            this.params.push({'cancel_url': this.cancel_url})
            this.params.push({'notify_url': this.notify_url})
            this.handlePageLoad(true);
        }
    },
    watch: {
        authEd() {
            this.loadPaypal()
        }
    },
    data() {
        return {
            allow: true,
            paypalRedirectLink: "",
            stripeRedirectLink: "",
            isLoaded: false,
            
            ext_id: undefined,
            amount: undefined,
            currency: undefined,
            email: undefined,
            description: undefined,
            success_url: undefined,
            cancel_url: undefined,
            notify_url: undefined,
            params: []
        }
    },
    methods: {
        stripeRedirect() {
            if (this.ext_id !== undefined && this.amount !== undefined && this.currency !== undefined && this.success_url !== undefined && this.cancel_url !== undefined && this.notify_url !== undefined) {
                const query = {};
                this.params.forEach(param => {
                    Object.assign(query, param);
                });
                router.push({ path: this.stripeRedirectLink, query })
            } else {
                this.handlePageLoad(false)
            }
        },
        paypalRedirect() {
            if (this.ext_id !== undefined && this.amount !== undefined && this.currency !== undefined && this.success_url !== undefined && this.cancel_url !== undefined && this.notify_url !== undefined) {
                const query = {};
                this.params.forEach(param => {
                    Object.assign(query, param);
                });
                router.push({ path: this.paypalRedirectLink, query })
            } else {
                this.handlePageLoad(false)
            }
        },
        handlePageLoad(value) {
            this.isLoaded = value
        },
        loadPaypal() {
            this.paypalRedirectLink = '/payment/paypal/creating_notified_order'
            console.log(this.paypalRedirectLink);
        },
        loadStripe() {
            this.stripeRedirectLink = '/payment/stripe/creating_notified_order'
            console.log(this.stripeRedirectLink);
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
    position: fixed;
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