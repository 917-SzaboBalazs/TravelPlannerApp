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

function App() {
  return (
    <>
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
            
            <Route path="*" element={<Page404 />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
