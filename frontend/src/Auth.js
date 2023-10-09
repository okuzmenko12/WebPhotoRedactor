import axios from "axios"

export const fetchToken = async (func) => {
    try {
        await axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/token/verify/`, { 'token': localStorage.getItem('AuthToken') });
        if (func !== undefined) {
            func();
        }
        return true;
    } catch {
        try {
            await setNewToken();
            if (func !== undefined) {
                func();
            }
            return true;
        } catch {
            return false;
        }
    }
};

export const setNewToken = () =>{
    return (axios.post(`${process.env.VUE_APP_BACKEND_DOMAIN}/api/v1/auth/token/refresh/`, { 'refresh': localStorage.getItem('AuthRefreshToken')})
    .then(res => setLocalToken(res.data.access))
    .catch())
};

//Local tokens

export const setLocalToken = async (token) => {
    return localStorage.setItem('AuthToken', token)
};

export const setLocalRefreshToken = async (token) => {
    return localStorage.setItem('AuthRefreshToken', token)
};

export const getLocalToken = () => {
    return localStorage.getItem('AuthToken')
};

export const getLocalRefreshToken = () => {
    return localStorage.getItem('AuthRefreshToken')
};

//headers

export const getHeaders = async () => {
    return { 'Authorization': `Bearer ${getLocalToken()}` }
};