<template>
    <article :id=createId() class="article_article">
        <div class="article">
            <p class="white fs--50 fw--700">{{ name }}</p>
            <p class="white fs--20">{{ article }}</p>
        </div>
    </article>
</template>

<script>
    export default {
        props: {
            name: String,
            article: String,
        },
        methods: {
            createId() {
                return this.name.toLowerCase().replaceAll(" ", "")
            }
        }
    }
</script>

<style>
.article_article {
    width: 100%;
    height: auto;
    display: flex;
    justify-content: center;
    align-items: center;
}
.article {
    width: 50%;
    padding: 20px;
    margin-top: 100px;
    display: flex;
    flex-direction: column;
    gap: 40px;
    text-align: start;
    box-sizing: border-box;
    border-radius: 20px;
    overflow-wrap: anywhere;
    background: linear-gradient(rgba(255, 255, 255, 0.4), rgba(255, 255, 255, 0.4)) padding-box,
    linear-gradient(to right, #0500FF, #00FFA3) border-box;
    backdrop-filter: blur(25px);
    border-radius: 20px;
    border: 4px solid transparent;
}

.article p {
    margin: 0;
    text-transform: capitalize;
}
</style>