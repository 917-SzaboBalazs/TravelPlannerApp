import { Container, Typography } from '@mui/material';
import React, { useEffect, useState } from 'react';
import axiosInstance from '../../../axios';

const AvgDurationOfTrips = () => {

    const [data, setData] = useState({
        'number_of_trips': 0,
        'average_duration': 0.
    });

    const LoadData = () => {
        axiosInstance
            .get('/reports/avg_duration_of_trips_in_days/')
            .then((res) => {
                setData(res.data);
            })
            .catch((err) => {
                alert(err);
            })
    };

    useEffect(() => {
        LoadData();
    }, []);

    return (
      <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
            
            <Typography variant="h3" align="center" sx={{ m: 2 }}>
            Average duration of trips in days
            </Typography>

            <Typography align="center">
                <b>Number of Trips</b>: {data.number_of_trips} <br />
                <b>Average Duration</b>: {data.average_duration} days
            </Typography>
  
        </Container>
      </>
    )
  };
  
  export default AvgDurationOfTrips;