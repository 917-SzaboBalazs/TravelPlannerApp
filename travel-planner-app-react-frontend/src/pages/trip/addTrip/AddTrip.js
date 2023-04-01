import { Button, Container, Input, Typography } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../../axios';
import MultipleSelectChip from '../../../components/trip/MultipleSelectChip';


const AddTrip = () => {

    const [name, setName] = useState("");
    const [destination, setDestination] = useState("");
    const [startDate, setStartDate] = useState(undefined);
    const [endDate, setEndDate] = useState(undefined);
    const [budget, setBudget] = useState(undefined);
    const [notes, setNotes] = useState("");

    const [accommodations, setAccommodations] = useState([]);
    const [selectedAccommodations, setSelectedAccommodations] = React.useState([]);

    const navigate = useNavigate();

    const handleSelectedAccommodations = (accommodations) => {
        setSelectedAccommodations(accommodations);
    }

    useEffect(() => {
        LoadAccommodations();
    }, []);

    const LoadAccommodations = () => {
        axiosInstance
            .get('accommodations/')
            .then((res) => {
                setAccommodations(res.data);
            })
            .catch((err) => {
                alert(err);
            })
    };

    const handleSubmit = (event) => {
        event.preventDefault();

        const accommodationIds = [];

        for (var i = 0; i < selectedAccommodations.length; i++)
        {
            const index = accommodations.map(el => el.name).indexOf(selectedAccommodations[i]);
            const id = accommodations[index].id;
            accommodationIds.push(id);
        }
        
        
        axiosInstance
            .post('trips/', {
                name,
                destination,
                'start_date': startDate,
                'end_date': endDate,
                budget,
                notes,
                accommodations: accommodationIds,
            })
            .then(() => {

                navigate("/trips/");
            })
            .catch((err) => {
                console.log(err);
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
        setSelectedAccommodations([]);
    };

    return (
        <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }}>
          Add Trip
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

                <p>Accommodations</p>
                <MultipleSelectChip selected={selectedAccommodations} change={handleSelectedAccommodations}
                                    categoryName="Accommodations" 
                                    options={accommodations.map((item) => item.name)} />

                <Container align="center">
                    
                    <Button type="submit" variant="contained" sx={{ m: 1 }}>Create Trip</Button>
                    <Button type="reset" variant="outlined" sx={{ m: 1 }}>Clear</Button>

                </Container>
            </Container>
        </form>

        </Container>
        
    </>
    )
  }; 
  export default AddTrip;