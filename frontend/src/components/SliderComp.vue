<template>
    <div id="slider" class="slider">
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
            `
    }

    class Slider {
        constructor(selector, state) {
            this.$slider = document.getElementById(selector)
            this.state = {
                ...state,
                width: state.width || '512px'
            }
            this.#render(this.state)
            this.#listen()
        }

        #render() {
            this.$slider.innerHTML = getTemplate(this.state)
        }

        #update(props) {
            this.state = {
                ...this.state,
                ...props
            }
            this.#render(this.state)
        }

        #listen() {
            this.mouseDownHandler = this.mouseDownHandler.bind(this)
            this.mouseUpHandler = this.mouseUpHandler.bind(this)
            this.moveHandler = this.moveHandler.bind(this)
            this.$slider.addEventListener('mousedown', this.mouseDownHandler)
            this.$slider.addEventListener('mouseup', this.mouseUpHandler)
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
        mounted() {
            const slider = new Slider('slider', {
                after: 'https://static3.banki.ru/ugc/90/2c/3f/fe/10991560.jpg',
                before: 'https://exo.in.ua/images/news/2022/03/new-56641.jpg'
            })
        }
    }
</script>

<style>
#slider {
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
    background: no-repeat center center fixed;
    background-size: cover;
    border-radius: 20px 0 0 20px;
}

.after-slider {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 1;
    background: no-repeat center center fixed;
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
}

.slider-resize::after {
    content: ">";
    position: absolute;
    font-size: 30px;
    top: 50%;
    left: 5px;
}
</style>