---
toc: False
comments: True
layout: post
title: Create User
description: make user != toby
type: hacks
courses: {'compsci': {'week': 20}}
---
<form action="javascript:create_user()">
    <p><label>
        User ID:
        <input type="text" name="uid" id="uid" required="" />
    </label></p>
    <p><label>
        Password:
        <input type="password" name="password" id="password" required="" />
    </label></p>
    <p><label>
        Full Name:
        <input type="text" name="Name" id="Name" required="" />
    </label></p>
    <p><label>
        Favorite Ice Cream Flavor:
        <input type="text" name="icecream" id="icecream" required="" />
    </label></p>
    <p>
        <button>Create User</button>
    </p>
</form>

<!-- 
Below JavaScript code is designed to handle user authentication in a web application. It's written to work with a backend server that uses JWT (JSON Web Tokens) for authentication.

The script defines a function when the page loads. This function is triggered when the Login button in the HTML form above is pressed. 
 -->
<script type="module">
    // uri variable and options object are obtained from config.js


    function create_user(){
        // Set Authenticate endpoint
        const url ='http://127.0.0.1:8086/api/users/';

        // Set the body of the request to include login data from the DOM
        const body = {
            uid: document.getElementById("uid").value,
            password: document.getElementById("password").value,
            name: document.getElementById("Name").value,
            icecream: document.getElementById("icecream").value,
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
    window.create_user = create_user;
</script>