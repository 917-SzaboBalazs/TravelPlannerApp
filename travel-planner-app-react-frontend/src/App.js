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

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="trips/" element={<Trips />} />
            <Route path="trips/add/" element={<AddTrip />} />
            <Route path="trips/:tripId/" element={<TripDetails />} />
            <Route path="trips/:tripId/edit/" element={<EditTrip />} />
            <Route path="trips/:tripId/delete/" element={<DeleteTripConfirmation />} />
            <Route path="*" element={<Page404 />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
