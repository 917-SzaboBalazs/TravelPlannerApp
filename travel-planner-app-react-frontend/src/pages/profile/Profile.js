import React, { useEffect, useRef, useState } from 'react';
import axiosInstance from '../../axios';
import { Box, CircularProgress, Container, Typography } from '@mui/material';
import { useParams } from 'react-router-dom';

const Profile = () => {
    const [data, setData] = useState({});
    const [loading, setLoading] = useState(true);
    const dataFetchedRef = useRef(false);

    const userId = useParams().userId;

    const LoadData = () => {
        axiosInstance
            .get('/users/' + userId + '/profile/')
            .then((res) => {
                setData(res.data);
                setLoading(false);
            })
            .catch((err) => {
                console.log(err);
            })

        
    };

    useEffect(() => {
        if (dataFetchedRef.current) return;
        dataFetchedRef.current = true;
    
        LoadData();
    }, []);

    if (loading)
    {
        return <CircularProgress style={{ position: 'fixed', top: '50%', left: '50%', translate: '-50%' }}/>
    } 

    return (
        <>
          <Container maxWidth="x1" sx={{ height: '100%' }}>
            <Typography variant="h3" align="center" sx={{ m: 2 }} >
            Profile page
            </Typography>

            <Box component="div" align="center" sx={{ m: 3 }}>
                <Typography>
                Bio: {data.bio}
                </Typography>

                <Typography>
                Location: {data.location}
                </Typography>

                <Typography>
                Birthday: {data.birthday}
                </Typography>

                <Typography>
                Gender: {data.gender}
                </Typography>

                <Typography>
                Phone number: {data.phone_number}
                </Typography>
            </Box>
          </Container>
        </>
    )
}

export default Profile;