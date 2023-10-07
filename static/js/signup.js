const signupButton = document.querySelector('.su-btn');
signupButton.addEventListener('click', function() {
        // Set the value of the is_login field to 0 (false) when the Sign Up button is clicked
        document.querySelector('#is_login').value = '0';
        });
// document.querySelector('#my_form').addEventListener('submit', function() {
//     // Submit the form
//     return true;
// }); 