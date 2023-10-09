import { createRouter, createWebHistory } from 'vue-router'

import MainPage from "@/pages/MainPage"
import PricingPage from "@/pages/PricingPage"
import FeaturesPage from "@/pages/FeaturesPage"
import LoginPage from "@/pages/LoginPage"
import SignupPage from "@/pages/SignupPage"
import ProfilePage from "@/pages/ProfilePage"
import PaymentPage from "@/pages/PaymentPage"


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
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router