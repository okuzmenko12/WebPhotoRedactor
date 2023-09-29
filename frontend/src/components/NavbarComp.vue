<template>
    <div @click="navbarToggle" id="mobile__btn">
    </div>
    <div @click="navbarToggle" id="mobile__btn_close">✖</div>
    <nav id="navbar-nav">
        <div class="nav__sect">
            <router-link to="/" class="white up link fs--25 fw--900">FlexFi Upscale</router-link>
            <div class="nav__subsect">
                <router-link to="/pricing" class="nav__btn white up link">
                    Pricing
                    <svg xmlns="http://www.w3.org/2000/svg" width="12" height="21" viewBox="0 0 12 21">
                        <path d="M11 7.03255C11 1.07441 1 0.683712 1 7.03255C1 13.3814 11 12.893 11 16.507C11 20.1209 1 20.5116 1 16.507M6 0V21" stroke-width="2" fill="none"/>
                    </svg>
                </router-link>
                <router-link to="/features" class="nav__btn white up link">
                    Featues
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="19" viewBox="0 0 20 19">
                        <path class="fill_obj" d="M9.04894 0.927052C9.3483 0.00574108 10.6517 0.00573985 10.9511 0.92705L12.4697 5.60081C12.6035 6.01284 12.9875 6.2918 13.4207 6.2918H18.335C19.3037 6.2918 19.7065 7.53141 18.9228 8.10081L14.947 10.9894C14.5966 11.244 14.4499 11.6954 14.5838 12.1074L16.1024 16.7812C16.4017 17.7025 15.3472 18.4686 14.5635 17.8992L10.5878 15.0106C10.2373 14.756 9.7627 14.756 9.41221 15.0106L5.43648 17.8992C4.65276 18.4686 3.59828 17.7025 3.89763 16.7812L5.41623 12.1074C5.5501 11.6954 5.40345 11.244 5.05296 10.9894L1.07722 8.10081C0.293507 7.53141 0.696283 6.2918 1.66501 6.2918H6.57929C7.01252 6.2918 7.39647 6.01284 7.53035 5.60081L9.04894 0.927052Z"/>
                    </svg>
                </router-link>
                <router-link to="/blog" class="nav__btn white up link">
                    Blog
                    <svg xmlns="http://www.w3.org/2000/svg" width="33" height="22" viewBox="0 0 33 22">
                        <path d="M7.875 20.5H31.5V1.5H7.875V7.12963M7.875 20.5V7.12963M7.875 20.5L1.5 9.94444L7.875 7.12963M29.25 7.12963H10.125M17.625 11H29.25M29.25 14.5185H10.125M10.125 9.24074V12.4074H13.5V9.24074H10.125Z" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                    </svg>
                </router-link>
            </div>
        </div>
        <div class="nav__auth-btn white">
            <router-link to="/login" class="auth link">Log in</router-link >
            <router-link to="/singup" class="log-in__btn auth link">Sing up</router-link >
        </div>
        <router-view/>
    </nav>
</template>

<script>
export default {
    mounted() {
        const navBar = document.getElementById('navbar-nav');

        window.addEventListener('scroll', () => {
            if (window.scrollY > 0) {
                navBar.classList.add('scrolled');
            } else {
                navBar.classList.remove('scrolled');
            }
        });
    },
    methods: {
        navbarToggle() {
            const navbar = document.getElementById('navbar-nav')
            const button = document.getElementById('mobile__btn')
            const closeButton = document.getElementById('mobile__btn_close')
            navbar.classList.toggle('visible')
            closeButton.classList.toggle('visible')
            button.classList.toggle('hide')
        }
    }
}
</script>

<style>
#navbar-nav {
    position: fixed;
    top: 0;
    width: 100%;
    height: auto;
    padding: 10px 100px 10px 200px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: transparent;
    box-sizing: border-box;
    z-index: 100;
    transition: .3s
}

#navbar-nav.scrolled {
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(25px);
}

#mobile__btn {
    position: fixed;
    top: 20%;
    left: 0;
    border-radius: 0 20px 20px 0;
    width: 30px;
    height: 50px;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(25px);
    z-index: 2;
    display: none;
    transition: .3s;
}

#mobile__btn::before {
    content: ">";
    position: absolute;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 25px;
    color: #fff;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
}

#mobile__btn_close {
    position: fixed;
    top: 20px;
    right: 20px;
    background: transparent;
    display: none;
    color: #ffffff;
    font-weight: 900;
    z-index: 101;
    transition: .3s;
}

#mobile__btn_close:hover {
    color: #FF0000;
}

.visible {
    display: flex !important;
}

.hide {
    display: none !important;
}

.white {
    color: white;
}

.up {
    text-transform: uppercase;
}

.nav__sect {
    display: flex;
    align-items: center;
    gap: 50px;
}

.nav__subsect {
    display: flex;
    align-items: center;
    gap: 25px;
}

.nav__btn {
    display: flex;
    align-items: center;
    gap: 5px;
    cursor: pointer;
    transition: .3s;
}

.nav__auth-btn {
    display: flex;
    align-items: center;
    gap: 10px;
}

.auth {
    cursor: pointer;
    transition: .3s;
}

.log-in__btn {
    background: transparent;
    border: rgba(255, 255, 255, 0.22) 1px solid;
    padding: 10px 5px;
    border-radius: 10px;
    cursor: pointer;
    transition: .3s;
}

.log-in__btn:hover {
    background: rgba(238, 130, 238, 0.486);
}

.link {
    color: #fff;
    stroke: #fff;
    text-decoration: none;
    transition: .3s;
}

.link:hover {
    color: rgba(238, 130, 238, 0.911);
    stroke: rgba(238, 130, 238, 0.911);
}

.fill_obj {
    fill: #fff;
    stroke: none;
    transition: .3s;
}

.link:hover .fill_obj {
    fill: rgba(238, 130, 238, 0.911);
}

@media (min-width: 1400px) and (max-width: 1599px) {

}

@media (min-width: 1200px) and (max-width: 1399px) {

}

@media (min-width: 992px) and (max-width: 1199px) {

}

@media (min-width: 768px) and (max-width: 991px) {
    #navbar-nav {
        position: fixed;
        top: 0;
        width: 100%;
        height: 100%;
        padding: 100px 10px 100px 10px;
        display: none;
        align-items: center;
        justify-content: space-between;
        flex-direction: column;
        background: transparent;
        box-sizing: border-box;
        z-index: 100;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(25px);
        transition: .3s
    }

    .nav__sect {
        flex-direction: column;
    }

    .nav__subsect {
        flex-direction: column;
    }


    #mobile__btn {
        display: flex;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    #navbar-nav {
        position: fixed;
        top: 0;
        width: 100%;
        height: 100%;
        padding: 100px 10px 100px 10px;
        display: none;
        align-items: center;
        justify-content: space-between;
        flex-direction: column;
        background: transparent;
        box-sizing: border-box;
        z-index: 100;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(25px);
        transition: .3s
    }

    .nav__sect {
        flex-direction: column;
    }

    .nav__subsect {
        flex-direction: column;
    }


    #mobile__btn {
        display: flex;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    #navbar-nav {
        position: fixed;
        top: 0;
        width: 100%;
        height: 100%;
        padding: 100px 10px 100px 10px;
        display: none;
        align-items: center;
        justify-content: space-between;
        flex-direction: column;
        background: transparent;
        box-sizing: border-box;
        z-index: 100;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(25px);
        transition: .3s
    }

    .nav__sect {
        flex-direction: column;
    }

    .nav__subsect {
        flex-direction: column;
    }


    #mobile__btn {
        display: flex;
    }
}

@media (max-width: 480px) {
    #navbar-nav {
        position: fixed;
        top: 0;
        width: 100%;
        height: 100%;
        padding: 100px 10px 100px 10px;
        display: none;
        align-items: center;
        justify-content: space-between;
        flex-direction: column;
        background: transparent;
        box-sizing: border-box;
        z-index: 100;
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(25px);
        transition: .3s
    }

    .nav__sect {
        flex-direction: column;
    }

    .nav__subsect {
        flex-direction: column;
    }


    #mobile__btn {
        display: flex;
    }
}
</style>