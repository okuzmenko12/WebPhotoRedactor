import { createRouter, createWebHistory } from 'vue-router'

import MainPage from "@/pages/MainPage"
import PricingPage from "@/pages/PricingPage"
import BlogPage from "@/pages/BlogPage"
import FeaturesPage from "@/pages/FeaturesPage"

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
        path: '/blog',
        name: 'Blog',
        component: BlogPage
    },
    {
        path: '/login',
        name: 'Log in',
        component: MainPage
    },
    {
        path: '/singup',
        name: 'Sing Up',
        component: MainPage
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router