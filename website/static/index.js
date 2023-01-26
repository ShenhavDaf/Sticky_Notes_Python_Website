"use strict";

/* -------------------------------- Login modal -------------------------------- */
const loginModal = document.querySelector(".modal");
const closeLoginModalBtn = document.querySelector(".close-modal");
const overlay = document.querySelector(".overlay");

const openLoginModal = function () {
  loginModal.classList.remove("hidden");
  loginModal.classList.add("inline");
  overlay.classList.remove("hidden");
};

const closeLoginModal = function () {
  loginModal.classList.add("hidden");
  overlay.classList.add("hidden");
  // history.back();
};

closeLoginModalBtn.addEventListener("click", closeLoginModal);
overlay.addEventListener("click", closeLoginModal);

document.addEventListener("keydown", function (event) {
  if (event.key === "Escape" && !loginModal.classList.contains("hidden"))
    closeLoginModal();
});

/* -------------------------- show password eye (login) -------------------------- */
const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#passwordInput");

togglePassword.addEventListener("click", function (e) {
  // toggle the type attribute
  let type = password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);
  // toggle the eye slash icon
  this.classList.toggle("fa-eye-slash");
});

const toggleConfirm = document.querySelector("#toggleConfirmPassword");
const confirm = document.querySelector("#confirmPasswordInput");

toggleConfirm.addEventListener("click", function (e) {
  let type = confirm.getAttribute("type") === "password" ? "text" : "password";
  confirm.setAttribute("type", type);
  this.classList.toggle("fa-eye-slash");
});

/* -------------------------- Delete note -------------------------- */

function deleteNote(noteID) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ note_id: noteID }),
  }).then((_res) => {
    // reload / refresh the window
    window.location.href = "/";
  });
}
