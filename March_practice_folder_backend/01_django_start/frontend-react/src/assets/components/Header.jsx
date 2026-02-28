import React from 'react'
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <div className="text-white p-4 sm:p-6 z-10 relative">
      <nav className='flex justify-between items-center max-w-7xl mx-auto'>
        <Link to="/" className='text-xl sm:text-2xl text-white font-light'>STOCK PREDICTION PORTAL</Link>
        <div>
          <Link to="/login" className='text-sm sm:text-base text-white/80 hover:text-white px-3 sm:px-4 py-2 transition-colors'>Login</Link>
          <Link to="/register" className='text-sm sm:text-base text-white bg-white/10 hover:bg-white/20 px-4 sm:px-6 py-2 rounded transition-colors ml-2 sm:ml-4'>Register</Link>
        </div>
      </nav>
    </div>
  )
}

export default Header