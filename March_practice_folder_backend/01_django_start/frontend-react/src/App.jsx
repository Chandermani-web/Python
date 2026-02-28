import React from 'react';
import './assets/css/style.css';
import Header from './assets/components/Header';
import Main from './assets/components/Main';
import Footer from './assets/components/Footer';

const App = () => {
  return (
    <div className='bg-black text-white h-screen w-screen flex flex-col md:overflow-hidden relative'>
      <Header />
      <Main />
      <Footer />
    </div>
  )
}

export default App