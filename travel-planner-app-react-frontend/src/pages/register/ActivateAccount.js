import { Button, CircularProgress, Container, Input, TextField, Typography } from '@mui/material';
import React, { useEffect, useRef, useState } from 'react';
import { useParams } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../axios';
import Autocomplete, { createFilterOptions } from '@mui/material/Autocomplete'
import { toast } from 'react-toastify';

const ActivateAccount = () => {

    const [activationStatus, setActivationStatus] = useState("");
    const dataFetchedRef = useRef(false);
    const [loading, setLoading] = useState(true);
    const activationCode = useParams().code;

    const LoadStatus = () => {

        axiosInstance
            .get('/api/register/confirm/' + activationCode + '/')
            .then((res) => {
                setActivationStatus(res.data.message);
                setLoading(false);
            })
            .catch((err) => {
                console.log(err.response.data.message);
                setActivationStatus(err.response.data.message);
                setLoading(false);
            });

        return true;
    };

    useEffect(() => {

        if (dataFetchedRef.current) return;
        dataFetchedRef.current = true;

        LoadStatus();

    }, []);

    if (loading)
    {
        return <CircularProgress style={{ position: 'fixed', top: '50%', left: '50%', translate: '-50%' }}/>
    }

    return (
        <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }}>
          {activationStatus}
        </Typography>

        </Container>
        
    </>
    )

};

export default ActivateAccount;
