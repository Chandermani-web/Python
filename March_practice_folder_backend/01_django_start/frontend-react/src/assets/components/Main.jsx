import React from 'react'

const Main = () => {
  return (
    <div className='flex-1 relative'>
      {/* Background Image */}
      <div className='absolute inset-0'>
        <img 
          src="https://images.pexels.com/photos/7567550/pexels-photo-7567550.jpeg" 
          alt="Stock Market" 
          className='w-full h-full object-cover'
        />
        {/* Black Overlay */}
        <div className='absolute inset-0 bg-black/70'></div>        
        <div className='absolute inset-0 bg-blue-900/30'></div>        

      </div>
      
      {/* Content */}
      <div className='relative z-10 h-full flex items-center'>
        <div className='max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center sm:text-left'>
          <h1 className='text-3xl sm:text-4xl md:text-5xl font-light mb-4 sm:mb-6 leading-tight'>
            Welcome to Stock Prediction Portal
          </h1>
          <p className='text-base sm:text-lg text-white/80 max-w-3xl mx-auto sm:mx-0 mb-6 sm:mb-8 leading-relaxed'>
            This stock prediction application utilizes machine learning techniques, specifically employing Keras and LSTM models, integrated with the Django framework. It forecasts future stock prices by analyzing historical data patterns (100-day and 200-day moving averages), essential indicators widely used by stock analysts to inform trading and investment decisions.
          </p>
          <button className='bg-white text-black px-8 sm:px-12 py-3 sm:py-4 text-sm sm:text-base font-medium hover:bg-white/90 transition-colors rounded'>
            Get Started
          </button>
        </div>
      </div>
    </div>
  )
}

export default Main