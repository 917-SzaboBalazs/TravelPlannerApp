import React from 'react';
import './css/layout.css'
import { Outlet, Link } from "react-router-dom";
import ResponsiveNavigationBar from '../components/layout/responsiveNavigationBar'

const Layout = () => {
  return (
    <>
      <ResponsiveNavigationBar />

      <Outlet />
    </>
  )
};

export default Layout;