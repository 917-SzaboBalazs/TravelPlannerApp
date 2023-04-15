import { Button, Container, Input, TextField, Typography } from '@mui/material';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../../../axios';
import Autocomplete, { createFilterOptions } from '@mui/material/Autocomplete'


const AddTrip = () => {

    
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

    const LoadAccommodations = (accommodationFilter) => {
        
        if (accommodationFilter.length > 0)
        {
            axiosInstance
                .get('accommodations/?name_starts_with=' + accommodationFilter + "&&length=5")
                .then((res) => {
                    setAccommodations(res.data.results);
                })
                .catch((err) => {
                    alert(err);
                });
        }
        else
        {
            setAccommodations([]);
        }
    };

    const LoadTransportations = (transportationFilter) => {

        if (transportationFilter.length > 0)
        {
            axiosInstance
                .get('transportations/?name_starts_with=' + transportationFilter + "&&length=5")
                .then((res) => {
                    setTransportations(res.data.results);
                })
                .catch((err) => {
                    alert(err);
                });
        }
        else
        {
            setTransportations([]);
        }
    };

    const LoadActivities = (activityFilter) => {
        if (activityFilter.length > 0)
        {
            axiosInstance
                .get('activities/?name_starts_with=' + activityFilter + "&&length=5")
                .then((res) => {
                    setActivities(res.data.results);
                })
                .catch((err) => {
                    alert(err);
                });
        }
        else
        {
            setActivities([]);
        }
    };

    const validateFormData = () => {
        const errorMessages = [];

        if (name.length > 60)
        {
            errorMessages.push({"field": "name", "detail": "Maxiumum allowed length is 60 characters."});
        }

        if (destination.length > 60)
        {
            errorMessages.push({"field": "destination", "detail": "Maxiumum allowed length is 60 characters."});
        }

        if (startDate != undefined && endDate != undefined)
        {
            const startDateObject = Date.parse(startDate);
            const endDateObject = Date.parse(endDate);
    
            if (startDateObject > endDateObject)
            {
                errorMessages.push({"field": "endDate", "detail": "End date must be bigger or equal to start date."});
            }
        }

        if (budget < 0.)
        {
            errorMessages.push({"field": "budget", "detail": "Budget must be a non-negative number."});
        }

        if (notes.length > 500)
        {
            errorMessages.push({"field": "notes", "detail": "Maxiumum allowed length is 500 characters."});
        }

        if (selectedAccommodations.length > 10)
        {
            errorMessages.push({"field": "accommodations", "detail": "Maxiumum number of accommodations is 10."});
        }

        if (selectedTransportations.length > 10)
        {
            errorMessages.push({"field": "transportations", "detail": "Maxiumum number of transportations is 10."});
        }

        if (selectedActivities.length > 10)
        {
            errorMessages.push({"field": "activities", "detail": "Maxiumum number of activities is 10."});
        }

        return errorMessages;
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        const errorMessages = validateFormData();

        if (errorMessages.length > 0)
        {
            console.log(errorMessages);
            return;
        }
        
        axiosInstance
            .post('trips/', {
                name,
                destination,
                start_date: startDate,
                end_date: endDate,
                budget,
                notes,
                accommodations: selectedAccommodations.map(item => item.id),
                transportations: selectedTransportations.map(item => item.id),
                activities: selectedActivities.map(item => item.id),
            })
            .then(() => {
                navigate("/trips/");
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
                <Autocomplete
                    multiple
                    id="select-accommodations"
                    options={accommodations}
                    filterOptions={
                        createFilterOptions({
                            limit: 5,
                            stringify: (option) => option.name,
                        })
                    }
                    getOptionLabel={(option) => option.name}
                    onInputChange={(_, value) => LoadAccommodations(value)}
                    onChange={(_, values) => setSelectedAccommodations(values)}
                    renderInput={(params) => (
                    <TextField
                        {...params}
                        label="Accommodations"
                        placeholder="Select new accommodation"
                    />
                    )}
                    renderOption={(props, option) => {
                        return (
                            <li {...props} key={option.id}>
                                {option.name}
                            </li>
                        )
                    }}
                    isOptionEqualToValue={(option, value) => option.id === value.id}
                    value={selectedAccommodations}
                />

                <p>Transportations</p>
                <Autocomplete
                    multiple
                    id="select-transportations"
                    options={transportations}
                    filterOptions={
                        createFilterOptions({
                            limit: 5,
                            stringify: (option) => option.name,
                        })
                    }
                    getOptionLabel={(option) => option.name}
                    onInputChange={(_, value) => LoadTransportations(value)}
                    onChange={(_, values) => setSelectedTransportations(values)}
                    renderInput={(params) => (
                    <TextField
                        {...params}
                        label="Transportations"
                        placeholder="Select new transportation"
                    />
                    )}
                    renderOption={(props, option) => {
                        return (
                            <li {...props} key={option.id}>
                                {option.name}
                            </li>
                        )
                    }}
                    isOptionEqualToValue={(option, value) => option.id === value.id}
                    value={selectedTransportations}
                />

                <p>Activities</p>
                <Autocomplete
                    multiple
                    id="select-activities"
                    options={activities}
                    filterOptions={
                        createFilterOptions({
                            limit: 5,
                            stringify: (option) => option.name,
                        })
                    }
                    getOptionLabel={(option) => option.name}
                    onInputChange={(_, value) => LoadActivities(value)}
                    onChange={(_, values) => setSelectedActivities(values)}
                    renderInput={(params) => (
                    <TextField
                        {...params}
                        label="Activities"
                        placeholder="Select new activity"
                    />
                    )}
                    renderOption={(props, option) => {
                        return (
                            <li {...props} key={option.id}>
                                {option.name}
                            </li>
                        )
                    }}
                    isOptionEqualToValue={(option, value) => option.id === value.id}
                    value={selectedActivities}
                />

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