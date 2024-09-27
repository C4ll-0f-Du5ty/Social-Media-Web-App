import './App.css'

import Nav from './NavBar/Nav.jsx'
import Landing from './landingPage/landingPage.jsx'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './Authentication/Login/login.jsx'
import Register from './Authentication/Register/register.jsx'
import { AuthProvider } from './Context/AuthContext.jsx'
import PrivateRoute from './Private/privateRoute.jsx'
import Profile from './Authentication/Profile/profile.jsx'
import ErrorRoute from './Private/Error.jsx'

import ProfilePage from './Authentication/Profile/ProfilePage.jsx'
import HomePage from './HomePage/HomePage.jsx'

// UI Error Handler
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';



function App() {
  return (
    <>


      <Router>
        <AuthProvider>
          <Nav />
          <Routes>
            <Route element={<ErrorRoute><Login /></ErrorRoute>} path='/login' />
            <Route path='/' index element={<Landing />} />
            {/* <Route element={<PrivateRoute><Profile /></PrivateRoute>} path="/profile/:username" /> */}
            <Route element={<PrivateRoute><Profile /></PrivateRoute>} path="/profile" />
            <Route element={<ErrorRoute><Register /></ErrorRoute>} path='/register' />


            <Route element={<PrivateRoute><ProfilePage /></PrivateRoute>} path='/profile/:username' />
            <Route element={<PrivateRoute><HomePage /></PrivateRoute>} path='/homepage' />

          </Routes>
        </AuthProvider >
      </Router >
      <ToastContainer />
    </>

  )
}

export default App
