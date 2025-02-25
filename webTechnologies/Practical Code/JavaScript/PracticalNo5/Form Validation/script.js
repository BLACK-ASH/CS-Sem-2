// handling submit event

// To Check Name
function checkName(name) {
    if (name.length < 3) {
        alert("Name should be at least 3 characters long");
        return false;
    }
    return true;
}

// To Check Email
function checkEmail(email) {
    // RegEx For Email
    let re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!re.test(email)) {
        alert("Invalid Email");
        return false;
    }
    return true;
}

// To Check Password
function checkPassword(password, confirmPassword) {
    if (password.length < 6) {
        alert("Password should be at least 6 characters long");
        return false;
    }

    if (password !== confirmPassword) {
        alert("Passwords do not match");
        return false;
    }
    return true;
}

// To Check Age
function checkAge(age) {
    if (age < 14) {
        alert("You must be at least 14 years old");
        return false;
    }
    return true;
}

myForm.addEventListener("submit", handleSubmit);
function handleSubmit(e) {
    e.preventDefault();
    let name = document.querySelector("#username").value;
    let email = document.querySelector("#email").value;
    let password = document.querySelector("#password").value;
    let confirmPassword = document.querySelector("#confirmPassword").value;
    let age = document.querySelector("#age").value;

    if (checkName(name) && checkEmail(email) && checkPassword(password, confirmPassword) && checkAge(age)) {
        alert("Form submitted successfully");
    }   

    // Reset Form
    name = "";
    email = "";
    password = "";
    confirmPassword = "";
    age = "";
}

