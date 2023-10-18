<template>
    <div :id="div_id" class="slider" :class="div_class">
        <div class="before-slider">
            <div class="slider-resize" data-type="resize"></div>
        </div>
        <div class="after-slider"></div>
    </div>
</template>

<script>
const getTemplate = (state) => {
    return `
        <div class="before-slider" style='width: ${state.width}; background-image: url(${state.before})'>
            <div class="slider-resize" data-type="resize"></div>
        </div>
        <div class="after-slider" style='background-image: url(${state.after})'></div>
    `;
}

class Slider {
    constructor(element, state) {
        setTimeout(() => {
            this.$slider = document.getElementById(element)
            this.state = {
                ...state,
                width: state.width || `${this.$slider.parentNode.clientWidth / 2}px`
            };
            this.#render(this.state);
            this.#listen();
        }, 0)
    }

    #render(state) {
        this.$slider.innerHTML = getTemplate(state);
    }

    #update(props) {
        this.state = {
            ...this.state,
            ...props
        };
        this.#render(this.state);
    }

    #listen() {
        this.mouseDownHandler = this.mouseDownHandler.bind(this);
        this.mouseUpHandler = this.mouseUpHandler.bind(this);
        this.moveHandler = this.moveHandler.bind(this);
        this.$slider.addEventListener('mousedown', this.mouseDownHandler);
        this.$slider.addEventListener('mouseup', this.mouseUpHandler);
    }

    mouseDownHandler(event) {
        if (event.target.dataset.type === 'resize') {
            this.currentX = event.clientX;
            this.$slider.addEventListener('mousemove', this.moveHandler);
        }
    }

    mouseUpHandler() {
        this.$slider.removeEventListener('mousemove', this.moveHandler);
    }

    moveHandler(event) {
        let newX = this.currentX - event.clientX;
        let newWidth = `${parseInt(this.state.width) - newX}px`;
        this.#update({ width: newWidth });
        this.currentX = event.clientX;
    }
}

export default {
    props: {
        before_img: String,
        after_img: String,
        div_class: String
    },
    data() {
        return {
            div_id: '',
        }
    },
    methods: {
        generateId(length) {
            const characters = 'abcdefghijklmnopqrstuvwxyz0123456789'; // Pool of characters
            let id = '';
            for (let i = 0; i < length; i++) {
                const randomIndex = Math.floor(Math.random() * characters.length);
                id += characters[randomIndex];
            }
            return id;
        }
    },
    mounted() {
        this.div_id = this.generateId(6);
        const slider = new Slider(this.div_id, { // eslint-disable-line
            after: this.after_img,
            before: this.before_img
        });
    }
}
</script>

<style>
.slider {
    position: relative;
    width: 90%;
    height: 400px;
    background-color: transparent;
}

.before-slider {
    position: absolute;
    width: 50%;
    height: 100%;
    z-index: 2;
    background-size: cover;
    max-width: 90%;
    min-width: 10%;
    border-radius: 20px 0 0 20px;
}

.after-slider {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 1;
    background-size: cover;
    border-radius: 20px;
}

.slider-resize {
    position: absolute;
    width: 5px;
    height: 100%;
    right: 0;
    top: 0;
    background-color: #000;
    cursor: e-resize;
}

.slider-resize::before {
    content: "<";
    position: absolute;
    font-size: 30px;
    top: 50%;
    right: 5px;
    color: #000;
}

.slider-resize::after {
    content: ">";
    position: absolute;
    font-size: 30px;
    top: 50%;
    left: 5px;
    color: #000;
}
</style>