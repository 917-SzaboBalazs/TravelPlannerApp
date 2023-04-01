import React, { useEffect, useState } from 'react';
import axiosInstance from '../../axios';
import { DataGrid } from '@mui/x-data-grid';
import Container from '@mui/material/Container';
import { Button, Typography } from '@mui/material';
import { Link, useNavigate } from "react-router-dom";
import './trips.css'


const Trips = () => {

  const navigate = useNavigate();

  const [data, setData] = useState([]);
  const columns = [
    { field: 'id', headerName: 'ID', width: 70 },
    { field: 'name', headerName: 'Name', width: 200, 
      renderCell: (params) => (
      <Link to={`${params.id}/`} className='details-link'>{params.value}</Link>
    )
    },
    { field: 'destination', headerName: 'Destination', width: 200 },
    { field: 'start_date', headerName: 'Start Date', width: 100 },
    { field: 'end_date', headerName: 'End Date', width: 100 },
    { field: 'budget', headerName: 'Budget', width: 100 },
    { field: 'notes', headerName: 'Notes', width: 400 },
    { field: 'actions', headerName: '', sortable: false, width: 200, renderCell: (params) => {
      return (
        <>
          <Button sx={{ m: 1 }}
            variant="contained"
            onClick={() => {navigate(params.id + '/edit/')}}
          >
            Edit
          </Button>
          <Button
            variant="contained"
            onClick={() => {navigate(params.id + '/delete/')}}
            sx={{bgcolor: '#8b0000', ":hover": {bgcolor: '#9b0000'}}}
          >
            Delete
          </Button>
        </>
      );
      }}
  ];

  const LoadTrips = (() => {
    
    axiosInstance
      .get('trips/')
      .then((res) => {

        setData(res.data);

    })
      .catch((err) => {

        alert(err);

    });

  });

  useEffect(() => {

    LoadTrips();

  }, []);

  return (
    <>
      <Container maxWidth="xl" sx={{ height: '100%'}}>
        
      <Typography variant="h3" align="center" sx={{ m: 2 }}>
        Trips
      </Typography>

        <DataGrid sx={{ height: '500px' }}
          rows={data}
          columns={columns}
          pageSize={5}
          rowsPerPageOptions={[5]}
          checkboxSelection
        />

        <Button variant="text" sx={{ m: 2 }}>
          <Link to="/trips/add/" className='add-link'>+ Add Trip</Link>
        </Button>
      </Container>

    </>
  )
};
  
  export default Trips;