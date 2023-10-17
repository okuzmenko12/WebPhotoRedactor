<template>
    <navbar-comp />
    <div class="features-container">
        <div class="articles_arts_cont">
            <p class="brand_text">Features</p>
            <h1 class="fs--50 fw--700 header_text align_center_text no-top">FlexFI Upscale features:</h1>
            <div class="articles_container">
                <article-ui name="Upscaling" article="article text" />
                <article-ui name="Background remove" article="article text" />
                <article-ui name="Remove JPEG Artifacts" article="article text" />
            </div>
        </div>

        <div class="more-features-block">
            <div class="flex_block column align_center_text">
                <p class="brand_text">More</p>
                <p class="header_text fs--33 fw--900 no-top">More about FlexFI Upscale Features</p>
            </div>
            <div class="more-features-block-block">
                <div class="about-feature-block">
                    <div class="about-feature-info white">
                        <p class="fs--33 fw--90">Upscaling</p>
                        <div @click="setNewImg($event, 1)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p>
                        </div>
                        <div @click="setNewImg($event, 2)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p>
                        </div>
                        <div @click="setNewImg($event, 3)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p>
                        </div>
                    </div>
                    <div class="about-feature-image-block">
                        <img v-if="upscaleBlock === 1" class="about-feature-image" :src="UpImg1">
                        <img v-else-if="upscaleBlock === 2" class="about-feature-image" :src="UpImg2">
                        <img v-else class="about-feature-image" :src="UpImg3">
                    </div>
                </div>
                <div class="hor-line"></div>
                <div class="about-feature-block">
                    <div class="about-feature-image-block">
                        <img v-if="bgBlock === 1" class="about-feature-image" :src="BgImg1">
                        <img v-else-if="bgBlock === 2" class="about-feature-image" :src="BgImg2">
                        <img v-else class="about-feature-image" :src="BgImg3">
                    </div>
                    <div class="about-feature-info white">
                        <p class="fs--33 fw--90">Background remove</p>
                        <div @click="setNewImgBg($event, 1)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgBg($event, 2)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgBg($event, 3)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                    </div>
                </div>
                <div class="hor-line"></div>
                <div class="about-feature-block">
                    <div class="about-feature-info white">
                        <p class="fs--33 fw--90">Remove JPEG Artifacts</p>
                        <div @click="setNewImgJpeg($event, 1)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgJpeg($event, 2)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgJpeg($event, 3)" class="article_choose__btn">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        </div>
                    <div class="about-feature-image-block">
                        <img v-if="jpegBlock === 1" class="about-feature-image" :src="JpegImg1">
                        <img v-else-if="jpegBlock === 2" class="about-feature-image" :src="JpegImg2">
                        <img v-else class="about-feature-image" :src="JpegImg3">
                    </div>
                </div>
            </div>
        </div>
    </div>
<footer-comp />
</template>

<script>
    import NavbarComp from "@/components/NavbarComp.vue";
    import FooterComp from "@/components/FooterComp.vue";
    import ArticleUi from "@/components/UI/ArticleUi.vue";
    import handlePopState from "@/utils/index.js";
    export default {
        components: {
            NavbarComp,
            FooterComp,
            ArticleUi
        },
        data() {
            return {
                upscaleBlock: 0,
                bgBlock: 0,
                jpegBlock: 0,
                UpImg1: require("@/assets/h.jpg"),
                UpImg2: require("@/assets/a.jpg"),
                UpImg3: require("@/assets/d.jpg"),
                BgImg1: require("@/assets/c.png"),
                BgImg2: require("@/assets/d.jpg"),
                BgImg3: require("@/assets/e.png"),
                JpegImg1: require("@/assets/f.jpg"),
                JpegImg2: require("@/assets/g.png"),
                JpegImg3: require("@/assets/h.jpg"),
            }
        },
        mounted() {
            handlePopState()
            document.title = `FlexFi Upscale - Features`
        },
        methods: {
            setNewImg(e, value) {
                if (this.upscaleBlock !== value) {
                    document.querySelectorAll(".article_choose__btn").forEach(elem => elem.classList.remove('active'))
                    this.upscaleBlock = value
                    e.target.classList.add("active")
                    console.log(value);
                }
            },
            setNewImgBg(e, value) {
                if (this.bgBlock !== value) {
                    document.querySelectorAll(".article_choose__btn").forEach(elem => elem.classList.remove('active'))
                    this.bgBlock = value
                    e.target.classList.add("active")
                    console.log(value);
                }
            },
            setNewImgJpeg(e, value) {
                if (this.jpegBlock !== value) {
                    document.querySelectorAll(".article_choose__btn").forEach(elem => elem.classList.remove('active'))
                    this.jpegBlock = value
                    e.target.classList.add("active")
                    console.log(value);
                }
            },
        }
    }
</script>

<style>
.features-container {
    width: 100%;
    height: auto;
    display: flex;
    padding-top: 200px;
    box-sizing: border-box;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 200px;
    z-index: 1;
}

.articles_arts_cont {
    width: 100%;
    display: flex;
    align-items: center;
    flex-direction: column;
}

.articles_container {
    width: 80%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    flex-wrap: wrap;
}

.more-features-block {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    color: #fff;
}

.more-features-block-block {
    width: 80%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
    padding: 20px 50px;
    border-radius: 20px;
    gap: 50px;
}

.about-features-blocks-container {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
}

.about-feature-block {
    width: 70%;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.about-feature-info {
    width: 40%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    gap: 20px;
}

.article_choose__btn {
    width: 100%;
    height: 150px;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
    color: #fff;
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
    padding: 20px 50px;
    border-radius: 20px;
    cursor: pointer;
    gap: 20px;
    transition: .3s;
}

.article_choose__btn.active {
    background-color: #ffffff2a;
}

.article_choose__btn:hover {
    background-color: #ffffff2a;
}

.about-feature-image-block {
    width: 400px;
    height: 400px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.about-feature-image {
    width: 100%;
    height: 100%;
    border-radius: 20px;
}

.v-1 {
    width: 2px;
    margin-left: 100px;
    margin-right: 100px;
    opacity: 0.3;
    background: linear-gradient(0deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.v-2 {
    width: 2px;
    margin-left: 100px;
    margin-right: 100px;
    opacity: 0.3;
    background: linear-gradient(180deg,transparent 0%, #fff 0%, rgba(255,255,255,0) 100%);
}

.v-3 {
    width: 2px;
    margin-left: 100px;
    margin-right: 100px;
    opacity: 0.3;
    background: linear-gradient(180deg,transparent 0%, #fff 0%, #fff 100%);
}

.hl {
    height: 2px;
    width: 100%;
    opacity: 0.3;
    background: linear-gradient(90deg, rgba(255, 255, 255, 0) 0%, #fff 50%, rgba(255, 255, 255, 0) 100%);
}

@media (min-width: 1400px) and (max-width: 1599px) {
    .about-feature-block {
        width: 80%;
    }
}

@media (min-width: 1200px) and (max-width: 1399px) {
    .about-feature-block {
        width: 90%;
    }

    .about-feature-image-block {
        width: 350px;
        height: 350px;
    }
}

@media (min-width: 992px) and (max-width: 1199px) {
    .about-feature-block {
        width: 100%;
    }

    .article_choose__btn {
        width: 90%;
        height: 150px;
    }

    .about-feature-image-block {
        width: 350px;
        height: 350px;
    }
}

@media (min-width: 768px) and (max-width: 991px) {
    .about-feature-block {
        width: 100%;
        flex-direction: column;
    }

    .article_choose__btn {
        width: 90%;
        height: 150px;
    }

    .about-feature-image-block {
        width: 300px;
        height: 300px;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .about-feature-block {
        width: 100%;
        flex-direction: column;
    }

    .article_choose__btn {
        width: 90%;
        height: 150px;
    }

    .about-feature-image-block {
        width: 300px;
        height: 300px;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .about-feature-block {
        width: 100%;
        flex-direction: column;
    }

    .article_choose__btn {
        width: 90%;
        height: 150px;
    }

    .about-feature-image-block {
        width: 200px;
        height: 200px;
    }
}

@media (max-width: 480px) {
    .more-features-block-block {
        width: 60%;
    }

    .about-feature-block {
        width: 100%;
        flex-direction: column;
    }

    .article_choose__btn {
        width: 90%;
        height: 150px;
    }

    .about-feature-image-block {
        width: 150px;
        height: 150px;
    }

    .article_choose__btn .fs--25 {
        font-size: 15px
    }

    .article_choose__btn .small_text {
        font-size: 11px
    }
}
</style>