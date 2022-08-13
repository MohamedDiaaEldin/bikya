import { fetchRequest } from "./FetchRequest.js";
import { buildEmptyFields } from "./HandelErrors.js";
import { isValidLoginInput } from "./ValidateInput.js";
import { displayErrorAtElement } from "./HandelErrors.js";

const loginBtn = document.getElementById("loginBtn");
const email = document.getElementById("email");
const password = document.getElementById("password");
const signupBtn = document.getElementById("signupBtn");

/// user input validation
const loginClickHandler = () => {
  const customer = {
    email: email.value,
    password: password.value,
  };

  const validation = isValidLoginInput(customer);

  const errorElement = document.querySelector(".error");
  /// If there is empty fields
  if (validation.empty) {
    const errorMessage =
      "error: empty fields \n" + buildEmptyFields(validation.emptyFields);
    displayErrorAtElement(errorElement, errorMessage);
    return;
  }
  /// else
  /// make request with login data
  displayErrorAtElement(errorElement, "");

  fetchRequest("login", "POST", customer, false)
    .then((response) => {
      
      console.log(response.headers)
      if (!response.ok) {
        throw new Error(response.status);
      }

      // window.location.href = 'orders.html'
      
    })
    .catch((error) => {
      // if user unauthorized
      if (error.message === "401")
        displayErrorAtElement(errorElement, "wrong email or password");
    });
};
loginBtn.addEventListener("click", loginClickHandler);

// sign up click listner
signupBtn.addEventListener("click", () => {
  document.location.href = "signup.html";
});
