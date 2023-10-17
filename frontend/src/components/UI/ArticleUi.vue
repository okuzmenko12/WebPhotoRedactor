<template>
    <div v-if="article_id" :id="article_id" class="article" @mouseover="showDescription(true)" @mouseleave="showDescription(false)">
        <p v-if="article_name_id" :id="article_name_id" class="white fs--33 fw--700 art_name">{{ name }}</p>
        <p v-if="article_desc_id" :id="article_desc_id" class="descr_art small_text fs--20">{{ article }}</p>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                article_desc_id: "",
                article_name_id: "",
                article_id: "",
            };
        },
        mounted() {
            this.article_desc_id = `desc-${this.generateId(6)}`
            this.article_name_id = `name-${this.generateId(6)}`
            this.article_id = `art-${this.generateId(6)}`
        },
        props: {
            name: String,
            article: String,
        },
        methods: {
            createId() {
                return this.name.toLowerCase().replaceAll(" ", "")
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
            showDescription(shouldShow) {
                const body = document.getElementById(this.article_id)
                const desc = document.getElementById(this.article_desc_id);
                const name = document.getElementById(this.article_name_id);

                if (desc && name) {
                    const newPosition = shouldShow ? `${0.4 * body.clientHeight - desc.clientHeight}px` : "40%";
                    const newOpacity = shouldShow ? 1 : 0;

                    name.style = desc.style = `
                        position: absolute;
                        bottom: ${shouldShow ? "50%" : "40%"};
                        transition: .3s;
                    `;

                    desc.style.opacity = newOpacity;
                    desc.style.bottom = newPosition;

                    if (shouldShow) {
                        desc.style.display = 'flex';
                    }
                }
            },
        }
    }
</script>

<style>
.article {
    width: 450px;
    height: 300px;
    padding: 20px;
    margin-top: 100px;
    display: flex;
    flex-direction: column;
    gap: 40px;
    text-align: center;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    border-radius: 20px;
    overflow-wrap: anywhere;
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
    border-radius: 20px;
    overflow-y: auto;
    overflow-x: hidden;
}

.descr_art {
    opacity: 0;
    bottom: 40%;
    position: absolute
}

.art_name {
    bottom: 40%;
    position: absolute
}

.article p {
    margin: 0;
    text-transform: capitalize;
}

@media (min-width: 768px) and (max-width: 991px) {
    .article {
        width: 75%;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .article {
        width: 75%;
    }

    .article .fs--50 {
        font-size: 30px;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .article {
        width: 90%;
    }

    .article .fs--50 {
        font-size: 25px;
    }
}

@media (max-width: 480px) {
    .article {
        width: 90%;
    }

    .article .fs--50 {
        font-size: 25px;
    }

    .art_name {
        font-size: 25px
    }
}
</style>