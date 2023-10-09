<template>
    <div class="questions-block">
        <p class="brand_text">FAQ</p>
        <p class="header_text fs--50 fw--900 no-margin">Often questions</p>
        <question-model question="dsadads" answear="dsadsssssssssssssssssssssssssssssssssssdasdasdsad"/>
        <question-model question="dsadads" answear="dsadsssssssssssssssssssssssssssssssssssdasdasdsad"/>
        <question-model question="dsadads" answear="dsadsssssssssssssssssssssssssssssssssssdasdasdsad"/>
        <question-model question="dsadads" answear="dsadsssssssssssssssssssssssssssssssssssdasdasdsad"/>
    </div>
</template>

<script>
    import QuestionModel from "@/components/UI/QuestionModel.vue";
    export default {
        components: {
            QuestionModel
        }
    }
</script>

<style>
.questions-block {
    width: 50%;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

@media (min-width: 768px) and (max-width: 991px) {
    .questions-block {
        width: 75%;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .questions-block {
        width: 75%;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .questions-block {
        width: 75%;
    }
}

@media (max-width: 480px) {
    .questions-block {
        width: 75%;
    }
}
</style>