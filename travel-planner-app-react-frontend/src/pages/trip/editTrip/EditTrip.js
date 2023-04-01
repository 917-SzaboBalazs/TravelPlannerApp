import { Button, Container, Input, Typography } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import axiosInstance from '../../../axios';

const EditTrip = () => {

    const [name, setName] = useState("");
    const [destination, setDestination] = useState("");
    const [startDate, setStartDate] = useState(undefined);
    const [endDate, setEndDate] = useState(undefined);
    const [budget, setBudget] = useState(undefined);
    const [notes, setNotes] = useState("");

    const navigate = useNavigate();

    const tripId = useParams().tripId;

    const LoadTrip = () => {
        axiosInstance
            .get('/trips/' + tripId + '/')
            .then((res) => {
                setName(res.data.name);
                setDestination(res.data.destination);
                setStartDate(res.data.start_date);
                setEndDate(res.data.end_date);
                setBudget(res.data.budget);
                setNotes(res.data.notes);
            })
            .catch((err) => {
                alert(err);
            });
    };

    useEffect(() => {
        LoadTrip();
    }, []);

    const handleSubmit = (event) => {
        event.preventDefault();
        
        axiosInstance
            .put('trips/' + tripId + '/', {
                name,
                destination,
                'start_date': startDate,
                'end_date': endDate,
                budget,
                notes,
            })
            .then(() => {
                navigate(-1);
            })
            .catch((err) => {
                alert(err);
            });
    };

    const handleReset = (event) => {
        event.preventDefault();

        setName("");
        setDestination("");
        setStartDate(undefined);
        setEndDate(undefined);
        setBudget(undefined);
        setNotes("");
    };

    return (
        <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }}>
          Edit Trip {name}
        </Typography>
  
        <form onSubmit={handleSubmit} onReset={handleReset}>
            <Container maxWidth="md" >
                <p>Name*</p>
                <Input type="text" name="name" value={name} onChange={(e) => setName(e.target.value)} fullWidth required />

                <p>Destination</p>
                <Input type="text" name="destination" value={destination} onChange={(e) => setDestination(e.target.value)} fullWidth />

                <p>Start date</p>
                <Input type="date" name="start_date" value={startDate ? startDate : ""} onChange={(e) => setStartDate(e.target.value)} fullWidth />

                <p>End date</p>
                <Input type="date" name="end_date" value={endDate ? endDate : ""} onChange={(e) => setEndDate(e.target.value)} fullWidth />

                <p>Budget</p>
                <Input type="number" name="budget" value={budget ? budget : ""} onChange={(e) => setBudget(e.target.value)} fullWidth />

                <p>Notes</p>
                <textarea name="notes" rows="10" value={notes} onChange={(e) => setNotes(e.target.value)} style={{width: '100%'}} />

                <Container align="center">
                    
                    <Button type="submit" variant="contained" sx={{ m: 1 }}>Edit Trip</Button>
                    <Button type="reset" variant="outlined" sx={{ m: 1 }}>Clear</Button>

                </Container>
            </Container>
        </form>

        </Container>
        
    </>
    )
  }; 
  export default EditTrip;