<template>
    <navbar-comp />
    <div class="profile-container">
        <div class="user-info white">
            <p class="brand_text no-margin">Username</p>
            <p class="fs--40 fw--900">{{ username }}</p>
            <p class="brand_text no-margin">Email</p>
            <p class="fs--40 fw--900">{{ email }}</p>
            <h5>Ну короче эта фигня ниже будет появляться когда у нашего юзера будет тариф и там нопка будет отменить тариф или как-то так</h5>
        </div>
        <div class="user-sub-info">
            <div class="user-left-data white">
                <p class="brand_text no-margin">Tries left</p>
                <p class="fs--33 fw--900 no-margin">Upscales: 100</p>
                <p class="fs--33 fw--900 no-margin">Upscales: 100</p>
                <p class="fs--33 fw--900 no-margin">Upscales: 100</p>
            </div>
            <div class="tarrif-data white">
                <div>
                    <p class="brand_text no-margin">Your tarrif:</p>
                    <p class="fs--40 fw--900 no-margin">Basic plan</p>
                </div>
                <button class="cancel-tarrif__btn fw--25 fw--700 white">Cancel tarrif</button>
                <button class="change-tarrif__btn fw--25 fw--700 white">Change tarrif</button>
            </div>
        </div>
    </div>
    <footer-comp />
</template>

<script>
    import axios from 'axios'
    import { getHeaders } from '@/Auth.js';
    import NavbarComp from "@/components/NavbarComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    import handlePopState from "@/utils/index.js";
    export default {
        components: {
            NavbarComp,
            FooterComp
        },
        data() {
            return {
                username: "",
                email: ""
            }
        },
        async mounted() {
            axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/user/`, { headers: await getHeaders() })
            .then(res => {
                document.title = `FlexFi Upscale - ${res.data.username}`
                this.username = res.data.username
                this.email = res.data.email
            }),
            handlePopState()
        }
    }
</script>

<style>
.profile-container {
    position: relative;
    width: 100%;
    height: auto;
    display: flex;
    padding-top: 200px;
    box-sizing: border-box;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    z-index: 1;
    gap: 20px;
}

.user-sub-info {
    width: 90%;
    height: 250px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 20px;
}

.tarrif-data {
    border-radius: 20px;
    width: 50%;
    height: 100%;
    box-sizing: border-box;
    background: linear-gradient(#171921, #171921) padding-box,
    linear-gradient(to right, var(--first_color), var(--secondary_color)) border-box;
    border: 4px solid transparent;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 20px
}

.user-left-data {
    border-radius: 20px;
    width: 50%;
    height: 100%;
    box-sizing: border-box;
    background: linear-gradient(#171921, #171921) padding-box,
    linear-gradient(to right, var(--first_color), var(--secondary_color)) border-box;
    border: 4px solid transparent;
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    gap: 20px
}

.cancel-tarrif__btn {
    width: 150px;
    background-color: #FF0066;
    border-radius: 4px;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    transition: .3s;
}

.cancel-tarrif__btn:hover {
    background-color: #ba044d;
}

.change-tarrif__btn {
    width: 150px;
    background-color: #74f77d;
    border-radius: 4px;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    transition: .3s;
}

.change-tarrif__btn:hover {
    background-color: #51bd59;
}

.user-info {
    position: relative;
    width: 90%;
    height: auto;
    border-radius: 20px;
    background: linear-gradient(#171921, #171921) padding-box,
    linear-gradient(to right, var(--first_color), var(--secondary_color)) border-box;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    box-sizing: border-box;
    border: 4px solid transparent;
}

@media (min-width: 651px) and (max-width: 767px) {
    .user-info .fs--40 {
        font-size: 25px;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .user-info .fs--40 {
        font-size: 25px;
    }
}

@media (max-width: 480px) {
    .user-info .fs--40 {
        font-size: 17px;
    }
}
</style>