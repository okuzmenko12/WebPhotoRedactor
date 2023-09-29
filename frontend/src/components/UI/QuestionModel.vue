<template>
        <div @click="toggleActive" :class="{ active: isActive }" class="ContentBx white">
            <div class="Label" :class="{ active: isActive }">
                {{ question }}
            </div>
            <div class="Content small_text" @click.stop :class="{ active: isActive }">
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
  border-radius: 10px;
  transition: .3s;
}

.Label {
  position: relative;
  padding: 10px;
  background: #ffffff0a;
  backdrop-filter: blur(25px);
  border-radius: 10px;
  border: 1px solid #3d3d3d;
  cursor: pointer;
  transition: .3s;
}

.Label.active {
  border-radius: 10px 10px 0 0;
  border: 0;
}

.ContentBx.active {
  border: 1px solid #3d3d3d;
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
  background: #ffffff0a;
  backdrop-filter: blur(25px);
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