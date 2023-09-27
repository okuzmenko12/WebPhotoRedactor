<template>
    <div class="questions-block">
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
</style>