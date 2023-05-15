import axios from 'axios';

const baseURL = 'https://travel-planner-app.mooo.com/';
//const baseURL = 'http://127.0.0.1:8000/';
//const baseURL = 'http://35.202.17.84:8000/';

const axiosInstance = axios.create({
  
  baseURL: baseURL,
  headers: {
    Authorization: localStorage.getItem('access_token') ? 'JWT ' + localStorage.getItem('access_token') : null,
    'Content-Type': 'application/json',
    accept: 'application/json',
  },
});

export default axiosInstance;