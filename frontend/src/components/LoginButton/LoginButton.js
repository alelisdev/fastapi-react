import React from 'react';
import { useGoogleAuth } from './googleAuth';

const LoginButton = () => {

    const { signIn } = useGoogleAuth();

    return (
        <div>
            <button onClick={signIn}>Google Login</button>
        </div>
    );
};

export default LoginButton;