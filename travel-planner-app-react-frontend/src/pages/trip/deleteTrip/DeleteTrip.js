import { Button, CircularProgress, Container, Typography } from '@mui/material';
import { Box } from '@mui/system';
import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import axiosInstance from '../../../axios';

const DeleteTripConfirmation = () => {

    const [loading, setLoading] = useState(true);

    const [name, setName] = useState("");
    const tripId = useParams().tripId;
    const navigate = useNavigate();

    const LoadTripName = () => {
        axiosInstance
            .get('/trips/' + tripId + '/')
            .then((res) => {
                setName(res.data.name);
                setLoading(false);
            })
            .catch((err) => {
                navigate('/404')
            })
    };

    useEffect(() => {
        LoadTripName();
    });

    const DeleteTrip = (event) => {
        event.stopPropagation();
    
        axiosInstance
          .delete('trips/' + tripId + '/')
          .then((res) => {
            
            navigate('/trips/');
    
          })
          .catch((err) => {
            alert(err);
          });
    
          
      };

    if (loading)
    {
        return <CircularProgress style={{ position: 'fixed', top: '50%', left: '50%', translate: '-50%' }}/>
    }

    return (
      <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
        
        <Typography variant="h4" align="center" sx={{ m: 2 }}>
          Are you sure that you want to delete Trip {name}?
        </Typography>

        <Box component="div" align="center">
                <Button
                    variant="contained"
                    onClick={DeleteTrip}
                    sx={{bgcolor: '#8b0000', ":hover": {bgcolor: '#9b0000'}}}
                >
                Yes
                </Button>
                <Button sx={{ m: 1 }}
                    variant="contained"
                    onClick={() => {navigate(-1)}}
                >
                No
                </Button>
            </Box>
  
        </Container>
      </>
    )
  };
  
  export default DeleteTripConfirmation;