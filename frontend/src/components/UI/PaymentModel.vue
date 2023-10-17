<template>
    <div @click="toggleActive" :id="bxId" :class="{ active: isActive }" class="ContentBx-pay white">
        <div class="Label-pay" :id="localId" :class="{ active: isActive }">
            {{ name }}
            <svg v-if="method == 'paypal'" width="30px" height="30px" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
                <circle cx="24" cy="24" r="20" fill="#0070BA"/>
                <path d="M32.3305 18.0977C32.3082 18.24 32.2828 18.3856 32.2542 18.5351C31.2704 23.5861 27.9046 25.331 23.606 25.331H21.4173C20.8916 25.331 20.4486 25.7127 20.3667 26.2313L19.2461 33.3381L18.9288 35.3527C18.8755 35.693 19.1379 36 19.4815 36H23.3634C23.8231 36 24.2136 35.666 24.286 35.2127L24.3241 35.0154L25.055 30.3772L25.1019 30.1227C25.1735 29.6678 25.5648 29.3338 26.0245 29.3338H26.6051C30.3661 29.3338 33.3103 27.8068 34.1708 23.388C34.5303 21.5421 34.3442 20.0008 33.393 18.9168C33.1051 18.59 32.748 18.3188 32.3305 18.0977Z" fill="white" fill-opacity="0.6"/>
                <path d="M31.3009 17.6871C31.1506 17.6434 30.9955 17.6036 30.8364 17.5678C30.6766 17.5328 30.5127 17.5018 30.3441 17.4748C29.754 17.3793 29.1074 17.334 28.4147 17.334H22.5676C22.4237 17.334 22.2869 17.3666 22.1644 17.4254C21.8948 17.5551 21.6944 17.8104 21.6459 18.1229L20.402 26.0013L20.3662 26.2311C20.4481 25.7126 20.8911 25.3308 21.4168 25.3308H23.6055C27.9041 25.3308 31.2699 23.5851 32.2537 18.5349C32.2831 18.3854 32.3078 18.2398 32.33 18.0975C32.0811 17.9655 31.8115 17.8525 31.5212 17.7563C31.4496 17.7324 31.3757 17.7094 31.3009 17.6871Z" fill="white" fill-opacity="0.8"/>
                <path d="M21.6461 18.1231C21.6946 17.8105 21.895 17.5552 22.1646 17.4264C22.2879 17.3675 22.4239 17.3349 22.5678 17.3349H28.4149C29.1077 17.3349 29.7542 17.3803 30.3444 17.4757C30.513 17.5027 30.6768 17.5338 30.8367 17.5687C30.9957 17.6045 31.1508 17.6443 31.3011 17.688C31.3759 17.7103 31.4498 17.7334 31.5222 17.7564C31.8125 17.8527 32.0821 17.9664 32.331 18.0976C32.6237 16.231 32.3287 14.9601 31.3194 13.8093C30.2068 12.5424 28.1986 12 25.629 12H18.169C17.6441 12 17.1963 12.3817 17.1152 12.9011L14.0079 32.5969C13.9467 32.9866 14.2473 33.3381 14.6402 33.3381H19.2458L20.4022 26.0014L21.6461 18.1231Z" fill="white"/>
            </svg>
            <svg v-else version="1.1" xmlns="http://www.w3.org/2000/svg" width="30px" height="30px"  xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                viewBox="0 0 370 370" style="enable-background:new 0 0 370 370;" xml:space="preserve">
            <g id="XMLID_2206_">
                <polygon id="XMLID_2207_" style="fill:#78B9EB;" points="165.531,150 185,150 194.377,150 179.954,135.577 	"/>
                <polygon id="XMLID_2208_" style="fill:#78B9EB;" points="156.375,111.999 138.689,94.313 83.004,150 118.374,150 	"/>
                <path id="XMLID_2209_" style="fill:#5A8BB0;" d="M194.377,150h41.858c-5.35-8.09-4.462-19.089,2.663-26.214
                    c4.828-4.829,11.434-6.77,17.709-5.868c-0.9-6.276,1.04-12.882,5.869-17.711c8.139-8.138,21.334-8.138,29.473,0
                    c8.139,8.139,8.141,21.335,0,29.474c-4.828,4.828-11.434,6.769-17.711,5.868c0.712,4.958-0.341,10.12-3.204,14.451h35.964
                    L345,111.997l-70.732-70.733l-94.314,94.313L194.377,150z"/>
                
                    <rect id="XMLID_2210_" x="182.184" y="-10.691" transform="matrix(0.7071 0.7071 -0.7071 0.7071 96.6202 -121.2638)" style="fill:#5A8BB0;" width="25.01" height="133.379"/>
                <polygon id="XMLID_2211_" style="fill:#3C5D76;" points="118.374,150 165.531,150 179.954,135.577 274.268,41.264 274.268,41.264 
                    250.688,17.685 156.375,111.999 	"/>
                <path id="XMLID_2212_" style="fill:#FFDA44;" d="M274.238,135.549c-4.303-0.618-8.451-2.558-11.762-5.868
                    c-3.311-3.311-5.251-7.46-5.869-11.763c-6.275-0.901-12.881,1.039-17.709,5.868c-7.125,7.125-8.013,18.124-2.663,26.214h34.799
                    C273.897,145.669,274.95,140.507,274.238,135.549z"/>
                <path id="XMLID_2213_" style="fill:#FF5023;" d="M274.238,135.549c6.277,0.9,12.883-1.04,17.711-5.868
                    c8.141-8.139,8.139-21.335,0-29.474c-8.139-8.138-21.334-8.138-29.473,0c-4.829,4.829-6.77,11.435-5.869,17.711
                    c0.618,4.303,2.559,8.452,5.869,11.763C265.787,132.991,269.935,134.931,274.238,135.549z"/>
                <polygon id="XMLID_2214_" style="fill:#A0815C;" points="185,150 165.531,150 118.374,150 83.004,150 25,150 25,370 185,370 	"/>
                <polygon id="XMLID_2215_" style="fill:#786145;" points="271.034,150 236.235,150 194.377,150 185,150 185,370 345,370 
                    345,289.999 235,289.999 225,260 225,259.999 235,230 345,230 345,150 306.998,150 	"/>
                <path id="XMLID_2216_" style="fill:#50412E;" d="M225,259.999V260l10,29.999h110V260v-0.001V230H235L225,259.999z M260,245
                    c8.284,0,15,6.715,15,15c0,8.285-6.716,15-15,15c-8.284,0-15-6.715-15-15C245,251.715,251.716,245,260,245z"/>
                <circle id="XMLID_2219_" style="fill:#CDCDD0;" cx="260" cy="260" r="15"/>
            </g>
            </svg>
        </div>
        <div class="Content-pay small_text" @click.stop :class="{ active: isActive }">
            <p v-if="description !== ''">{{description}}</p>
            <div v-if="method == 'paypal'" @click="func" class="stripe__btn"><svg style="color: #000" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-wallet" viewBox="0 0 16 16"> <path d="M0 3a2 2 0 0 1 2-2h13.5a.5.5 0 0 1 0 1H15v2a1 1 0 0 1 1 1v8.5a1.5 1.5 0 0 1-1.5 1.5h-12A2.5 2.5 0 0 1 0 12.5V3zm1 1.732V12.5A1.5 1.5 0 0 0 2.5 14h12a.5.5 0 0 0 .5-.5V5H2a1.99 1.99 0 0 1-1-.268zM1 3a1 1 0 0 0 1 1h12V2H2a1 1 0 0 0-1 1z" fill="#000"></path></svg></div>
            <div v-else @click="func" class="stripe__btn"><svg style="color: #000" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-wallet" viewBox="0 0 16 16"> <path d="M0 3a2 2 0 0 1 2-2h13.5a.5.5 0 0 1 0 1H15v2a1 1 0 0 1 1 1v8.5a1.5 1.5 0 0 1-1.5 1.5h-12A2.5 2.5 0 0 1 0 12.5V3zm1 1.732V12.5A1.5 1.5 0 0 0 2.5 14h12a.5.5 0 0 0 .5-.5V5H2a1.99 1.99 0 0 1-1-.268zM1 3a1 1 0 0 0 1 1h12V2H2a1 1 0 0 0-1 1z" fill="#000"></path></svg></div>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        name: String,
        url: String,
        method: String,
        description: String,
        func: Function,
        auth: Boolean
    },
    data() {
        return {
            isActive: false,
            localId: `pay-${this.generateId(7)}`,
            bxId: `bx-${this.generateId(7)}`,
        };
    },
    methods: {
        toggleActive() {
            if (this.auth === false) {
                const contentBx = document.getElementById(this.bxId)
                const label = document.getElementById(this.localId)
                const input = document.getElementById('email_input_field')
                const msg = document.getElementById('email_message_msg')
                const input2 = document.getElementById('name_input_field')
                const msg2 = document.getElementById('name_message_msg')
                if (contentBx.classList.contains("activeNow")) {
                    this.isActive = !this.isActive;
                } else {
                    label.style.border = "1px solid #FF0000"
                    if (input.value.length < 1) {
                    input.style.border = '1px solid #FF0000';
                    msg.style.color = '#FF0000';
                    msg.style.opacity = "1";
                    this.updateEmail("This field is required");
                    } else {
                        msg.style.opacity = "0";
                        input.style.border = '1px #2e2f35 solid';
                    }

                    if (input2.value.length < 1) {
                        input2.style.border = '1px solid #FF0000';
                        msg2.style.color = '#FF0000';
                        msg2.style.opacity = "1";
                        this.updateName("This field is required");
                    } else {
                            msg2.style.opacity = "0"
                            input2.style.border = '1px #2e2f35 solid'
                    }
                    setTimeout(() => {
                        label.style.border = "1px solid #3d3d3d"
                        if (input.value.length < 1) {
                            msg.style.opacity = "0"
                            input.style.border = '1px #2e2f35 solid'
                        }
                        if (input2.value.length < 1) {
                            msg2.style.opacity = "0"
                            input2.style.border = '1px #2e2f35 solid'
                        }
                    }, 2000)
                }
            } else {
                this.isActive = !this.isActive;
            }
        },
        updateEmail(value) {
            this.$emit('update:email', value);
        },
        updateName(value) {
            this.$emit('update:name', value);
        },
        generateId(length) {
            const characters = 'abcdefghijklmnopqrstuvwxyz0123456789'; // Pool of characters
            let id = '';
            for (let i = 0; i < length; i++) {
                const randomIndex = Math.floor(Math.random() * characters.length);
                id += characters[randomIndex];
            }
            return id;
        },
    }
};
</script>

<style>
.ContentBx-pay {
    margin-bottom: 10px;
    width: 99%;
    min-height: 50px;
    border-radius: 10px;
    transition: .3s;
}

#paypal-button-container {
    width: 150px;
    height: 25px;
}

.Label-pay {
    position: relative;
    padding: 10px;
    background: #ffffff0a;
    backdrop-filter: blur(25px);
    border-radius: 10px;
    display: flex;
    gap: 10px;
    align-items: center;
    border: 1px solid #3d3d3d;
    cursor: pointer;
    transition: .3s;
}

.Label-pay.active {
    border-radius: 10px 10px 0 0;
    border: 0;
}

.ContentBx-pay.active {
    border: 1px solid #3d3d3d;
}

.Label-pay::before {
    content: "+";
    position: absolute;
    top: 50%;
    right: 20px;
    transform: translateY(-50%);
    font-size: 1.5em;
}

.Label-pay.active::before {
    content: '-';
}

.Content-pay {
    position: relative;
    background: #ffffff0a;
    backdrop-filter: blur(25px);
    height: 0;
    overflow: hidden;
    overflow-y: auto;
    overflow-wrap: anywhere;
    display: flex;
    flex-direction: column;
    text-align: start !important;
    justify-content: space-around;
    transition: .3s;
}

.Content-pay p {
    text-align: start !important;
}

.Content-pay.active {
    padding: 10px;
    height: 150px;
    border-radius: 0 0 10px 10px;
}
</style>