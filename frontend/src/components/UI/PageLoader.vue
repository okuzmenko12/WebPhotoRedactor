<template>
    <div class="preload">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>
.preload {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100px;
}

.preload span {
    display: block;
    height: 15px;
    width: 15px;
    background-color: var(--first_color);
    margin: 0 7px;
    border-radius: 10px;
    animation: 1.2s upDown infinite;
}

.preload span:first-child {
    animation-delay: .15s;
}

.preload span:nth-child(2) {
    animation-delay: .3s;
}

.preload span:nth-child(3) {
    animation-delay: .45s;
}

.preload span:nth-child(4) {
    animation-delay: .6s;
}

.preload span:last-child {
    animation-delay: .75s;
}

@keyframes upDown {
    0% {
        height: 15px;
        background-color: var(--first_color)
    }
    50% {
        height: 60px;
        background-color: var(--secondary_color)
    }
    100% {
        height: 15px;
        background-color: var(--first_color)
    }
}
</style>