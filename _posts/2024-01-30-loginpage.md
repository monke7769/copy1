---
toc: False
comments: True
layout: post
title: Login Page
description: toby
type: hacks
courses: {'compsci': {'week': 20}}
---
<form action="javascript:login_user()">
    <p><label>
        User ID:
        <input type="text" name="uid" id="uid" required="" />
    </label></p>
    <p><label>
        Password:
        <input type="password" name="password" id="password" required="" />
    </label></p>
    <p>
        <button>Login</button>
    </p>
</form>
<!--
Below JavaScript code is designed to handle user authentication in a web application. It's written to work with a backend server that uses JWT (JSON Web Tokens) for authentication.
The script defines a function when the page loads. This function is triggered when the Login button in the HTML form above is pressed.
 -->
<script>
    // uri variable and options object are obtained from config.js
    function login_user(){
        // Set Authenticate endpoint
        const url = 'http://127.0.0.1:8086/api/users/authenticate';
        // Set the body of the request to include login data from the DOM
        const body = {
            uid: document.getElementById("uid").value,
            password: document.getElementById("password").value,
        };
        // Change options according to Authentication requirements
        const authOptions = {
            mode: 'cors', // no-cors, *cors, same-origin
            credentials: 'include', // include, same-origin, omit
            headers: {
                'Content-Type': 'application/json',
            },
            method: 'POST', // Override the method property
            cache: 'no-cache', // Set the cache property
            body: JSON.stringify(body)
        };
        // Fetch JWT
        fetch(url, authOptions)
        .then(response => {
            // handle error response from Web API
            if (!response.ok) {
                const errorMsg = 'Login error: ' + response.status;
                console.log(errorMsg);
                alert("Failed Authentication: Credentials Incorrect")
                return;
            }
            // Success!!!
            // Redirect to the database page
            window.location.href = "http://0.0.0.0:4800/copy1//2024/01/30/Users.html";
        })
        // catch fetch errors (ie ACCESS to server blocked)
        .catch(err => {
            console.error(err);
        });
    }
    // Attach login_user to the window object, allowing access to form action
    window.login_user = login_user;
</script>