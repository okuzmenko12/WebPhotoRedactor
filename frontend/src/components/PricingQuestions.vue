<template>
    <div class="questions-block">
        <p class="brand_text">FAQ</p>
        <p class="header_text fs--50 fw--900 no-top align_center_text">Pricing questions</p>
        <p class="white fs--20 no-top align_center_text">Here is typicaly asked questions about payment. You can contact us at: <a class="contact_email fs--20 no-top align_center_text" target="_blank" rel="noreferrer" href="mailto:koooilrekt@gmail.com?subject=Contact%20Us">koooilrekt@gmail.com</a></p>
        <template v-if="questions.length > 0">
            <question-model v-for="question in questions" :key="question.id" :question="question.title" :answear="question.text"/>
        </template>

        <template v-else>
            <p class="fs--20 white">No questions was asked.</p>
        </template>
    </div>
</template>

<script>
    import axios from "axios"
    import QuestionModel from "@/components/UI/QuestionModel.vue";
    export default {
        components: {
            QuestionModel
        },
        data() {
            return {
                questions: []
            }
        },
        mounted() {
            axios.get(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/main/pricing_faqs/`)
            .then(res => {
                this.questions = res.data
            })
        }
    }
</script>

<style>
.questions-block {
    width: 70%;
    height: auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

.contact_email {
    color: var(--secondary_color)
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
        width: 60%;
    }
}
</style>