import { Button, Container, Input, Typography } from '@mui/material';
import React, { useEffect, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import axiosInstance from '../../../axios';
import MultipleSelectChip from '../../../components/trip/MultipleSelectChip';

const EditTrip = () => {

    const [name, setName] = useState("");
    const [destination, setDestination] = useState("");
    const [startDate, setStartDate] = useState(undefined);
    const [endDate, setEndDate] = useState(undefined);
    const [budget, setBudget] = useState(undefined);
    const [notes, setNotes] = useState("");

    const [accommodations, setAccommodations] = useState([]);
    const [selectedAccommodations, setSelectedAccommodations] = useState([]);

    const [transportations, setTransportations] = useState([]);
    const [selectedTransportations, setSelectedTransportations] = useState([]);

    const [activities, setActivities] = useState([]);
    const [selectedActivities, setSelectedActivities] = useState([]);


    const navigate = useNavigate();

    const handleSelectedAccommodations = (accommodations) => {
        setSelectedAccommodations(accommodations);
    };

    const handleSelectedTransformations = (transformations) => {
        setSelectedTransportations(transformations);
    };

    const handleSelectedActivities = (activities) => {
        setSelectedActivities(activities);
    };

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
                
                setSelectedAccommodations(res.data.accommodations.map(item => item.name));
                setSelectedTransportations(res.data.transportations.map(item => item.name));
                setSelectedActivities(res.data.activities.map(item => item.name));
            })
            .catch((err) => {
                alert(err);
            });
    };

    const LoadAccommodations = () => {
        axiosInstance
            .get('accommodations/')
            .then((res) => {
                setAccommodations(res.data);
            })
            .catch((err) => {
                alert(err);
            });
    };

    const LoadTransportations = () => {
        axiosInstance
            .get('transportations/')
            .then((res) => {
                setTransportations(res.data);
            })
            .catch((err) => {
                alert(err);
            });
    };

    const LoadActivities = () => {
        axiosInstance
            .get('activities/')
            .then((res) => {
                setActivities(res.data);
            })
            .catch((err) => {
                alert(err);
            });
    };

    useEffect(() => {
        LoadTrip();

        LoadAccommodations();
        LoadTransportations();
        LoadActivities();
    }, []);

    const handleSubmit = (event) => {
        event.preventDefault();

        const accommodationIds = [];

        for (let i = 0; i < selectedAccommodations.length; i++)
        {
            const index = accommodations.map(el => el.name).indexOf(selectedAccommodations[i]);
            const id = accommodations[index].id;
            accommodationIds.push(id);
        }

        const transportationIds= [];

        for (let i = 0; i < selectedTransportations.length; i++)
        {
            const index = transportations.map(el => el.name).indexOf(selectedTransportations[i]);
            const id = transportations[index].id;
            transportationIds.push(id);
        }
        
        const activityIds = [];

        for (let i = 0; i < selectedActivities.length; i++)
        {
            const index = activities.map(el => el.name).indexOf(selectedActivities[i]);
            const id = activities[index].id;
            activityIds.push(id);
        }
        
        axiosInstance
            .put('trips/' + tripId + '/', {
                name,
                destination,
                'start_date': startDate,
                'end_date': endDate,
                budget,
                notes,
                accommodations: accommodationIds,
                transportations: transportationIds,
                activities: activityIds,
            })
            .then(() => {
                navigate('/trips/' + tripId + '/');
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
        setSelectedAccommodations([]);
        setSelectedTransportations([]);
        setSelectedActivities([]);
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

                <p>Accommodations</p>
                <MultipleSelectChip selected={selectedAccommodations} change={handleSelectedAccommodations}
                                    categoryName="Accommodations" 
                                    options={accommodations.map((item) => item.name)} />

                <p>Transportations</p>
                <MultipleSelectChip selected={selectedTransportations} change={handleSelectedTransformations}
                                    categoryName="Transformations" 
                                    options={transportations.map((item) => item.name)} />

                <p>Activities</p>
                <MultipleSelectChip selected={selectedActivities} change={handleSelectedActivities}
                                    categoryName="Activities" 
                                    options={activities.map((item) => item.name)} />

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