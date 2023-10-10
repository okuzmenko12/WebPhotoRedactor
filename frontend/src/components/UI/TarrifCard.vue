<template>
    <div class="card white">
        <div class="card-top">
            <p class="fs--33 fw--900 no-margin">{{ name }}</p>
            <div class="tarrif-price">
                <svg xmlns="http://www.w3.org/2000/svg" id="header_card_top" viewBox="0 0 371 195">
                    <defs>
                        <linearGradient id="gradient" x1="0%" y1="0%" x2="0%" y2="100%">
                        <stop offset="0%"   stop-color="var(--first_color)"/>
                        <stop offset="100%" stop-color="var(--secondary_color)"/>
                        </linearGradient>
                    </defs>
                    <path fill="url(#gradient)" stroke="url(#gradient)" stroke-width="1" d="M 13.50,-0.50 C 127.83,-0.50 242.17,-0.50 356.50,-0.50 361.98,1.60 366.65,4.93 370.50,9.50 370.50,60.50 370.50,111.50 370.50,162.50 369.17,162.83 369.17,163.17 370.50,163.50 370.50,163.83 370.50,164.17 370.50,164.50 369.20,165.64 368.03,166.97 367.00,168.50 312.12,168.78 257.79,168.44 204.00,167.50 202.49,168.09 200.99,168.76 199.50,169.50 194.56,177.73 189.89,186.06 185.50,194.50 184.83,194.50 184.17,194.50 183.50,194.50 179.11,186.06 174.44,177.73 169.50,169.50 165.96,168.80 162.46,168.13 159.00,167.50 107.92,168.42 55.92,168.75 3.00,168.50 2.34,166.68 1.17,165.34 -0.50,164.50 -0.50,112.83 -0.50,61.17 -0.50,9.50 3.35,4.97 8.02,1.64 13.50,-0.50 Z" />
                </svg>
                <p class="fs--33 no-margin fw--900">{{ price }}</p>
                <p class="fs--12 no-margin fw--900">/ {{ time }}</p>
            </div>
        </div>
        <div class="card-desc">
            <p class="fs--15 fw--700 no-margin desc-elem">
                {{ Upcount }} upscales
                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 21 21" fill="none">
                    <path d="M0 4.56165H16.2162V21" stroke="white" stroke-width="2"/>
                    <path d="M19.46 18.2603H3.24377V1.8219" stroke="white" stroke-width="2"/>
                    <path d="M3.50391 17.9945L20.0005 1" stroke="white" stroke-width="2"/>
                </svg>
            </p>
            <div class="hor-line"></div>
            <p class="fs--15 fw--700 no-margin desc-elem">
                {{ BgRemcount }} background removings
                <svg xmlns="http://www.w3.org/2000/svg" width="15" height="13" viewBox="0 0 30 27" fill="none">
                    <path d="M27.5 26.3927H14.25M1 26.3927H8.5M14.25 26.3927H8.5M14.25 26.3927L22.3879 18.3927M8.5 26.3927L1 18.8927L11.6857 7.89271M22.3879 18.3927C22.3879 18.3927 26.3378 14.7503 29 11.8927C31.6622 9.03514 20.5 -1.10727 18 1.39272C15.5 3.8927 11.6857 7.89271 11.6857 7.89271M22.3879 18.3927L11.6857 7.89271" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                </svg>
            </p>
            <div class="hor-line"></div>
            <p class="fs--15 fw--700 no-margin desc-elem">
                {{ JPEGcount }} JPEG artifacts removings
                <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22" fill="none">
                    <path d="M6.25584 8.23742C6.55519 7.31611 7.8586 7.3161 8.15795 8.23742L8.60043 9.59922C8.73431 10.0112 9.11826 10.2902 9.55149 10.2902H10.9834C11.9521 10.2902 12.3549 11.5298 11.5712 12.0992L10.4127 12.9409C10.0623 13.1955 9.9156 13.6469 10.0495 14.0589L10.4919 15.4207C10.7913 16.342 9.73682 17.1081 8.95311 16.5387L7.79468 15.6971C7.44419 15.4425 6.9696 15.4425 6.61911 15.6971L5.46069 16.5387C4.67698 17.1081 3.62249 16.342 3.92185 15.4207L4.36432 14.0589C4.4982 13.6469 4.35154 13.1955 4.00105 12.9409L2.84263 12.0992C2.05892 11.5298 2.46169 10.2902 3.43041 10.2902H4.8623C5.29553 10.2902 5.67949 10.0112 5.81336 9.59922L6.25584 8.23742Z" fill="white"/>
                    <path d="M15.4551 1.46353C15.6048 1.00287 16.2565 1.00287 16.4062 1.46353L16.8403 2.79967C16.9072 3.00568 17.0992 3.14516 17.3158 3.14516H18.7207C19.2051 3.14516 19.4065 3.76497 19.0146 4.04967L17.878 4.87546C17.7028 5.00278 17.6295 5.22846 17.6964 5.43447L18.1305 6.77062C18.2802 7.23128 17.753 7.61434 17.3611 7.32964L16.2245 6.50385C16.0493 6.37653 15.812 6.37653 15.6367 6.50385L14.5001 7.32964C14.1083 7.61434 13.581 7.23128 13.7307 6.77062L14.1649 5.43447C14.2318 5.22846 14.1585 5.00278 13.9832 4.87546L12.8466 4.04967C12.4548 3.76497 12.6562 3.14516 13.1405 3.14516H14.5454C14.762 3.14516 14.954 3.00568 15.021 2.79967L15.4551 1.46353Z" fill="white"/>
                    <path d="M16.9727 14.3601C17.1224 13.8994 17.7741 13.8994 17.9237 14.3601L18.3579 15.6962C18.4248 15.9022 18.6168 16.0417 18.8334 16.0417H20.2383C20.7227 16.0417 20.9241 16.6615 20.5322 16.9462L19.3956 17.772C19.2204 17.8993 19.147 18.125 19.214 18.331L19.6481 19.6672C19.7978 20.1278 19.2706 20.5109 18.8787 20.2262L17.7421 19.4004C17.5669 19.2731 17.3296 19.2731 17.1543 19.4004L16.0177 20.2262C15.6259 20.5109 15.0986 20.1278 15.2483 19.6672L15.6824 18.331C15.7494 18.125 15.676 17.8993 15.5008 17.772L14.3642 16.9462C13.9724 16.6615 14.1737 16.0417 14.6581 16.0417H16.063C16.2796 16.0417 16.4716 15.9022 16.5385 15.6962L16.9727 14.3601Z" fill="white"/>
                </svg>
            </p>
        </div>
        <button @click="redirectToPaymentPage" class="buy-tariff-button fw--25 fw--700 white">buy</button>
    </div>
</template>

<script>
    import router from '@/router/router';
    import { fetchToken } from '@/Auth.js';
    export default {
        props: {
            name: String,
            price: String,
            time: String,
            Upcount: Number,
            BgRemcount: Number,
            JPEGcount: Number,
            PayPal: String,
            sub_id: Number
        },
        data() {
            return {
                modalVisible: false
            }
        },
        methods: {
            async redirectToPaymentPage() {
                if (await fetchToken()) {
                    router.push({ path: '/payment', query: { sub_id: this.sub_id } });
                } else {
                    router.push({ path: '/signup' });
                }
            }
        }
    }
</script>

<style>
.card {
    position: relative;
    width: 300px;
    height: 448px;
    border-radius: 20px;
    background: #171921;
    background-size: contain;
    background-position: top;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-bottom: 20px;
    box-sizing: border-box;
    z-index: 1;
}

#header_card_top {
    position: absolute;
    top: 0;
    width: 100%;
}

.card-top {
    width: 100%;
    height: 200px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}

.card-desc {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.desc-elem {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 5px;
    margin-top: 5px;
    margin-bottom: 5px;
    text-align: start;
    padding-left: 10px;
    box-sizing: border-box;
}

.tarrif-price {
    display: flex;
    justify-content: center;
    align-items: baseline;
}


.tarrif-price p {
    z-index: 2;
}

.card-top p {
    z-index: 2;
}

.hor-line {
    width: 95%;
    height: 2px;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.28);
}

.buy-tariff-button {
    width: 100px;
    height: 60px;
    border: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    background: linear-gradient(to right, var(--first_color), var(--secondary_color), var(--first_color));
    background-position: 0 50%;
    text-transform: uppercase;
    background-size: 200px;
    cursor: pointer;
    transition: .3s;
}

.buy-tariff-button:hover {
    background-position: 100% 50%;
}

@media (min-width: 481px) and (max-width: 650px) {
    .card {
        width: 230px;
        height: 348px;
    }

    .card-top {
        height: 150px;
    }

    .card-top p {
        font-size: 25px;
    }

    .card-top .fs--12 {
        font-size: 12px;
    }

    .card-desc p {
        font-size: 12px;
    }
}

@media (max-width: 480px) {
    .card {
        width: 200px;
        height: 348px;
    }

    .card-top {
        height: 150px;
    }

    .card-top p {
        font-size: 17px;
    }

    .card-top .fs--12 {
        font-size: 9px;
    }

    .card-desc p {
        font-size: 10px;
    }
}
</style>