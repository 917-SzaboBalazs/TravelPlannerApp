import { Box, Container, ListItem, Typography } from '@mui/material';
import { List } from '@mui/material';
import React from 'react';
import { Link } from 'react-router-dom';
import './reports.css';

const Reports = () => {
    return (
      <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }}>
          Reports
        </Typography>
        
        <List className="report-list">
            <ListItem align="center" sx={{ display: 'block' }}>
                <Link to="average-duration-of-trips-in-days/">
                    Average Duration Of Trips In Days
                </Link>
                
            </ListItem>
        </List>

        </Container>
      </>
    )
  };
  
  export default Reports;