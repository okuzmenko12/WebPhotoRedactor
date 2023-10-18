<template>
    <div @click="navbarToggle" id="mobile__btn"></div>
    <div @click="navbarToggle" id="mobile__btn_close">✖</div>
    <div @click="redirectToMain" id="close_modal" class="image_close_page" style="z-index: 4;">
            <svg height="15px" style="transform: rotate(180deg);" viewBox="0 0 5 9">
                <path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path>
            </svg>
            To Main
        </div>
    <div class="image_upload_head_container">
        <div class="image_upload_navbar">
            <div id="dd-dropdown">
                <div id="dd-arrow"><svg height="15px" viewBox="0 0 5 9"><path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path></svg>
                </div>
                <span v-if="isActive('#upscale')" id="dd-selected" @click="dropdownClick">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 21 21" fill="none">
                        <path d="M0 4.56165H16.2162V21" stroke="white" stroke-width="2"/>
                        <path d="M19.46 18.2603H3.24377V1.8219" stroke="white" stroke-width="2"/>
                        <path d="M3.50391 17.9945L20.0005 1" stroke="white" stroke-width="2"/>
                    </svg>
                    Upscale
                </span>
                <span v-else-if="isActive('#removebg')" id="dd-selected" @click="dropdownClick">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="13" viewBox="0 0 30 27" fill="none">
                        <path d="M27.5 26.3927H14.25M1 26.3927H8.5M14.25 26.3927H8.5M14.25 26.3927L22.3879 18.3927M8.5 26.3927L1 18.8927L11.6857 7.89271M22.3879 18.3927C22.3879 18.3927 26.3378 14.7503 29 11.8927C31.6622 9.03514 20.5 -1.10727 18 1.39272C15.5 3.8927 11.6857 7.89271 11.6857 7.89271M22.3879 18.3927L11.6857 7.89271" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                    </svg>
                    Remove background
                </span>
                <span v-else-if="isActive('#removejpegartifacts')" id="dd-selected" @click="dropdownClick">
                    <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22" fill="none">
                        <path d="M6.25584 8.23742C6.55519 7.31611 7.8586 7.3161 8.15795 8.23742L8.60043 9.59922C8.73431 10.0112 9.11826 10.2902 9.55149 10.2902H10.9834C11.9521 10.2902 12.3549 11.5298 11.5712 12.0992L10.4127 12.9409C10.0623 13.1955 9.9156 13.6469 10.0495 14.0589L10.4919 15.4207C10.7913 16.342 9.73682 17.1081 8.95311 16.5387L7.79468 15.6971C7.44419 15.4425 6.9696 15.4425 6.61911 15.6971L5.46069 16.5387C4.67698 17.1081 3.62249 16.342 3.92185 15.4207L4.36432 14.0589C4.4982 13.6469 4.35154 13.1955 4.00105 12.9409L2.84263 12.0992C2.05892 11.5298 2.46169 10.2902 3.43041 10.2902H4.8623C5.29553 10.2902 5.67949 10.0112 5.81336 9.59922L6.25584 8.23742Z" fill="white"/>
                        <path d="M15.4551 1.46353C15.6048 1.00287 16.2565 1.00287 16.4062 1.46353L16.8403 2.79967C16.9072 3.00568 17.0992 3.14516 17.3158 3.14516H18.7207C19.2051 3.14516 19.4065 3.76497 19.0146 4.04967L17.878 4.87546C17.7028 5.00278 17.6295 5.22846 17.6964 5.43447L18.1305 6.77062C18.2802 7.23128 17.753 7.61434 17.3611 7.32964L16.2245 6.50385C16.0493 6.37653 15.812 6.37653 15.6367 6.50385L14.5001 7.32964C14.1083 7.61434 13.581 7.23128 13.7307 6.77062L14.1649 5.43447C14.2318 5.22846 14.1585 5.00278 13.9832 4.87546L12.8466 4.04967C12.4548 3.76497 12.6562 3.14516 13.1405 3.14516H14.5454C14.762 3.14516 14.954 3.00568 15.021 2.79967L15.4551 1.46353Z" fill="white"/>
                        <path d="M16.9727 14.3601C17.1224 13.8994 17.7741 13.8994 17.9237 14.3601L18.3579 15.6962C18.4248 15.9022 18.6168 16.0417 18.8334 16.0417H20.2383C20.7227 16.0417 20.9241 16.6615 20.5322 16.9462L19.3956 17.772C19.2204 17.8993 19.147 18.125 19.214 18.331L19.6481 19.6672C19.7978 20.1278 19.2706 20.5109 18.8787 20.2262L17.7421 19.4004C17.5669 19.2731 17.3296 19.2731 17.1543 19.4004L16.0177 20.2262C15.6259 20.5109 15.0986 20.1278 15.2483 19.6672L15.6824 18.331C15.7494 18.125 15.676 17.8993 15.5008 17.772L14.3642 16.9462C13.9724 16.6615 14.1737 16.0417 14.6581 16.0417H16.063C16.2796 16.0417 16.4716 15.9022 16.5385 15.6962L16.9727 14.3601Z" fill="white"/>
                    </svg>
                    Remove JPEG artifacts
                </span>
                <span v-else id="dd-selected" @click="dropdownClick">
                    <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 21 21" fill="none">
                        <path d="M0 4.56165H16.2162V21" stroke="white" stroke-width="2"/>
                        <path d="M19.46 18.2603H3.24377V1.8219" stroke="white" stroke-width="2"/>
                        <path d="M3.50391 17.9945L20.0005 1" stroke="white" stroke-width="2"/>
                    </svg>
                    Upscale
                </span>
                <div v-if="isActive('#upscale')" id="dd-menu">
                        <router-link id="prbtn-2" class="profile_button align_center_text " :class="{ 'active': isActive('#removebg') }" to="#removebg">
                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="13" viewBox="0 0 30 27" fill="none">
                                <path d="M27.5 26.3927H14.25M1 26.3927H8.5M14.25 26.3927H8.5M14.25 26.3927L22.3879 18.3927M8.5 26.3927L1 18.8927L11.6857 7.89271M22.3879 18.3927C22.3879 18.3927 26.3378 14.7503 29 11.8927C31.6622 9.03514 20.5 -1.10727 18 1.39272C15.5 3.8927 11.6857 7.89271 11.6857 7.89271M22.3879 18.3927L11.6857 7.89271" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            </svg>
                            Remove background
                        </router-link>
                        <div class="hor-line payment_desc_hor_line"></div>
                        <router-link id="prbtn-3" class="profile_button align_center_text " :class="{ 'active': isActive('#removejpegartifacts') }" to="#removejpegartifacts">
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22" fill="none">
                                <path d="M6.25584 8.23742C6.55519 7.31611 7.8586 7.3161 8.15795 8.23742L8.60043 9.59922C8.73431 10.0112 9.11826 10.2902 9.55149 10.2902H10.9834C11.9521 10.2902 12.3549 11.5298 11.5712 12.0992L10.4127 12.9409C10.0623 13.1955 9.9156 13.6469 10.0495 14.0589L10.4919 15.4207C10.7913 16.342 9.73682 17.1081 8.95311 16.5387L7.79468 15.6971C7.44419 15.4425 6.9696 15.4425 6.61911 15.6971L5.46069 16.5387C4.67698 17.1081 3.62249 16.342 3.92185 15.4207L4.36432 14.0589C4.4982 13.6469 4.35154 13.1955 4.00105 12.9409L2.84263 12.0992C2.05892 11.5298 2.46169 10.2902 3.43041 10.2902H4.8623C5.29553 10.2902 5.67949 10.0112 5.81336 9.59922L6.25584 8.23742Z" fill="white"/>
                                <path d="M15.4551 1.46353C15.6048 1.00287 16.2565 1.00287 16.4062 1.46353L16.8403 2.79967C16.9072 3.00568 17.0992 3.14516 17.3158 3.14516H18.7207C19.2051 3.14516 19.4065 3.76497 19.0146 4.04967L17.878 4.87546C17.7028 5.00278 17.6295 5.22846 17.6964 5.43447L18.1305 6.77062C18.2802 7.23128 17.753 7.61434 17.3611 7.32964L16.2245 6.50385C16.0493 6.37653 15.812 6.37653 15.6367 6.50385L14.5001 7.32964C14.1083 7.61434 13.581 7.23128 13.7307 6.77062L14.1649 5.43447C14.2318 5.22846 14.1585 5.00278 13.9832 4.87546L12.8466 4.04967C12.4548 3.76497 12.6562 3.14516 13.1405 3.14516H14.5454C14.762 3.14516 14.954 3.00568 15.021 2.79967L15.4551 1.46353Z" fill="white"/>
                                <path d="M16.9727 14.3601C17.1224 13.8994 17.7741 13.8994 17.9237 14.3601L18.3579 15.6962C18.4248 15.9022 18.6168 16.0417 18.8334 16.0417H20.2383C20.7227 16.0417 20.9241 16.6615 20.5322 16.9462L19.3956 17.772C19.2204 17.8993 19.147 18.125 19.214 18.331L19.6481 19.6672C19.7978 20.1278 19.2706 20.5109 18.8787 20.2262L17.7421 19.4004C17.5669 19.2731 17.3296 19.2731 17.1543 19.4004L16.0177 20.2262C15.6259 20.5109 15.0986 20.1278 15.2483 19.6672L15.6824 18.331C15.7494 18.125 15.676 17.8993 15.5008 17.772L14.3642 16.9462C13.9724 16.6615 14.1737 16.0417 14.6581 16.0417H16.063C16.2796 16.0417 16.4716 15.9022 16.5385 15.6962L16.9727 14.3601Z" fill="white"/>
                            </svg>
                            Remove JPEG artifacts
                        </router-link>
                </div>
                <div v-else-if="isActive('#removebg')" id="dd-menu">
                        <router-link id="prbtn-1" class="profile_button align_center_text " :class="{ 'active': isActive('#upscale') }" to="#upscale">
                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 21 21" fill="none">
                                <path d="M0 4.56165H16.2162V21" stroke="white" stroke-width="2"/>
                                <path d="M19.46 18.2603H3.24377V1.8219" stroke="white" stroke-width="2"/>
                                <path d="M3.50391 17.9945L20.0005 1" stroke="white" stroke-width="2"/>
                            </svg>
                            Upscale
                        </router-link>
                        <div class="hor-line payment_desc_hor_line"></div>
                        <router-link id="prbtn-3" class="profile_button align_center_text " :class="{ 'active': isActive('#removejpegartifacts') }" to="#removejpegartifacts">
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22" fill="none">
                                <path d="M6.25584 8.23742C6.55519 7.31611 7.8586 7.3161 8.15795 8.23742L8.60043 9.59922C8.73431 10.0112 9.11826 10.2902 9.55149 10.2902H10.9834C11.9521 10.2902 12.3549 11.5298 11.5712 12.0992L10.4127 12.9409C10.0623 13.1955 9.9156 13.6469 10.0495 14.0589L10.4919 15.4207C10.7913 16.342 9.73682 17.1081 8.95311 16.5387L7.79468 15.6971C7.44419 15.4425 6.9696 15.4425 6.61911 15.6971L5.46069 16.5387C4.67698 17.1081 3.62249 16.342 3.92185 15.4207L4.36432 14.0589C4.4982 13.6469 4.35154 13.1955 4.00105 12.9409L2.84263 12.0992C2.05892 11.5298 2.46169 10.2902 3.43041 10.2902H4.8623C5.29553 10.2902 5.67949 10.0112 5.81336 9.59922L6.25584 8.23742Z" fill="white"/>
                                <path d="M15.4551 1.46353C15.6048 1.00287 16.2565 1.00287 16.4062 1.46353L16.8403 2.79967C16.9072 3.00568 17.0992 3.14516 17.3158 3.14516H18.7207C19.2051 3.14516 19.4065 3.76497 19.0146 4.04967L17.878 4.87546C17.7028 5.00278 17.6295 5.22846 17.6964 5.43447L18.1305 6.77062C18.2802 7.23128 17.753 7.61434 17.3611 7.32964L16.2245 6.50385C16.0493 6.37653 15.812 6.37653 15.6367 6.50385L14.5001 7.32964C14.1083 7.61434 13.581 7.23128 13.7307 6.77062L14.1649 5.43447C14.2318 5.22846 14.1585 5.00278 13.9832 4.87546L12.8466 4.04967C12.4548 3.76497 12.6562 3.14516 13.1405 3.14516H14.5454C14.762 3.14516 14.954 3.00568 15.021 2.79967L15.4551 1.46353Z" fill="white"/>
                                <path d="M16.9727 14.3601C17.1224 13.8994 17.7741 13.8994 17.9237 14.3601L18.3579 15.6962C18.4248 15.9022 18.6168 16.0417 18.8334 16.0417H20.2383C20.7227 16.0417 20.9241 16.6615 20.5322 16.9462L19.3956 17.772C19.2204 17.8993 19.147 18.125 19.214 18.331L19.6481 19.6672C19.7978 20.1278 19.2706 20.5109 18.8787 20.2262L17.7421 19.4004C17.5669 19.2731 17.3296 19.2731 17.1543 19.4004L16.0177 20.2262C15.6259 20.5109 15.0986 20.1278 15.2483 19.6672L15.6824 18.331C15.7494 18.125 15.676 17.8993 15.5008 17.772L14.3642 16.9462C13.9724 16.6615 14.1737 16.0417 14.6581 16.0417H16.063C16.2796 16.0417 16.4716 15.9022 16.5385 15.6962L16.9727 14.3601Z" fill="white"/>
                            </svg>
                            Remove JPEG artifacts
                        </router-link>
                </div>
                <div v-else-if="isActive('#removejpegartifacts')" id="dd-menu">
                        <router-link id="prbtn-1" class="profile_button align_center_text " :class="{ 'active': isActive('#upscale') }" to="#upscale">
                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15" viewBox="0 0 21 21" fill="none">
                                <path d="M0 4.56165H16.2162V21" stroke="white" stroke-width="2"/>
                                <path d="M19.46 18.2603H3.24377V1.8219" stroke="white" stroke-width="2"/>
                                <path d="M3.50391 17.9945L20.0005 1" stroke="white" stroke-width="2"/>
                            </svg>
                            Upscale
                        </router-link>
                        <div class="hor-line payment_desc_hor_line"></div>
                        <router-link id="prbtn-2" class="profile_button align_center_text " :class="{ 'active': isActive('#removebg') }" to="#removebg">
                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="13" viewBox="0 0 30 27" fill="none">
                                <path d="M27.5 26.3927H14.25M1 26.3927H8.5M14.25 26.3927H8.5M14.25 26.3927L22.3879 18.3927M8.5 26.3927L1 18.8927L11.6857 7.89271M22.3879 18.3927C22.3879 18.3927 26.3378 14.7503 29 11.8927C31.6622 9.03514 20.5 -1.10727 18 1.39272C15.5 3.8927 11.6857 7.89271 11.6857 7.89271M22.3879 18.3927L11.6857 7.89271" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            </svg>
                            Remove background
                        </router-link>
                </div>
                <div v-else id="dd-menu">
                        <router-link id="prbtn-2" class="profile_button align_center_text " :class="{ 'active': isActive('#removebg') }" to="#removebg">
                            <svg xmlns="http://www.w3.org/2000/svg" width="15" height="13" viewBox="0 0 30 27" fill="none">
                                <path d="M27.5 26.3927H14.25M1 26.3927H8.5M14.25 26.3927H8.5M14.25 26.3927L22.3879 18.3927M8.5 26.3927L1 18.8927L11.6857 7.89271M22.3879 18.3927C22.3879 18.3927 26.3378 14.7503 29 11.8927C31.6622 9.03514 20.5 -1.10727 18 1.39272C15.5 3.8927 11.6857 7.89271 11.6857 7.89271M22.3879 18.3927L11.6857 7.89271" stroke="white" stroke-width="2" stroke-linejoin="round"/>
                            </svg>
                            Remove background
                        </router-link>
                        <div class="hor-line payment_desc_hor_line"></div>
                        <router-link id="prbtn-3" class="profile_button align_center_text " :class="{ 'active': isActive('#removejpegartifacts') }" to="#removejpegartifacts">
                            <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 22 22" fill="none">
                                <path d="M6.25584 8.23742C6.55519 7.31611 7.8586 7.3161 8.15795 8.23742L8.60043 9.59922C8.73431 10.0112 9.11826 10.2902 9.55149 10.2902H10.9834C11.9521 10.2902 12.3549 11.5298 11.5712 12.0992L10.4127 12.9409C10.0623 13.1955 9.9156 13.6469 10.0495 14.0589L10.4919 15.4207C10.7913 16.342 9.73682 17.1081 8.95311 16.5387L7.79468 15.6971C7.44419 15.4425 6.9696 15.4425 6.61911 15.6971L5.46069 16.5387C4.67698 17.1081 3.62249 16.342 3.92185 15.4207L4.36432 14.0589C4.4982 13.6469 4.35154 13.1955 4.00105 12.9409L2.84263 12.0992C2.05892 11.5298 2.46169 10.2902 3.43041 10.2902H4.8623C5.29553 10.2902 5.67949 10.0112 5.81336 9.59922L6.25584 8.23742Z" fill="white"/>
                                <path d="M15.4551 1.46353C15.6048 1.00287 16.2565 1.00287 16.4062 1.46353L16.8403 2.79967C16.9072 3.00568 17.0992 3.14516 17.3158 3.14516H18.7207C19.2051 3.14516 19.4065 3.76497 19.0146 4.04967L17.878 4.87546C17.7028 5.00278 17.6295 5.22846 17.6964 5.43447L18.1305 6.77062C18.2802 7.23128 17.753 7.61434 17.3611 7.32964L16.2245 6.50385C16.0493 6.37653 15.812 6.37653 15.6367 6.50385L14.5001 7.32964C14.1083 7.61434 13.581 7.23128 13.7307 6.77062L14.1649 5.43447C14.2318 5.22846 14.1585 5.00278 13.9832 4.87546L12.8466 4.04967C12.4548 3.76497 12.6562 3.14516 13.1405 3.14516H14.5454C14.762 3.14516 14.954 3.00568 15.021 2.79967L15.4551 1.46353Z" fill="white"/>
                                <path d="M16.9727 14.3601C17.1224 13.8994 17.7741 13.8994 17.9237 14.3601L18.3579 15.6962C18.4248 15.9022 18.6168 16.0417 18.8334 16.0417H20.2383C20.7227 16.0417 20.9241 16.6615 20.5322 16.9462L19.3956 17.772C19.2204 17.8993 19.147 18.125 19.214 18.331L19.6481 19.6672C19.7978 20.1278 19.2706 20.5109 18.8787 20.2262L17.7421 19.4004C17.5669 19.2731 17.3296 19.2731 17.1543 19.4004L16.0177 20.2262C15.6259 20.5109 15.0986 20.1278 15.2483 19.6672L15.6824 18.331C15.7494 18.125 15.676 17.8993 15.5008 17.772L14.3642 16.9462C13.9724 16.6615 14.1737 16.0417 14.6581 16.0417H16.063C16.2796 16.0417 16.4716 15.9022 16.5385 15.6962L16.9727 14.3601Z" fill="white"/>
                            </svg>
                            Remove JPEG artifacts
                        </router-link>
                </div>
            </div>
        </div>
        <div class="image_upload_cont_container">
            <template v-if="isActive('#upscale')">
                <drop-n-drag :upscale_factor="upscaleFactor" :api_url="upscaleApiURL"/>
            </template>
            <template v-else-if="isActive('#removebg')">
                <drop-n-drag :bg_color="bgColor" :bgUrl="bgImgUrl" :bgFile="bgFileOrText" :output_type="outputType" :blur="bgBlur" @files-updated="handleFilesUpdated" api_url="/api/v1/images/remove_bg/"/>
            </template>
            <template v-else-if="isActive('#removejpegartifacts')">
                <drop-n-drag :strt="strenght" api_url="/api/v1/images/remove_jpeg_artifacts/"/>
            </template>
            <template v-else>
                <drop-n-drag api_url="/api/v1/images/upscale/"/>
            </template>
            <div id="profile_bar" class="profile_bar">
                <div v-if="isActive('#upscale')" class="profile_buttons image_buttons">
                    <div class="button_image_block" style="z-index: 2;">
                        <p>Upscale factor:</p>
                        <div id="factor-dropdown">
                            <div id="factor-arrow"><svg height="15px" viewBox="0 0 5 9"><path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path></svg>
                            </div>
                            <span id="factor-selected" @click="openFactorChoose">
                                {{upscaleFactor}}
                            </span>
                            <div id="factor-menu">
                                <li v-for="(factor, index) in factors" :key="index" @click="factorClick">
                                    {{ factor }}
                                </li>
                            </div>
                        </div>
                    </div>
                    <div class="button_image_block">
                        <input @change="toggleChecked('ultra_enhance')" :checked="isUltraEnhanceChecked" type="checkbox" name="enhancerType">
                        <p>ULTRA ENHANCER</p>
                    </div>
                    <div class="button_image_block">
                        <input @change="toggleChecked('ultra')" :checked="isUltraChecked" type="checkbox" name="enhancerType">
                        <p>ULTRA</p>
                    </div>
                </div>

                <div v-if="isActive('#removejpegartifacts')" class="profile_buttons image_buttons">
                    <div class="button_image_block" style="z-index: 2;">
                        <p>Strenght:</p>
                        <div id="factor-dropdown">
                            <div id="factor-arrow"><svg height="15px" viewBox="0 0 5 9"><path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path></svg>
                            </div>
                            <span id="factor-selected" @click="openFactorChoose">
                                {{strenght}}
                            </span>
                            <div id="factor-menu">
                                <li v-for="(strt, index) in jpegStrt" :key="index" @click="jpegstrtClick">
                                    {{ strt }}
                                </li>
                            </div>
                        </div>
                    </div>
                </div>

                <div v-if="isActive('#removebg')" class="profile_buttons image_buttons">
                    <div v-if="showColor === true" class="button_image_block">
                        <p>Background color:</p>
                        <div id="color-picker"></div>
                    </div>
                    <div v-if="showBg === true" class="button_image_block">
                        <p>Background image:</p>
                        <template v-if="bgFileOrText">
                            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" @click="openInputGUI" style="cursor: pointer" stroke-width='10px' viewBox="0 0 135 135" fill="none">
                                <path class="fill_obj" d="M11.5 99.5V10.5H124.5V93M11.5 99.5V109.5H124.5V93M11.5 99.5L42.5 61.5C52.2302 55.0949 57.4907 55.1456 67 61.5L90 91L101 81C106.771 77.0229 109.695 76.5457 114 81L124.5 93M1 1V134H134V1H1ZM96 49.5C102.874 48.5904 105.582 46.8445 106.5 39.5C105.9 31.7287 103.969 28.9576 96 28.5C87.8186 29.4879 86.0562 32.3313 85.5 39.5C86.9237 46.4436 89.351 48.5071 96 49.5Z" stroke="white"/>
                            </svg>
                        </template>

                        <template v-else>
                            <input-ui v-model="bgImgUrl"/>
                        </template>
                    </div>
                    <p v-if="bgFileOrText === true" class='link fs--12 no-top' style="cursor: pointer" @click="changeBgFile(false) ">Paste url</p>
                    <p v-else class='link fs--12 no-top' style="cursor: pointer" @click="changeBgFile(true)">Choose image</p>
                    <div class="button_image_block">
                        <p>BLUR</p>
                        %   
                        <input-ui :numberType="true" v-model="bgBlur" type="number" min="0" max="100" />
                    </div>
                    <div v-if="showBg === true && showColor === true" class="button_image_block" style="z-index: 2;">
                        <p>Ouput:</p>
                        <div id="factor-dropdown">
                            <div id="factor-arrow"><svg height="15px" viewBox="0 0 5 9"><path d="M0.419,9.000 L0.003,8.606 L4.164,4.500 L0.003,0.394 L0.419,0.000 L4.997,4.500 L0.419,9.000 Z" ></path></svg>
                            </div>
                            <span id="factor-selected" @click="openFactorChoose">
                                {{outputType}}
                            </span>
                            <div id="factor-menu">
                                <li v-for="(output, index) in outPuts" :key="index" @click="outputClick">
                                    {{ output }}
                                </li>
                            </div>
                        </div>
                    </div>
                    <button v-if="showBg === false || showColor === false" @click="resetSettings" id="upload_button">Reset settings</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import DropNDrag from "@/components/UI/DropNDrag.vue";
    import router from "@/router/router.js";
    import '@simonwep/pickr/dist/themes/nano.min.css';
    import Pickr from '@simonwep/pickr';
    import InputUi from "@/components/UI/InputUi.vue";
    import handlePopState from "@/utils/index.js";

    export default {
        components: {
            DropNDrag,
            InputUi
        },
        mounted() {
            handlePopState()
            if (document.getElementById('color-picker')) {
                this.$nextTick(() => {
                    this.loadChooseBgColor();
                });
            }
            this.factors = this.allUpscaleFactors
        },
        updated() {
            const dd = document.getElementById('dd-arrow');
            dd.classList.remove('active');
            if (document.getElementById('color-picker')) {
                this.$nextTick(() => {
                    this.loadChooseBgColor();
                });
            }
        },
        data() {
            return {
                allowedFormats: [ '.jpg', '.jpeg', '.png', '.tiff', '.tga' ],
                allUpscaleUltraFactors: [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ],
                allUpscaleFactors: [ 2, 4, 6, 8 ],
                factors: [],
                outPuts: [ 'cutout', 'mask' ],
                jpegStrt: [ 'normal', 'high', 'maximal' ],
                isUltraEnhanceChecked: false,
                isUltraChecked: false,
                isDragOver: false,
                anyFiles: false,
                bgFileExist: false,
                isLoading: false,
                loadedFile: false,
                fileName: "",
                bgColor: "#ffffff",
                upscaleFactor: 2,
                bgBlur: 0,
                bgFileOrText: true,
                outputType: "cutout",
                fileSize: 0,
                upscaleApiURL: "/api/v1/images/upscale/",
                showColor: true,
                strenght: "normal",
                bgImgUrl: "",
                showBg: true,
                fileSrc: ""
            }
        },
        watch: {
            bgColor() {
                setTimeout(() => {
                    this.changeBgState()
                }, 0)
            },
            bgFileExist() {
                setTimeout(() => {
                    this.changeColorState()
                }, 0)
            },
            bgImgUrl() {
                if (this.bgImgUrl.length > 1) {
                    this.changeColorState()
                }
            }
        },
        methods: {
            isActive(hash) {
                return this.$route.hash === hash;
            },
            resetSettings() {
                const input = document.querySelector('.bgImageUpload')
                this.showBg = true
                this.showColor = true
                this.bgImgUrl = ""
                if (this.bgColor !== "#ffffff" && document.querySelector('.pcr-button')) {
                    this.bgColor = "#ffffff"
                    document.querySelector('.pcr-button').style.setProperty('--pcr-color', this.bgColor);
                }

                input.value = ''
            },
            handleFilesUpdated() {
                this.bgFileExist = true
            },
            changeBgState() {
                this.showBg = false
            },
            changeColorState() {
                this.showColor = false
            },
            changeBgFile(value) {
                this.bgFileOrText = value
            },
            navbarToggle() { 
                    const navbar = document.getElementById('profile_bar')
                    const button = document.getElementById('mobile__btn')
                    const redirectBtn = document.getElementById('close_modal')
                    const closeButton = document.getElementById('mobile__btn_close')
                    redirectBtn.classList.toggle('visible')
                    navbar.classList.toggle('visible')
                    closeButton.classList.toggle('visible')
                    button.classList.toggle('hide')
            },
            redirectToMain() {
                router.push({ path: "/" })
            },
            dropdownClick() {
                const dd = document.getElementById('dd-arrow');
                const menu = document.getElementById('dd-menu');
                dd.classList.toggle('active');
                menu.classList.toggle('visible');
            },
            openFactorChoose() {
                const dd = document.getElementById('factor-arrow');
                const menu = document.getElementById('factor-menu');
                dd.classList.toggle('active');
                menu.classList.toggle('visible');
            },
            factorClick(event) {
                const dd = document.getElementById('factor-arrow');
                const menu = document.getElementById('factor-menu');
                if (event) {
                    const selectedFactor = event.target.textContent;
                    this.upscaleFactor = selectedFactor;
                    const factorItems = document.querySelectorAll('#factor-menu li');
                    factorItems.forEach(item => {
                        item.classList.remove('active');
                    });
                    event.target.classList.add('active');
                    dd.classList.remove('active');
                    menu.classList.remove('visible');
                }
            },
            outputClick(event) {
                const dd = document.getElementById('factor-arrow');
                const menu = document.getElementById('factor-menu');
                if (event) {
                    const selectedOutput = event.target.textContent;
                    this.outputType = selectedOutput;
                    const factorItems = document.querySelectorAll('#factor-menu li');
                    factorItems.forEach(item => {
                        item.classList.remove('active');
                    });
                    event.target.classList.add('active');
                    dd.classList.remove('active');
                    menu.classList.remove('visible');
                }
            },
            jpegstrtClick(event) {
                const dd = document.getElementById('factor-arrow');
                const menu = document.getElementById('factor-menu');
                if (event) {
                    const selectedStrt = event.target.textContent;
                    this.strenght = selectedStrt;
                    const factorItems = document.querySelectorAll('#factor-menu li');
                    factorItems.forEach(item => {
                        item.classList.remove('active');
                    });
                    event.target.classList.add('active');
                    dd.classList.remove('active');
                    menu.classList.remove('visible');
                }
            },
            openInputGUI() {
                const input = document.querySelector('.bgImageUpload')
                if (this.bgFileOrText === true) {
                    input.click()
                }
            },
            toggleChecked(option) {
                if (option === "ultra_enhance" && !this.isUltraEnhanceChecked) {
                    this.isUltraEnhanceChecked = true;
                    this.isUltraChecked = false;
                    this.upscaleFactor = 2
                    this.upscaleApiURL = `/api/v1/images/upscale/${option}/`;
                    this.factors = this.allUpscaleUltraFactors;
                } else if (option === "ultra" && !this.isUltraChecked) {
                    this.isUltraChecked = true;
                    this.isUltraEnhanceChecked = false;
                    this.upscaleApiURL = `/api/v1/images/upscale/${option}/`;
                    this.factors = this.allUpscaleUltraFactors;
                    this.upscaleFactor = 2
                } else {
                    this.isUltraEnhanceChecked = false;
                    this.isUltraChecked = false;
                    this.upscaleApiURL = "/api/v1/images/upscale/";
                    this.factors = this.allUpscaleFactors;
                    this.upscaleFactor = 2
                }
            },
            loadChooseBgColor() {
                if (this.isActive('#removebg')) {
                    const pickr = Pickr.create({
                        el: '#color-picker',
                        theme: 'nano',
                        default: '#ffffff',

                        swatches: [
                            '#FF0000',
                            '#E91E63',
                            '#9C27B0',
                            '#673AB7',
                            '#3F51B5',
                            '#000000',
                            '#ffffff',
                            '#009688',
                            '#4CAF50',
                            '#8BC34A',
                            '#CDDC39',
                            '#FFEB3B',
                            '#FFC107'
                        ],

                        components: {
                            preview: true,
                            opacity: false,
                            hue: true,

                            interaction: {
                                hex: true,
                                rgba: false,
                                hsla: false,
                                hsva: false,
                                cmyk: false,
                                input: true,
                                clear: true,
                                save: true
                            }
                        }
                    });
                    pickr.on('change', (...args) => {
                    let color = args[0].toHEXA();
                    document.querySelector('.pcr-button').style.setProperty('--pcr-color', color);
                    });
                    pickr.on('hide', (...args) => {
                        let color
                        if (args[0]._lastColor === null) {
                            color = '#ffffff'
                            this.bgColor = '#ffffff'
                        } else {
                            color = args[0]._lastColor.toHEXA();
                        }
                        document.querySelector('.pcr-button').style.setProperty('--pcr-color', color);
                        this.bgColor = `#${color[0]+ color[1] + color[2]}`
                    });
                    pickr.on('clear', () => {
                        this.bgColor = '#ffffff'
                        document.querySelector('.pcr-button').style.setProperty('--pcr-color', this.bgColor)
                    });
                    pickr.on('save', (...args) => {
                        if (args[0] !== null) {
                            let color = args[0].toHEXA();
                            this.bgColor = `#${color[0]+ color[1] + color[2]}`
                            console.log(args);
                            console.log(this.bgColor);
                        }
                    })
                }
            }
        }
    }
</script>

<style>
.image_upload_head_container {
    position: fixed;
    width: 100%;
    height: auto;
    display: flex;
    box-sizing: border-box;
    justify-content: left;
    align-items: center;
    flex-direction: column;
    z-index: 1;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background-color: #171921;
}

.image_upload_navbar {
    height: 65px;
    width: 100%;
    display: flex;
    background: #1b1e29;
    border-bottom: 1px solid #000;
    padding-left: 150px;
    padding-top: 20px;
    padding-bottom: 20px;
    align-items: center;
    z-index: 2;
    box-sizing: border-box;
}

.image_upload_cont_container {
    width: 100%;
    height: 100%;
    display: flex;
    box-sizing: border-box;
    justify-content: left;
    align-items: center;
}

.button_image_block input[type=checkbox] {
    -webkit-appearance: none;
    appearance: none;
    background-color: transparent;
    margin: 0;
    font: inherit;
    color: currentColor;
    width: 1.15em;
    height: 1.15em;
    border: 0.15em solid currentColor;
    border-radius: 0.15em;
    transform: translateY(-0.075em);
    cursor: pointer;
    display: grid;
    place-content: center;
}

.input-container input {
	color: #fff
}

.button_image_block input[type="checkbox"]::before {
    content: "";
    width: 0.65em;
    height: 0.65em;
    clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
    transform: scale(0);
    transition: .3s;
    box-shadow: inset 1em 1em var(--secondary_color);
    background-color: var(--secondary_color);
}

.button_image_block input[type="checkbox"]:checked::before {
    transform: scale(1);
}

.image_buttons {
    width: 80%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 70px 0 0 0;
}

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

.button_image_block {
    width: 100%;
    max-width: 100%;
    padding: 0 10px;
    box-sizing: border-box;
    background-color: #6161610a;
    backdrop-filter: blur(25px);
    border: 2px solid rgb(60, 59, 59);
    color: #fff;
    border-radius: 20px;
    display: flex;
    justify-content: space-between;
    text-align: center;
    align-items: center;
    gap: 10px;
}

#image_upload_block {
    width: 90%;
    height: 500px;
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

.width-auto {
    width: auto !important;
    max-width: 80% !important;
    height: auto !important;
    max-height: 80% !important;
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

#dd-dropdown {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 20px;
}

#dd-arrow {
    position: absolute;
    right: 10px;
    transform: rotate(90deg) translateX(130%);
    stroke: #fff;
}

#dd-arrow.active {
    transform: rotate(270deg) translateX(-90%) translateY(2px);
}

#dd-selected {
    background: #3b3f4d;
    padding: 10px 25px 10px 10px;
    border-radius: 15px;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    transition: .3s;
}

#dd-selected:hover {
    background: #4a4e5d;
}

#dd-menu {
    position: absolute;
    display: none;
    flex-direction: column;
    align-items: center;
    top: 50px;
    background: #3b3f4d;
    padding: 20px 40px;
    border-radius: 20px;
    gap: 20px;
}

#factor-dropdown {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 20px;
    width: 116px;
}

#factor-arrow {
    position: absolute;
    right: 10px;
    transform: rotate(90deg) translateX(130%);
    stroke: #fff;
}

#factor-arrow.active {
    transform: rotate(270deg) translateX(-90%) translateY(2px);
}

#factor-selected {
    background: #3b3f4d;
    padding: 10px 25px 10px 10px;
    border-radius: 15px;
    color: #fff;
    display: flex;
    align-items: center;
    gap: 10px;
    cursor: pointer;
    transition: .3s;
}

#factor-selected:hover {
    background: #4a4e5d;
}

#factor-menu {
    position: absolute;
    display: none;
    flex-direction: column;
    align-items: center;
    top: 50px;
    background: #3b3f4d;
    padding: 20px;
    border-radius: 20px;
    gap: 20px;
    list-style: none;
    color: #fff;
    max-height: 200px;
    overflow-y: auto;
    z-index: 2;
    overflow-x: hidden
}

#factor-menu li {
    padding: 10px 25px;
    border-radius: 10px;
    cursor: pointer;
    transition: .3s;
}

#factor-menu li:hover {
    background-color: #0000006b;
    scale: 110%
}

#factor-menu li.active {
    background-color: #0000006b;
    scale: 110%
}

@media (min-width: 768px) and (max-width: 991px) {
    .image_close_page {
        display: none
    }

    .image_upload_navbar {
        padding-left: 50px;
    }
}

@media (min-width: 651px) and (max-width: 767px) {
    .image_close_page {
        display: none
    }

    .image_upload_navbar {
        padding-left: 50px;
    }
}

@media (min-width: 481px) and (max-width: 650px) {
    .image_close_page {
        display: none
    }

    .image_upload_navbar {
        padding-left: 50px;
    }
}

@media (max-width: 480px) {
    .image_close_page {
        display: none
    }

    .image_upload_navbar {
        padding-left: 5px;
    }
}
</style>