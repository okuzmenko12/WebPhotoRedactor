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
                <p class="header_text fs--50 fw--900 no-top">More about FlexFI Upscale Features</p>
            </div>
            <div class="more-features-block-block">
                <div class="about-feature-block">
                    <div class="about-feature-info white">
                        <p class="fs--33 fw--900 width--100 align_left_text">Upscaling</p>
                        <div @click="setNewImg($event, 1)" class="article_choose__btn UPSC">
                            <p class="fs--25 fw--900 white no-margin">Upscale</p>
                            <p class="small_text no-margin">  </p>
                        </div>
                        <div @click="setNewImg($event, 2)" class="article_choose__btn UPSC">
                            <p class="fs--25 fw--900 white no-margin">Ultra upscale</p>
                            <p class="small_text no-margin">ultra enhance</p>
                        </div>
                        <div @click="setNewImg($event, 3)" :class="upscaleBlock > 3 || upscaleBlock < 1 ? 'active' : '' " class="article_choose__btn UPSC">
                            <p class="fs--25 fw--900 white no-margin">Ultra enhance</p>
                            <p class="small_text no-margin">AAHAHHA</p>
                        </div>
                    </div>
                    <div class="about-feature-image-block">
                        <slider-comp v-if="upscaleBlock === 1" :before_img="UpImg1" :after_img="UpImg1_2" :div_class="sliderClass" />
                        <slider-comp v-else-if="upscaleBlock === 2" :before_img="UpImg2" :after_img="UpImg2_2" :div_class="sliderClass" />
                        <slider-comp v-else :before_img="UpImg3" :after_img="UpImg3_2" :div_class="sliderClass" />
                    </div>
                </div>

                <div class="about-feature-block">
                    <div class="about-feature-image-block">
                        <slider-comp v-if="bgBlock === 1" :before_img="BgImg1" :after_img="BgImg1_2" :div_class="sliderClass" />
                        <slider-comp v-else-if="bgBlock === 2" :before_img="BgImg2" :after_img="BgImg2_2" :div_class="sliderClass" />
                        <slider-comp v-else :before_img="BgImg3" :after_img="BgImg3_2" :div_class="sliderClass" />
                    </div>
                    <div class="about-feature-info white">
                        <p class="fs--33 fw--900 width--100 align_left_text">Background remove</p>
                        <div class=""></div>
                        <div @click="setNewImgBg($event, 1)" class="article_choose__btn BGR">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgBg($event, 2)" class="article_choose__btn BGR">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgBg($event, 3)" :class="bgBlock > 3 || bgBlock < 1 ? 'active' : '' " class="article_choose__btn BGR">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                    </div>
                </div>

                <div class="about-feature-block">
                    <div class="about-feature-info white">
                        <p class="fs--33 fw--900 width--100 align_left_text">Remove JPEG Artifacts</p>
                        <div @click="setNewImgJpeg($event, 1)" class="article_choose__btn RJPEGA">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgJpeg($event, 2)" class="article_choose__btn RJPEGA">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        <div @click="setNewImgJpeg($event, 3)" :class="jpegBlock > 3 || jpegBlock < 1 ? 'active' : '' " class="article_choose__btn  RJPEGA">
                            <p class="fs--25 fw--900 white no-margin">AAHAHHA</p>
                            <p class="small_text no-margin">AAHAHHA</p></div>
                        </div>
                    <div class="about-feature-image-block">
                        <slider-comp v-if="jpegBlock === 1" :before_img="JpegImg1" :after_img="JpegImg1_2" :div_class="sliderClass" />
                        <slider-comp v-else-if="jpegBlock === 2" :before_img="JpegImg2" :after_img="JpegImg2_2" :div_class="sliderClass" />
                        <slider-comp v-else :before_img="JpegImg3" :after_img="JpegImg3_2" :div_class="sliderClass" />
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
    import SliderComp from "@/components/SliderComp.vue";
    export default {
        components: {
            NavbarComp,
            FooterComp,
            ArticleUi,
            SliderComp
        },
        data() {
            return {
                upscaleBlock: 0,
                bgBlock: 0,
                jpegBlock: 0,

                UpImg1: require("@/assets/car2.png"),
                UpImg1_2: require("@/assets/car.jpg"),
                UpImg2: require("@/assets/flower2.png"),
                UpImg2_2: require("@/assets/flower.png"),
                UpImg3: require("@/assets/crystal2.png"),
                UpImg3_2: require("@/assets/crystal.png"),

                BgImg1: require("@/assets/woman.jpg"),
                BgImg1_2: require("@/assets/woman_bg.png"),
                BgImg2: require("@/assets/dog.jpg"),
                BgImg2_2: require("@/assets/dog2.png"),
                BgImg3: require("@/assets/audi_car.jpg"),
                BgImg3_2: require("@/assets/audi_car2.png"),

                JpegImg1: require("@/assets/jpeg_sun.jpg"),
                JpegImg1_2: require("@/assets/jpeg_sun2.png"),
                JpegImg2: require("@/assets/flower2.png"),
                JpegImg2_2: require("@/assets/flower.png"),
                JpegImg3: require("@/assets/flower2.png"),
                JpegImg3_2: require("@/assets/flower.png"),

                sliderClass: "slider-features"
            }
        },
        mounted() {
            handlePopState()
            document.title = `FlexFi Upscale - Features`
        },
        methods: {
            setNewImg(e, value) {
                if (this.upscaleBlock !== value) {
                    document.querySelectorAll(".UPSC").forEach(elem => elem.classList.remove('active'))
                    this.upscaleBlock = value
                    setTimeout(() => {
                        e.target.classList.add("active")
                    }, 0)
                    console.log(value);
                }
            },
            setNewImgBg(e, value) {
                if (this.bgBlock !== value) {
                    document.querySelectorAll(".BGR").forEach(elem => elem.classList.remove('active'))
                    this.bgBlock = value
                    setTimeout(() => {
                        e.target.classList.add("active")
                    }, 0)
                    console.log(value);
                }
            },
            setNewImgJpeg(e, value) {
                if (this.jpegBlock !== value) {
                    document.querySelectorAll(".RJPEGA").forEach(elem => elem.classList.remove('active'))
                    this.jpegBlock = value
                    setTimeout(() => {
                        e.target.classList.add("active")
                    }, 0)
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

.slider-features {
    width: 100% !important;
    height: 100% !important;
}

.about-feature-block {
    width: 70%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid rgba(255, 255, 255, 0.5);
    border-radius: 20px;
    padding: 50px;
    overflow: hidden;
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
    padding: 20px 50px;
    border-radius: 20px;
    cursor: pointer;
    gap: 20px;
    transition: .3s;
}

.article_choose__btn.active {
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
}

.article_choose__btn:hover {
    background-color: #ffffff0a;
    backdrop-filter: blur(25px);
    border: 1px solid rgb(144, 145, 154);
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