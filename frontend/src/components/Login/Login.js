import React, {useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import { RiGoogleFill } from 'react-icons/ri';
import { GoogleLogin } from 'react-google-login';
import api from '../../actions/apiClient'

const clientId = '688665682012-gnodgapvpdm5l3j9hg3mlhp4pm2nqg03.apps.googleusercontent.com';

function Login() {
    const navigate = useNavigate();

    useEffect(() => {
        if(localStorage.getItem('fastapitoken'))
        {
            navigate('/dashboard');
        }
    // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [localStorage.getItem('fastapitoken')])

    const handleGoogleSuccess = async (data) => {
            await api.post('/signup/google', data)
        .then((res) => {
            console.log('res', res.data.jwtToken);
            localStorage.setItem('fastapitoken', res.data.jwtToken);
            navigate('/dashboard');
        })
        .catch((err) => {
            if (err.response === undefined) {
                console.log('something went wrong');
            } else {
                console.log(err.response.data);
            }
        });

    };

    const handleGoogleFailure = (err) => {
        console.log(err);
    };

    return(
        <div className="bg-white">
            <div className="col-md-6 m-auto mt-5 mb-5">
                <GoogleLogin
                clientId={clientId}
                buttonText="Login"
                onSuccess={handleGoogleSuccess}
                // uxMode={"redirect"}
                onFailure={handleGoogleFailure}
                cookiePolicy={'single_host_origin'}
                render={renderProps => (
                    <button
                    className="btn btn-primary"
                    onClick={renderProps.onClick}
                    // disabled={renderProps.disabled}
                    >
                    <div className="d-flex justify-content-center align-items-center">
                        <RiGoogleFill size={19} />
                        <span className="ml-2">Login with Google</span>
                    </div>
                    </button>
                )}
                />
            </div>
            
        </div>
    )
}
export default Login;