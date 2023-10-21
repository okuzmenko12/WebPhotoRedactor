import { createRouter, createWebHistory } from 'vue-router'

import MainPage from "@/pages/MainPage";
import PricingPage from "@/pages/PricingPage";
import FeaturesPage from "@/pages/FeaturesPage";
import LoginPage from "@/pages/LoginPage";
import SignupPage from "@/pages/SignupPage";
import ProfilePage from "@/pages/ProfilePage";
import PaymentPage from "@/pages/PaymentPage";
import ConfirmPage from "@/pages/ConfirmPage";
import ChangePassword from "@/pages/ChangePassword";
import ChangePasswordEmail from "@/pages/ChangePasswordEmail";
import ChangeEmail from "@/pages/ChangeEmail";
import ImagePage from "@/pages/ImagePage";
import paypalSuccess from "@/pages/SuccessPaypalPage";
import stripeSuccess from "@/pages/SuccessStripePage";
import paypalCancel from "@/pages/CancelPaypalPage";
import stripeCancel from "@/pages/CancelStripePage";
import IPP from "@/pages/InterimPaymentPaypal";
import IPS from "@/pages/InterimPaymentStripe";

import NotifiedPaymentPage from "@/pages/NotifiedPaymentPage";
import NIPP from "@/pages/NotifiedInterimPaymentPaypal";
import NIPS from "@/pages/NotifiedInterimPaymentStripe";
import notifiedPaypalSuccess from "@/pages/NotifiedSuccessPaypalPage";
import notifiedStripeSuccess from "@/pages/NotifiedSuccessStripePage";
import notifiedPaypalCancel from "@/pages/NotifiedCancelPaypalPage";
import notifiedStripeCancel from "@/pages/NotifiedCancelStripePage";


const routes = [
    {
        path: '/',
        name: 'Main',
        component: MainPage
    },
    {
        path: '/pricing',
        name: 'Pricing',
        component: PricingPage
    },
    {
        path: '/features',
        name: 'Features',
        component: FeaturesPage
    },
    {
        path: '/login',
        name: 'Log in',
        component: LoginPage
    },
    {
        path: '/signup',
        name: 'Sign Up',
        component: SignupPage
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfilePage
    },
    {
        path: '/payment',
        name: 'Payment',
        component: PaymentPage
    },
    {
        path: '/email_confirmation',
        name: 'Email confirmation',
        component: ConfirmPage
    },
    {
        path: '/reset_password',
        name: 'Resseting password',
        component: ChangePasswordEmail
    },
    {
        path: '/reset_password_confirmation',
        name: 'Resseting password confirmation',
        component: ChangePassword
    },
    {
        path: '/change_email_confirmation',
        name: 'Change email confirmation',
        component: ChangeEmail
    },
    {
        path: '/image_upload',
        name: 'Image upload',
        component: ImagePage
    },
    {
        path: '/payment/paypal/success',
        name: 'Paypal success',
        component: paypalSuccess
    },
    {
        path: '/payment/paypal/cancel',
        name: 'Paypal cancel',
        component: paypalCancel
    },
    {
        path: '/payment/stripe/success',
        name: 'Stripe success',
        component: stripeSuccess
    },
    {
        path: '/payment/stripe/cancel',
        name: 'Stripe cancel',
        component: stripeCancel
    },
    {
        path: '/payment/paypal/creating_order',
        name: 'Creating Paypal order',
        component: IPP
    },
    {
        path: '/payment/stripe/creating_order',
        name: 'Creating Stripe order',
        component: IPS
    },
    {
        path: '/payment/notified',
        name: 'Notified payment',
        component: NotifiedPaymentPage
    },
    {
        path: '/payment/paypal/creating_notified_order',
        name: 'Creating Notified Paypal order',
        component: NIPP
    },
    {
        path: '/payment/stripe/creating_notified_order',
        name: 'Creating Notified Stripe order',
        component: NIPS
    },
    {
        path: '/payment/paypal/notified_success',
        name: 'Notified Paypal success',
        component: notifiedPaypalSuccess
    },
    {
        path: '/payment/paypal/notified_cancel',
        name: 'Notified Paypal cancel',
        component: notifiedPaypalCancel
    },
    {
        path: '/payment/stripe/notified_success',
        name: 'Notified Stripe success',
        component: notifiedStripeSuccess
    },
    {
        path: '/payment/stripe/notified_cancel',
        name: 'Notified Stripe cancel',
        component: notifiedStripeCancel
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router