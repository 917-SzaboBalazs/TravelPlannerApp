import { Container, ListItem, Typography } from '@mui/material';
import { List } from '@mui/material';
import React from 'react';
import { Link } from 'react-router-dom';
import './admin.css';

const Admin = () => {
    return (
      <>
        <Container maxWidth="xl" sx={{ height: '100%' }}>
        
        <Typography variant="h3" align="center" sx={{ m: 2 }}>
          Admin Page
        </Typography>
        
        <List className="admin-list">
            <ListItem align="center" sx={{ display: 'block' }}>
                <Link to="users/">
                    Manage Users
                </Link>
                
            </ListItem>
        </List>

        </Container>
      </>
    )
  };
  
  export default Admin;