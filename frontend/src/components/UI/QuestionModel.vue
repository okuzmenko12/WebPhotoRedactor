<template>
        <div @click="toggleActive" class="ContentBx white">
            <div class="Label" :class="{ active: isActive }">
                {{ question }}
            </div>
            <div class="Content" @click.stop :class="{ active: isActive }">
                {{ answear }}
            </div>
        </div>
</template>

<script>
export default {
    props: {
        question: String,
        answear: String
    },
    data() {
        return {
            isActive: false
        };
    },
    methods: {
        toggleActive() {
            this.isActive = !this.isActive;
        }
    }
};
</script>

<style>
.ContentBx {
  width: 100%;
  min-height: 50px;
}

.Label {
  position: relative;
  padding: 10px;
  background: linear-gradient(to right, var(--first_color), var(--secondary_color), var(--first_color));
  background-position: 0 50%;
  background-size: 700px;
  cursor: pointer;
  border-radius: 10px;
  transition: .3s;
}

.Label.active {
  border-radius: 10px 10px 0 0;
  background-position: 50% 100%;
}

.Label::before {
  content: "+";
  position: absolute;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
  font-size: 1.5em;
}

.Label.active::before {
  content: '-';
}

.Content {
  position: relative;
  background: var(--first_darker_color);
  height: 0;
  overflow: hidden;
  overflow-y: auto;
  overflow-wrap: anywhere;
  transition: .3s;
}

.Content.active {
  padding: 10px;
  height: 150px;
  border-radius: 0 0 10px 10px;
}
</style>