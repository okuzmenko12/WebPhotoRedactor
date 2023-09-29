import { createRouter, createWebHistory } from 'vue-router'

import MainPage from "@/pages/MainPage"
import PricingPage from "@/pages/PricingPage"
import FeaturesPage from "@/pages/FeaturesPage"
import LoginPage from "@/pages/LoginPage"
import SingupPage from "@/pages/SingupPage"


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
        path: '/singup',
        name: 'Sing Up',
        component: SingupPage
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router