import React, { useEffect, useRef, useState } from 'react';
import axiosInstance from '../../axios';
import { DataGrid } from '@mui/x-data-grid';
import Container from '@mui/material/Container';
import { Button, CircularProgress, Pagination, Typography } from '@mui/material';
import { Link, useNavigate } from "react-router-dom";
import './trips.css'
import { toast } from 'react-toastify';


const Trips = () => {

  const dataFetchedRef = useRef(false);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [pageLoading, setPageLoading] = useState(false);

  const [count, setCount] = useState(0);
  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(100);
  const [data, setData] = useState([]);
  const [statistics, setStatistics] = useState({
    "avgBudget": 0,
    "nameOfLongestTrip": "",
  });

  const calcAvgBudget = (data) => {
    var totalBudget = 0.;
    var idOfLongestTrip = 0;

    for (let i = 0; i < data.length; i++)
    {
      totalBudget += data[i].budget;
      let curr_end_date = new Date(data[i].end_date);
      let curr_start_date = new Date(data[i].start_date);
      
      let max_end_date = new Date(data[idOfLongestTrip].end_date);
      let max_start_date = new Date(data[idOfLongestTrip].start_date);

      if (curr_end_date - curr_start_date > max_end_date - max_start_date)
      {
        idOfLongestTrip = i;
      }
    }

    var avgBudget = data.length > 0 ? totalBudget / data.length : 0.;
    var nameOfLongestTrip = data[idOfLongestTrip].name;

    setStatistics({
      "avgBudget": avgBudget,
      "nameOfLongestTrip": nameOfLongestTrip,
    })
  }

  const columns = [
    { field: 'id', headerName: 'ID', width: 100 },
    { field: 'name', headerName: 'Name', width: 350, 
      renderCell: (params) => (
      <Link to={`${params.id}/`} className='details-link'>{params.value}</Link>
    )
    },
    { field: 'destination', headerName: 'Destination', width: 150 },
    { field: 'start_date', headerName: 'Start Date', width: 100 },
    { field: 'end_date', headerName: 'End Date', width: 100 },
    { field: 'budget', headerName: 'Budget', width: 80 },
    { field: 'number_of_accommodations', headerName: 'Accommodations', width: 130 },
    { field: 'number_of_transportations', headerName: 'Transportations', width: 130 },
    { field: 'number_of_activities', headerName: 'Activities', width: 130 },
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

  const handlePageChange = ((event) => {
    var pageNumber = 0;
    setPageLoading(true);

    if (event.target.dataset.testid === "NavigateNextIcon")
    {
      pageNumber = page + 1;
    }
    else if (event.target.dataset.testid === "NavigateBeforeIcon")
    {
      pageNumber = page - 1;
    }
    else
    {
      pageNumber = parseInt(event.target.outerText)
    }

    setPage(pageNumber);
  })

  const LoadTrips = (() => {
    
    axiosInstance
      .get('trips/?page=' + page)
      .then((res) => {
        setCount(res.data.count);
        setData(res.data.results);
        calcAvgBudget(res.data.results);
        
        setLoading(false);
        setPageLoading(false);
    })
      .catch((err) => {

        toast.error(err.response.data.detail);

    });

  });

  useEffect(() => {
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    LoadTrips();

  }, [page]);

  if (loading)
  {
      return <CircularProgress style={{ position: 'fixed', top: '50%', left: '50%', translate: '-50%' }}/>
  }

  return (
    <>
      <Container maxWidth="xl" sx={{ height: '100%'}}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }} >
          Trips
        </Typography>

        <Button variant="contained" size="large" className="trips-add-button">
          <Link to="/trips/add/" className='add-link'>+ Add Trip</Link>
        </Button>

        {!pageLoading ?
          <DataGrid sx={{ height: '600px' }}
            rows={data}
            columns={columns}
            initialState={{
              sorting: {
                sortModel: [{ field: 'id', sort: 'desc' }],
              },
            }}
            hideFooter
            components={{
              NoRowsOverlay: () => (
                <></>
              ),
            }}
          />
          :
          <DataGrid sx={{ height: '600px' }}
              rows={[]}
              columns={columns}
              hideFooter
              components={{
                NoRowsOverlay: () => (
                  <CircularProgress style={{ position: 'fixed', top: '50%', left: '50%', translate: '-50%' }}/>
                ),
              }}
            />
        }

        <Pagination
          count={Math.ceil(count / pageSize)}
          page={page}
          onChange={handlePageChange}
          color='primary'
          variant='outlined'
          className='pagination'
          siblingCount={2}
          boundaryCount={1}
        />

        {/*
        <Box variant="div">
          <Typography variant="h4" align='center' sx={{ mt: 2, mb: 1 }}>
            Page Statistics
          </Typography>

          <Typography align="center" sx={{ m: 1 }}>
            You have {data.length} trips
          </Typography>

          <Typography align="center" sx={{ m: 1 }}>
            Average budget: {statistics.avgBudget} euros
          </Typography>

          <Typography align="center" sx={{ m: 1 }}>
            Your longest trip is {statistics.nameOfLongestTrip}
          </Typography>
        </Box>
        */}

        
      </Container>

    </>
  )
};
  
  export default Trips;