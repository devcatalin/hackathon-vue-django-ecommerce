import axios from "axios";

const axiosApi = axios.create({});

axiosApi.interceptors.request.use(
  config => {
    let token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default axiosApi;
