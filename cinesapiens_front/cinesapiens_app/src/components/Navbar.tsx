import { useState } from 'react'
import Logo from '../assets/images/preview-Photoroom.png'
import { AiOutlineBars, AiOutlineClose, AiOutlineRight } from 'react-icons/ai'

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false)

  const onHandleMenu = () => {
    setIsOpen(!isOpen)
  }

  return (
    <nav>
      <div className='flex items-center justify-between mx-4 text-white'>
        <div>
          <img src={Logo.src} alt='Logo' width='50' height='50' />
        </div>
        <div>
          <button onClick={onHandleMenu}>
            <AiOutlineBars width={36} height={36} className='text-xl' />
          </button>
        </div>
      </div>

      {/* Overlay Background */}
      <div
        className={`bg-black/50 fixed z-30 w-full h-screen top-0 right-0 transition-opacity duration-300 ${
          isOpen ? 'opacity-100' : 'opacity-0 pointer-events-none'
        }`}
      />

      {/* Sidebar Menu */}
      <div
        className={`bg-gradient-to-tr from-color-component-nav-2 to-color-component-nav1 fixed z-40 w-1/2 h-screen top-0 right-0 flex flex-col gap-4 p-6 transition-transform duration-300 ${
          isOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div className='h-5 flex items-center justify-between w-full'>
          <p className='font-bold font-montserratAlternates'>CineSapiens</p>
          <button onClick={onHandleMenu}>
            <AiOutlineClose className='text-xl' />
          </button>
        </div>
        <ul className='font-montserrat font-bold'>
          <li className='flex gap-2 items-center'>
            <AiOutlineRight />
            <a href='/'>Home</a>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default Navbar
