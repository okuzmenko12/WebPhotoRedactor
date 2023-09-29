<template>
    <div class="tool-card white">
        <div class="tool-card-top no-margin">
            <p class="fs--25 fw--900 no-margin">{{ name }}</p>
        </div>
        <div class="tool-card-desc no-margin">
            <p class="fs--15 fw--700 no-margin tool-desc-elem">
                {{ description }}
            </p>
        </div>
        <router-link :to="link" class="readmore__btn fw--25 fw--700 white">Read more</router-link>
    </div>
</template>

<script>
    export default {
        props: {
            name: String,
            description: String
        },
        data() {
            return {
                link: `/features#${this.name.toLowerCase().replaceAll(" ", "")}`
            }
        }
    }
</script>

<style>
.tool-card {
    position: relative;
    width: 300px;
    height: 350px;
    border-radius: 20px;
    background: #171921 no-repeat;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
    padding: 20px 0;
    box-sizing: border-box;
    z-index: 1;
}

.tool-card-top {
    width: auto;
    height: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.tool-card-desc {
    width: 100%;
    height: auto;
    padding: 0 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    box-sizing: border-box;
}

.tool-desc-elem {
    width: auto !important;
    display: flex;
    align-items: center;
    box-sizing: border-box;
}

.hor-line {
    width: 95%;
    height: 2px;
    border-radius: 10px;
    background: rgba(255, 255, 255, 0.28);
}

.readmore__btn {
    width: 100px;
    height: 45px;
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
    text-decoration: 0;
    transition: .3s;
}

.readmore__btn:hover {
    background-position: 100% 50%;
}
</style>