import { createRouter, createWebHistory } from 'vue-router'
import MainPage from "@/pages/MainPage"

const routes = [
    {
        path: '/',
        name: 'Main',
        component: MainPage
    },
    {
        path: '/pricing',
        alias: '/',
        name: 'Pricing',
        component: MainPage
    },
    {
        path: '/features',
        alias: '/',
        name: 'Features',
        component: MainPage
    },
    {
        path: '/blog',
        alias: '/',
        name: 'Blog',
        component: MainPage
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router