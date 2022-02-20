import React from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

function Header() {
    const navigate = useNavigate();

    const hanldeLogout = () => {
        if(localStorage.getItem('fastapitoken')){
            localStorage.setItem('fastapitoken', '');
        }
        navigate('/login');
    }

    const token = localStorage.getItem('fastapitoken');

    const authLinks = (
        <ul className="navbar-nav">
            <li className="nav-item">
                <a onClick={hanldeLogout} style={{color: 'white', cursor: 'pointer'}}>Logout</a>
            </li>
        </ul>
    );

    const Links = (
        <ul className="navbar-nav">
            <li className="nav-item" >
                <Link to={'/login'}>Login</Link>
            </li>  
        </ul>
    );

    return(
        <nav className="navbar navbar-expand-sm bg-dark navbar-dark">
            <div className="container-fluid">
                <h1 className='text-white'>
                    <i className="fas fa-code" /> React FastAPI
                 </h1>
                 <div>{ token ? authLinks : Links}</div>
            </div>
        </nav>
    )
}
export default Header;