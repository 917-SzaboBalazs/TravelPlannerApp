import React, { useEffect, useRef, useState } from 'react';
import axiosInstance from '../../axios';
import { DataGrid } from '@mui/x-data-grid';
import Container from '@mui/material/Container';
import { Box, Button, CircularProgress, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, FormControl, InputLabel, MenuItem, Pagination, Select, Typography } from '@mui/material';
import { Link, useNavigate } from "react-router-dom";
import './trips.css'
import { toast } from 'react-toastify';


const Trips = () => {

  const dataFetchedRef = useRef(false);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [pageLoading, setPageLoading] = useState(false);

  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(100);
  const [data, setData] = useState([]);
  const [statistics, setStatistics] = useState({
    "avgBudget": 0,
    "nameOfLongestTrip": "",
  });
  const [action, setAction] = useState(0);
  const [selected, setSelected] = useState([]);

  const [openDialog, setOpenDialog] = useState(false);

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
    { field: 'name', headerName: 'Name', width: 500, 
      renderCell: (params) => (
      <Link to={`${params.id}/`} className='details-link'>{params.value}</Link>
    )
    },
    { field: 'username', headerName: 'User', width: 200,
      renderCell : (params) => (
        <Link to={`/user/${params.row.user_id}`} className='details-link'>{params.value}</Link>
      )
    },
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

  const handlePageChange = ((_, value) => {
    setPageLoading(true);
    setPage(value);
  })

  const LoadTrips = (() => {

    const limit = 20;
    const offset = (page - 1) * limit;
    
    axiosInstance
      .get('trips/?limit=' + limit + "&&offset=" + offset)
      .then((res) => {
        setData(res.data);
        calcAvgBudget(res.data);
        
        setLoading(false);
        setPageLoading(false);
        dataFetchedRef.current = false;
    })
      .catch((err) => {

        console.log(err);
        toast.error(err.response.data.detail);

    });
  });

  const handleActionsOnClick = () => {
    setOpenDialog(false);

    if (action === 1) {
      if (selected.length === 0) {
        toast.warning('Please select items to delete!');
        return;
      }
      else
      {
        handleOpenDialog();
      }
    }
  };

  const handleBulkDelete = () => {
    axiosInstance
      .delete('/trips/bulk_delete/', { data: { ids: selected } })
      .then((res) => {
        setSelected([]);
        setAction(0);
        toast.success('Items have been deleted successfully!');
        LoadTrips();
        setOpenDialog(false);
      })
      .catch((err) => {
        toast.error(err.response.data.detail);
        setOpenDialog(false);
      });
  }

  const handelSelectionChange = ((newSelection) => {
    setSelected(newSelection, ...selected);
  });

  const handleOpenDialog = () => {
    setOpenDialog(true);
  };

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
      <Container maxWidth="xl" sx={{ height: '100%', position: 'relative'}}>

      <Dialog open={openDialog} onClose={() => setOpenDialog(false)}>
        <DialogTitle>Are you sure you want to delete?</DialogTitle>
        <DialogContent>
          <DialogContentText>
            This action cannot be undone.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setOpenDialog(false)}>Cancel</Button>
          <Button onClick={handleBulkDelete}>Delete</Button>
        </DialogActions>
      </Dialog>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }} >
          Trips
        </Typography>

        <Button variant="contained" size="large" className="trips-add-button">
          <Link to="/trips/add/" className='add-link'>+ Add Trip</Link>
        </Button>

        <Box className="actions-container">
        <FormControl sx={{ m: 2, width: '200px' }}>
          <InputLabel id="actions-label">Actions</InputLabel>
          <Select
            labelId="actions-label"
            id="actions"
            label="Actions"
            value={action}
            onChange={(event) => setAction(event.target.value)}
          >
            <MenuItem value={1}>Delete Selected</MenuItem>
          </Select>
        </FormControl>

          <Button 
            variant="contained" sx={{ height: '40px', width: '70px' }}
            onClick={handleActionsOnClick}
          >
            Go</Button>
        </Box>

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
            checkboxSelection
            disableRowSelectionOnClick
            onRowSelectionModelChange={handelSelectionChange} 
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
          count={999999}
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