<template>
        <div class="upload_image_container">
            <input v-show="false" ref="imageUploadInput" id="image_upload_btn" type='file' @input="checkIfThereAnyFile" :accept="allowedFormats" />
            <input v-show="false" ref="bgImageUpload" id="image_upload_btn" class="bgImageUpload" :type='bgFile ? "file" : "text"' @input="handleFileChange" :accept="allowedFormats" />
            <div v-if='isLoading === false && loadedFile === false' @drop.prevent="handleDrop" @dragenter.prevent="toggleIsDragOver(true)" @dragleave.prevent="toggleIsDragOver(false)" @dragover.prevent @click="handleClickZone" id="image_upload_block" class="white">
                <template v-if="isDragOver === false && anyFiles === false">
                    <p class="no-margin align_center_text">Drag and drop file</p>
                    <p class="no-margin brand_text align_center_text">or</p>
                    <button id="upload_button">Upload Image</button>
                </template>
                <template v-if="isDragOver === true && anyFiles === false">
                    <p class="no-margin" @drop.prevent>Drag and drop file here</p>
                </template>
                <template v-if="isDragOver === false && anyFiles === true">
                    <div class="align_center_text">{{ fileName }} Size: {{ fileSize }}</div>
                </template>
            </div>

            <template v-if="isLoading === true && loadedFile === false">
                <div id="image_upload_block" :class="{ 'width-auto': fileSrc !== '' }" class="white">
                    <p v-if="loadedFile === false"><page-loader /></p>
                </div>
            </template>

            <template v-if="isLoading === false && loadedFile === true">
                <div id="image_upload_block" :class="{ 'width-auto': fileSrc !== '' }" class="white">
                    <img class="ready_image" @click="downloadImage" :src="fileSrc"/>
                </div>
            </template>
            <div class="flex-block gp--50">
                <button v-if="anyFiles === true && loadedFile === false && isLoading === false" @click="handleFileUploadUpscale" id="upload_button">Start!</button>
                <button v-if="loadedFile === true && fileSrc !== ''" @click="downloadImage" id="upload_button">Download</button>
                <button v-if="loadedFile === true && fileSrc !== ''" @click="uploadMoreFiles" id="upload_button">Upload again!</button>
            </div>
            <p class="error_text fw--900 fs--20">{{ image_upload }}</p>
        </div>
</template>

<script>
    import axios from "axios";
    import { getHeaders, fetchToken, checkTrackingToken } from "@/Auth.js";
    import PageLoader from "@/components/UI/PageLoader.vue";

    export default {
        components: {
            PageLoader
        },
        props: {
            api_url: String,
            upscale_factor: String,
            bg_color: String,
            blur: Number,
            output_type: String,
            bgFile: Boolean,
            bgUrl: String,
            strt: String
        },
        watch: {
            isLoading(newV) {
                this.changeIsLoadingInParentElem(newV)
            }
        },
        async mounted() {
            this.userIp = await checkTrackingToken()
        },
        data() {
            return {
                allowedFormats: ['.jpg', '.jpeg', '.png', '.tiff', '.tga'],
                isDragOver: false,
                anyFiles: false,
                isLoading: false,
                loadedFile: false,
                fileName: "",
                fileSize: 0,
                fileSrc: "",
                fileNameResponse: "",
                image_upload: "",
                userIp: "",
                FDFunctions: []
            }
        },
        methods: {
            handleClickZone() {
                const input = this.$refs.imageUploadInput;
                input.click();
            },
            handleFileChange(event) {
                const selectedFiles = event.target.files[0];
                this.$emit('files-updated', selectedFiles);
            },
            changeIsLoadingInParentElem(value) {
                this.$emit('is_loading', value);
            },
            async handleFileUploadUpscale() {
                this.isLoading = true;
                let bgBlurValid = true;
                const input = this.$refs.imageUploadInput;
                const input2 = this.$refs.bgImageUpload;
                this.image_upload = "";
                const formData = new FormData();
                this.FDFunctions.push({'ip_address_or_token': this.userIp});
                formData.append('image', input.files[0]);

                if (this.bgFile === true) {
                    if (input2.files.length > 0) {
                        formData.append('bg_image', input2.files[0]);
                    } else if (this.bg_color !== undefined && this.bg_color !== '#ffffff') {
                        this.FDFunctions.push({'bg_color': this.bg_color});
                    }
                } else {
                    if (this.bgUrl !== "") {
                        formData.append('bg_image_url', this.bgUrl);
                    } else if (this.bg_color !== undefined && this.bg_color !== '#ffffff') {
                        this.FDFunctions.push({'bg_color': this.bg_color});
                    }
                }

                if (this.blur !== undefined) {
                    let blur = parseInt(this.blur);

                    if (blur > 100 || isNaN(blur) || blur < 0) {
                        this.image_upload = "Please enter a valid blur %, between 0 and 100.";
                        bgBlurValid = false;
                    } else {
                        this.FDFunctions.push({'bg_blur': blur});
                        bgBlurValid = true;
                    }
                }

                if (this.output_type !== undefined) {
                    this.FDFunctions.push({'output_type': this.output_type});
                }

                if (this.upscale_factor !== undefined) {
                    this.FDFunctions.push({'upscale_factor': this.upscale_factor});
                }

                if (this.strt !== undefined) {
                    this.FDFunctions.push({'strength': this.strt});
                }


                this.FDFunctions.forEach(obj => {
                    for (let key in obj) {
                        formData.append(key, obj[key]);
                    }
                });

                if (!this.FDFunctions.some(obj => Object.prototype.hasOwnProperty.call(obj, 'bg_blur')) && bgBlurValid) {
                    this.sendRequestImg(formData)
                } else if (this.FDFunctions.some(obj => Object.prototype.hasOwnProperty.call(obj, 'bg_blur')) && bgBlurValid) {
                    this.sendRequestImg(formData)
                } else if (this.FDFunctions.some(obj => Object.prototype.hasOwnProperty.call(obj, 'bg_blur')) && !bgBlurValid) {
                    this.isLoading = false
                } else {
                    this.isLoading = false
                }
            },
            toggleIsDragOver(value) {
                this.isDragOver = value
            },
            async sendRequestImg(formData) {
                if (await fetchToken() === true) {
                    axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.api_url}`, formData, { headers: getHeaders() })
                    .then(response => {
                        console.log(response);
                        this.isLoading = false;
                        this.loadedFile = true;
                        this.fileNameResponse = response.data.name;
                        this.fileSrc = response.data.image;
                        this.image_upload = "";
                    })
                    .catch(error => {
                        const inputFile = this.$refs.imageUploadInput;
                        console.error(error);
                        this.isLoading = false;
                        this.image_upload = error.response ? error.response.data.error : "An error occurred during the upload.";
                        let fileList = new DataTransfer();
                        const file = new File([formData.get('image')], this.fileName);
                        fileList.items.add(file);
                        inputFile.files = fileList.files;
                    });
                } else {
                    axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN + this.api_url}`, formData)
                    .then(response => {
                        console.log(response);
                        this.isLoading = false;
                        this.loadedFile = true;
                        this.fileNameResponse = response.data.name;
                        this.fileSrc = response.data.image;
                        this.image_upload = "";
                    })
                    .catch(error => {
                        const inputFile = this.$refs.imageUploadInput;
                        console.error(error);
                        this.isLoading = false;
                        this.image_upload = error.response ? error.response.data.error : "An error occurred during the upload.";
                        let fileList = new DataTransfer();
                        const file = new File([formData.get('image')], this.fileName);
                        fileList.items.add(file);
                        inputFile.files = fileList.files;
                    });
                }
            },
            handleDrop(event) {
                const input = this.$refs.imageUploadInput;
                const files = event.dataTransfer.files;
                if (files.length > 0) {
                    const file = files[0];
                    this.fileName = file.name;
                    this.fileSize = file.size;
                    const fileList = new DataTransfer();
                    fileList.items.add(file);
                    input.files = fileList.files;
                    this.checkIfThereAnyFile()
                }
                this.toggleIsDragOver(false);
            },
            checkIfThereAnyFile() {
                const input = this.$refs.imageUploadInput;
                if (input.files[0]) {
                    const file = input.files[0];
                    this.anyFiles = true
                    this.loadedFile = false
                    this.fileSrc = ""
                    this.fileName = file.name
                    this.fileSize = file.size
                }
            },
            async downloadImage() {
                const imageUrl = this.fileSrc;
                const response = await fetch(imageUrl);
                const imageBuffer = await response.arrayBuffer();
                const blob = new Blob([imageBuffer], { type: "image/jpeg" });
                const fileName = this.fileNameResponse
                const url = window.URL.createObjectURL(blob);
                const link = document.createElement("a");
                link.href = url;
                link.download = fileName;
                document.body.appendChild(link);
                link.click();
                window.URL.revokeObjectURL(url);
                document.body.removeChild(link);
            },
            uploadMoreFiles() {
                const input = this.$refs.imageUploadInput;
                input.value = '';
                this.anyFiles = false;
                this.loadedFile = false;
                this.fileName = "";
                this.fileSize = 0;
                this.fileSrc = "";
                this.fileNameResponse = "";
                this.image_upload = ""
            }
        }
    }
</script>

<style>
.upload_image_container {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    flex-direction: column;
    overflow-y: auto;
    overflow-x: hidden;
    gap: 20px;
    padding: 40px;
}

.error_text {
    color: #ff0000;
    overflow-wrap: anywhere;
    text-align: center;
}

#image_upload_block {
    width: 90%;
    height: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    border: 5px #ffffff5e dashed;
    border-radius: 20px;
    cursor: pointer;
    gap: 20px;
    transition: .3s;
}

#image_upload_block:hover {
    border: 5px #fff dashed;
}

#upload_button {
    border: none;
    color: #fff;
    border-radius: 10px;
    background: linear-gradient(to right, var(--first_color), var(--secondary_color), var(--first_color));
    background-position: 0 50%;
    text-transform: uppercase;
    background-size: 200px;
    cursor: pointer;
    padding: 10px;
    transition: .3s;
}

#upload_button:hover {
    background-position: 50% 100%;
}

#image_upload_btn {
    cursor: pointer;
    color: #fff;
}

#image_upload_btn::-webkit-file-upload-button {
    border: none;
    color: #fff;
    border-radius: 10px;
    background: linear-gradient(to right, var(--first_color), var(--secondary_color), var(--first_color));
    background-position: 0 50%;
    text-transform: uppercase;
    background-size: 200px;
    cursor: pointer;
    padding: 10px;
    transition: .3s;
}

#image_upload_btn::-webkit-file-upload-button:hover {
    background-position: 50% 100%;
}

.ready_image {
    width: 100%;
    height: 100%;
    border-radius: 20px;
}

#download_on_click:hover {
    background-color: var(--secondary_color)
}

@media (max-height: 420px) {
    #upload_button {
        padding: 5px;
    }

    #image_upload_block {
        height: 70%;
    }
}
</style>