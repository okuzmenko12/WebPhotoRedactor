<template>
    <div class="wrapper">
        <div class="box1 box">
            <p class="fs--20">Print</p>
            <p class="fs--15">Enhance images for web design, print, product discovery and recommendations.</p>
        </div>
        <div class="box2 box">
            <p class="fs--20">E-commerce</p>
            <p class="fs--15">Image Noise Reduction in minutes to properly rank and optimize images for website sales.</p>
        </div>
        <div class="box3 box">
            <p class="fs--20">Graphic Design</p>
            <p class="fs--15">Enlarge pictures, assets, textures, photos, and all the graphics in seconds.</p>
        </div>
        <div class="box4 box">
            <p class="fs--20">Real Estate</p>
            <p class="fs--15">Enhance colors and photo resolution creating the perfect real estate marketing images.</p>
        </div>
        <div class="box5 box">
            <p class="fs--20">Digital painting</p>
            <p class="fs--15">Increasing image resolution and adding details to Luxurious art digital paintings for wallpaper automatically using AI.</p>
        </div>
    </div>
</template>

<script>
    export default {
        
    }
</script>

<style>
.wrapper {
    display: grid;
    width: 80%;
    grid-template-columns: repeat(3, 2fr);
    grid-auto-rows: 100px;
    gap: 20px;
    z-index: 1;
}

.box1 {
    grid-column-start: 2;
    grid-column-end: 4;
    grid-row-start: 1;
    grid-row-end: 3;
    background: url('https://d2ahk8dombjwkf.cloudfront.net/website_images/poster.webp');
    background-repeat: no-repeat;
    background-size: cover;
}
.box2 {
    grid-column-start: 1;
    grid-row-start: 1;
    grid-row-end: 8;
    background: url('https://d2ahk8dombjwkf.cloudfront.net/website_images/ecommerce.webp');
    background-repeat: no-repeat;
    background-size: cover;
}

.box3 {
    grid-column-start: 2;
    grid-row-start: 3;
    grid-row-end: 8;
    background: url('https://d2ahk8dombjwkf.cloudfront.net/website_images/graphicdesignpng.webp');
    background-repeat: no-repeat;
    background-size: cover;
}

.box4 {
    grid-column-start: 3;
    grid-row-start: 3;
    grid-row-end: 10;
    background: url('https://d2ahk8dombjwkf.cloudfront.net/website_images/realestate.webp');
    background-repeat: no-repeat;
    background-size: cover;
}

.box5 {
    grid-column-start: 1;
    grid-column-end: 3;
    grid-row-start: 8;
    grid-row-end: 10;
    background: url('https://d2ahk8dombjwkf.cloudfront.net/website_images/painting.webp');
    background-repeat: no-repeat;
    background-size: cover;
}

.box {
    border: 1px solid #0000005d;
    background-color: #fff;
    border-radius: 20px;
    padding: 50px;
    box-sizing: border-box;
}
</style>