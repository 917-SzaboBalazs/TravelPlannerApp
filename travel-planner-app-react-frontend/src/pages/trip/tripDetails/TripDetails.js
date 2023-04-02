import { Typography, Button } from '@mui/material';
import { Box, Container } from '@mui/system';
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axiosInstance from '../../../axios';
import { useNavigate } from "react-router-dom";

const TripDetails = () => {

    const navigate = useNavigate();

    const tripId = useParams().tripId;
    const [details, setDetails] = useState({
        name: "",
        destination: "",
        start_date: undefined,
        end_date: undefined,
        budget: undefined,
        notes: "",
        accommodations: [],
        activities: [],
        transportations: [],
    });

    const LoadTrip = () => {
        axiosInstance
            .get('/trips/' + tripId + '/')
            .then((res) => {
                setDetails(res.data);
            })
            .catch((err) => {
                navigate('/404')
            });

        return true;
    };

    useEffect(() => {
        LoadTrip();
    }, []);

    return (
        <>
            <Container maxWidth="xl" sx={{ height: '100%'}}>

            <Box component="div" sx={{ display: 'block' }}>
                <Box component="div" sx={{ m: 2 }}>
                    <Typography variant="h4" align="center">
                    {details.name}
                    </Typography>

                    <Typography align="center">
                    {details.destination} | {details.start_date} - {details.end_date}
                    </Typography>
                </Box>

            </Box>

            <Box component="div" align="center" sx={{ m: 3 }}>
                    <Typography>
                    Budget: {details.budget}
                    </Typography>

                    <Typography>
                    Notes: {details.notes}
                    </Typography>

                    <Box component="div" align="center">
                        <Box component="div" align="center">
                            <h4>Accommodations</h4>
                            {details.accommodations.map((item) => <p key={item.id}>{item.name}</p>)}
                        </Box>

                        <Box component="div" align="center">
                            <h4>Transportations</h4>
                            {details.transportations.map((item) => <p key={item.id}>{item.name}</p>)}
                        </Box>

                        <Box component="div" align="center">
                            <h4>Activities</h4>
                            {details.activities.map((item) => <p key={item.id}>{item.name}</p>)}
                        </Box>
                    </Box>
            </Box>


            <Box component="div" align="center">
                <Button sx={{ m: 1 }}
                    variant="contained"
                    onClick={() => {navigate('edit/')}}
                >
                Edit
                </Button>
                <Button
                    variant="contained"
                    onClick={() => {navigate('delete/')}}
                    sx={{bgcolor: '#8b0000', ":hover": {bgcolor: '#9b0000'}}}
                >
                Delete
                </Button>
            </Box>
            
            </Container>
        </>
    )

  };
  
  export default TripDetails;