import React from 'react';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./pages/Layout";
import Home from "./pages/Home";
import Trips from "./pages/trip/Trips";
import Page404 from "./pages/Page404";
import TripDetails from './pages/trip/tripDetails/TripDetails';
import AddTrip from './pages/trip/addTrip/AddTrip';
import EditTrip from './pages/trip/editTrip/EditTrip';
import DeleteTripConfirmation from './pages/trip/deleteTrip/DeleteTrip';
import AvgDurationOfTrips from './pages/reports/AvgDurationOfTrips/AvgDurationOfTrips'
import Reports from './pages/reports/Reports';
import Profile from './pages/profile/Profile';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import Register from './pages/register/Register';
import ActivateAccount from './pages/register/ActivateAccount';
import Login from './pages/login/Login';
import Users from './pages/admin/users/users';
import Admin from './pages/admin/admin';
import Chat from './pages/chat/Chat';

function App() {
  return (
    <>
      <ToastContainer
          position="top-center"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="colored"
      />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />

            <Route path="trips/">
              <Route index element={<Trips />}/>
              <Route path="add/" element={<AddTrip />} />
              <Route path=":tripId/" element={<TripDetails />} />
              <Route path=":tripId/edit/" element={<EditTrip />} />
              <Route path=":tripId/delete/" element={<DeleteTripConfirmation />} />

            </Route>

            <Route path="reports/">
              <Route index element={<Reports />} />
              <Route path="average-duration-of-trips-in-days/" element={<AvgDurationOfTrips />} />

            </Route>

            <Route path="user/:userId/" element={<Profile />} />

            <Route path="register/">
              <Route index element={<Register />} />
              <Route path="confirm/:code/" element={<ActivateAccount />} />
            </Route>
            
            <Route path="login/" element={<Login />} />

            <Route path="admin/">
              <Route index element={<Admin />} />
              <Route path="users/">
                <Route index element={<Users />} />
              </Route>
            </Route>

            <Route path="chat/" element={<Chat />} />
            
            <Route path="*" element={<Page404 />} />
          </Route> 
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
