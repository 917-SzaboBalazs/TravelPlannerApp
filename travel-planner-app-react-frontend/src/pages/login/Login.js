import { Button, Container, Input, TextField, Typography } from '@mui/material';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../axios';
import Autocomplete, { createFilterOptions } from '@mui/material/Autocomplete'
import { toast } from 'react-toastify';

const Login = () => {

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();

        const errorMessages = validateFormData();

        if (errorMessages.length > 0)
        {
            toast.error(errorMessages[0].detail);
            return;
        }

        axiosInstance
            .post('api/token/', {
                username,
                password,
            })
            .then((res) => {
                navigate('/');
                toast.success("Logged in");

                localStorage.setItem('access_token', res.data.access);
                localStorage.setItem('refresh_token', res.data.refresh);

                axiosInstance.defaults.headers['Autorization'] = 'JWT ' + localStorage.getItem('access_token');
                window.location.reload();

            })
            .catch((err) => {
                toast.error(err.response.data.detail);
            });
    };

    const handleReset = (event) => {
        event.preventDefault();
        toast.info("Cleared");

        setUsername("");
        setPassword("");
    };

    const validateFormData = () => {
        const errorMessages = [];
        
        return errorMessages;
    }

    return (
        <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }}>
          Login
        </Typography>
  
        <form onSubmit={handleSubmit} onReset={handleReset}>
            <Container maxWidth="md" >
                <p>Username</p>
                <Input type="text" name="username" value={username} onChange={(e) => setUsername(e.target.value)} fullWidth />

                <p>Password</p>
                <Input type="password" name="password" value={password} onChange={(e) => setPassword(e.target.value)} fullWidth />

                <Container align="center">
                    
                    <Button type="submit" variant="contained" sx={{ m: 1 }}>Login</Button>
                    <Button type="reset" variant="outlined" sx={{ m: 1 }}>Clear</Button>

                </Container>
            </Container>
        </form>

        </Container>
        
    </>
    )

};

export default Login;
