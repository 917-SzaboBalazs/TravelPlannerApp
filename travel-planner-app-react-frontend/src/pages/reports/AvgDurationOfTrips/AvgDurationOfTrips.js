import { CircularProgress, Container, Typography } from '@mui/material';
import React, { useEffect, useRef, useState } from 'react';
import axiosInstance from '../../../axios';
import { toast } from 'react-toastify';


const AvgDurationOfTrips = () => {

    const dataFetchedRef = useRef(false);
    const [loading, setLoading] = useState(true);

    const [data, setData] = useState({
        'number_of_trips': 0,
        'average_duration': 0.
    });

    const LoadData = () => {
        axiosInstance
            .get('/reports/avg_duration_of_trips_in_days/')
            .then((res) => {
                setData(res.data);
                setLoading(false);
            })
            .catch((err) => {
                toast.error(err.response.data.detail);
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