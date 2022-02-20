import React from 'react';

function Footer() {
    return(
        <div className="bg-dark p-2" style={{position: 'absolute', width: '100%', bottom: '0'}}>
            <div className="row col-12 d-flex justify-content-center text-white">
                <span className="h5">© 2022 copyright.</span>
            </div>
        </div>
    )
}
export default Footer;