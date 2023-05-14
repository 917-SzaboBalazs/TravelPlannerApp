import React, { useEffect, useRef, useState } from 'react';
import axiosInstance from '../../../axios';
import { DataGrid } from '@mui/x-data-grid';
import Container from '@mui/material/Container';
import { Button, Checkbox, CircularProgress, Pagination, Typography, useMediaQuery } from '@mui/material';
import { Link, useNavigate } from "react-router-dom";
import { toast } from 'react-toastify';


const Users = () => {

  const dataFetchedRef = useRef(false);
  const navigate = useNavigate();
  const [loading, setLoading] = useState(true);
  const [pageLoading, setPageLoading] = useState(false);
  const [data, setData] = useState({});

  const [page, setPage] = useState(1);
  const [pageSize, setPageSize] = useState(100);
  const mobile = useMediaQuery('(max-width: 900px)');

  const mobileColumns = [
    { field: 'username', headerName: 'Username', width: 100 },
    { field: 'is_superuser', headerName: 'Admin', width: 60,
      renderCell: (params) => (
        <Checkbox
          checked={params.value}
          onChange={() => handleCheckboxChange(params.id, 'is_superuser', !params.value, setData)}
        />
      )
    },
    { field: 'is_staff', headerName: 'Moderator', width: 60,
      renderCell: (params) => (
        <Checkbox
          checked={params.value}
          onChange={() => handleCheckboxChange(params.id, 'is_staff', !params.value, setData)}
        />
      )
    },
    { field: 'is_active', headerName: 'Active', width: 60,
      renderCell: (params) => (
        <Checkbox
          checked={params.value}
          onChange={() => handleCheckboxChange(params.id, 'is_active', !params.value, setData)}
        />
      )
    },
  ];

  const columns = [
    { field: 'id', headerName: 'ID', width: 100 },
    { field: 'username', headerName: 'Username', width: 300 },
    { field: 'is_superuser', headerName: 'Admin', width: 100,
      renderCell: (params) => (
        <Checkbox
          checked={params.value}
          onChange={() => handleCheckboxChange(params.id, 'is_superuser', !params.value, setData)}
        />
      )
    },
    { field: 'is_staff', headerName: 'Moderator', width: 100,
      renderCell: (params) => (
        <Checkbox
          checked={params.value}
          onChange={() => handleCheckboxChange(params.id, 'is_staff', !params.value, setData)}
        />
      )
    },
    { field: 'is_active', headerName: 'Active', width: 100,
      renderCell: (params) => (
        <Checkbox
          checked={params.value}
          onChange={() => handleCheckboxChange(params.id, 'is_active', !params.value, setData)}
        />
      )
    },
  ];

  function handleCheckboxChange(id, field, value, setRows) {
    axiosInstance
    .patch(`/users/${id}/`, {
      [field]: value
    })
    .then(response => {
      // Update the rows array with the new value
      const updatedRows = data.map(row => {
        if (row.id === id) {
          return { ...row, [field]: value };
        } else {
          return row;
        }
      });
      setData(updatedRows);
    })
    .catch(error => {
      // Handle error
    });
  }
  

  const handlePageChange = ((_, value) => {
    setPageLoading(true);
    setPage(value);
  })

  const LoadUsers = (() => {

    const limit = 20;
    const offset = (page - 1) * limit;
    
    axiosInstance
      .get('users/?limit=' + limit + "&&offset=" + offset)
      .then((res) => {
        setData(res.data);
        
        setLoading(false);
        setPageLoading(false);
        dataFetchedRef.current = false;
    })
      .catch((err) => {

        toast.error(err.response.data.detail);

    });
  });

  useEffect(() => {
    if (dataFetchedRef.current) return;
    dataFetchedRef.current = true;

    LoadUsers();

  }, [page]);

  if (loading)
  {
      return <CircularProgress style={{ position: 'fixed', top: '50%', left: '50%', translate: '-50%' }}/>
  }

  return (
    <>
      <Container maxWidth="xl" sx={{ height: '100%'}}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }} >
          Users
        </Typography>

        {!pageLoading ?
          !mobile ?
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
            <DataGrid
              rows={data}
              columns={mobileColumns}
              initialState={{
                sorting: {
                  sortModel: [{ field: 'id', sort: 'desc' }],
                },
              }}
              autoHeight
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
          count={999999}
          page={page}
          onChange={handlePageChange}
          size='small'
          color='primary'
          variant='outlined'
          className='pagination'
          siblingCount={1}
          boundaryCount={1}
        />

        
      </Container>

    </>
  )
};
  
  export default Users;