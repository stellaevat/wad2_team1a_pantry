const accepted_exts = ['bmp', 'cur', 'gif', 'png', 'apng', 'ico', 'jfif', 'jpe', 'jpg', 'jpeg', 'webp'];

// EDIT PROFILE PAGE
function validateProfilePicture() {
	var picture = document.getElementById("id_profile_picture").value;
	var clear = document.getElementById("clear-profile");
	var error = document.getElementById("picture-error");
	var errorRemove = document.getElementsByClassName("error-message");
	var successRemove = document.getElementsByClassName("success-message");

	if (picture != "") {
		var parts = picture.split(".");
		var ext = parts[parts.length - 1];
		
		if (!accepted_exts.includes(ext)) {
			for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
			for (i = 0; i < successRemove.length; i++) { successRemove[i].innerHTML = ""; }
			error.innerHTML = "<br />Invalid file format - please select an image.";
			document.getElementById("id_profile_picture").value = null;
			return false;
		} else {
			return true;
		}
	} else if (!clear.checked){
		for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
		for (i = 0; i < successRemove.length; i++) { successRemove[i].innerHTML = ""; }
		error.innerHTML = "No file chosen. To clear your profile picture please choose Clear.";
		return false;
	} else {
		return true;
	}
}

function validateUsername() {
	const usernamePattern = /^[\w.@+-]+$/;
	var username = document.getElementById("id_username").value;
	var error = document.getElementById('username-error');
	var errorRemove = document.getElementsByClassName("error-message");
	var successRemove = document.getElementsByClassName("success-message");
	
	if (!usernamePattern.test(username)) {
		for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
		for (i = 0; i < successRemove.length; i++) { successRemove[i].innerHTML = ""; }
		error.innerHTML = "Username may only contain letters, numbers, and @ . + - _ characters.";
		return false;
	} else {
		return true;
	}
}

function validatePassword() {
	var password = document.getElementById("id_new_password1").value;
	var confirmPassword = document.getElementById("id_new_password2").value;
	var error = document.getElementById('password-error');
	var errorRemove = document.getElementsByClassName("error-message");
	var successRemove = document.getElementsByClassName("success-message");
	
	if (password.length < 8) {
		for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
		for (i = 0; i < successRemove.length; i++) { successRemove[i].innerHTML = ""; }
		error.innerHTML = "New password too short - it must contain at least 8 characters.";
		return false;
	} else if (!isNaN(password)) {
		for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
		for (i = 0; i < successRemove.length; i++) { successRemove[i].innerHTML = ""; }
		error.innerHTML = "New password too simple - it must contain more than just numeric characters.";
		return false;
	} else if (password.toLowerCase() == username.toLowerCase()) {
		for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
		for (i = 0; i < successRemove.length; i++) { successRemove[i].innerHTML = ""; }
		error.innerHTML = "Username and new password too similar - try something different.";
		return false;
	} else if (password != confirmPassword) {
		for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
		for (i = 0; i < successRemove.length; i++) { successRemove[i].innerHTML = ""; }
		error.innerHTML = "New passwords don't match - please try again.";
		return false;
	} else {
		return true;
	}
}

function confirmAccountDelete() {
	var button = document.getElementById("del-account-btn");
	var label = document.getElementById("del-account-text");
	var warning = document.getElementById("del-warning");
	var errors = document.getElementsByClassName("error-message");
	var successes = document.getElementsByClassName("success-message");
	
	for (var i = 0; i < errors.length; i++) {
		errors[i].innerHTML = "";
	}
	for (var i = 0; i < successes.length; i++) {
		successes[i].innerHTML = "";
	}
	label.innerHTML = "Are you sure?";
	warning.innerHTML = "Deleting your account is permanent and cannot be undone. <br /> All of your data and recipes will be deleted."
	button.setAttribute("onclick", "delAccount()");
	button.setAttribute("focusout", "returnAccountNormal()");

	button.addEventListener("focusout", (event) => {
		returnAccountNormal();
	});
};

function returnAccountNormal() {
	var button = document.getElementById("del-account-btn");
	var label = document.getElementById("del-account-text");
	var warning = document.getElementById("del-warning");
	
	label.innerHTML = "Delete account";
	warning.innerHTML = "";
	button.setAttribute("onclick", "confirmAccountDelete()");
};

function delAccount(){
	window.location = "/pantry/user/" + username + "/account_deleted/";
}


// ADD RECIPE METHOD PAGE
function validateRecipePicture() {
	var picture = document.getElementById("recipe-pic-upload").value;
	var parts = picture.split(".");
	var ext = parts[parts.length - 1];
	var error = document.getElementById("picture-error");
	var errorRemove = document.getElementsByClassName("error-message");
		
	if (!accepted_exts.includes(ext)) {
		for (i = 0; i < errorRemove.length; i++) { errorRemove[i].innerHTML = ""; }
		error.innerHTML = "Invalid recipe picture - please select an image file.<br />";
		document.getElementById("recipe-pic-upload").value = null;
		return false;
	} else {
		return true;
	}
}


// SIGN UP PAGE
function validateCredentials() {
	const usernamePattern = /^[\w.@+-]+$/;
	
	var username = document.getElementById("id_username").value;
	var password = document.getElementById("id_password").value;
	var confirmPassword = document.getElementById("id_confirm_password").value;
	var error = document.getElementsByClassName('error-message')[0];
	
	if (!usernamePattern.test(username)) {
		error.innerHTML = "Username may only contain letters, numbers, and @ . + - _ characters.";
		return false;
	} else if (password.length < 8) {
		error.innerHTML = "Password too short - it must contain at least 8 characters.";
		return false;
	} else if (!isNaN(password)) {
		error.innerHTML = "Password too simple - it must contain more than just numeric characters.";
		return false;
	} else if (password.toLowerCase() == username.toLowerCase()) {
		error.innerHTML = "Username and password too similar - try something different.";
		return false;
	} else if (password != confirmPassword) {
		error.innerHTML = "Passwords don't match - please try again.";
		return false;
	} else {
		return true;
	}
}


// RECIPE PAGE
function star() {
	$.ajax({
		url: 'star/' + username,
		data: {
			'recipe_name_slug': recipe_name_slug,
			'username' : username
		},
		dataType: 'json',
		success: function () {
			var button = document.getElementById("star-btn");
			var icon = document.getElementById("star-icon");
			var text = document.getElementById("star-text");
			var counter = document.getElementById("starinfo");
	
			icon.innerHTML = '<i class="fa-solid fa-star fa-xs"></i>';
			text.innerHTML = 'Unstar';
			button.setAttribute('onclick','unstar()');
			counter.innerHTML++;
		}
	});
};

function unstar() {
	$.ajax({
		url: 'unstar/' + username,
		data: {
			'recipe_name_slug': recipe_name_slug,
			'username' : username
		},
		dataType: 'json',
		success: function () {
			var button = document.getElementById("star-btn");
			var icon = document.getElementById("star-icon");
			var text = document.getElementById("star-text");
			var counter = document.getElementById("starinfo");

			icon.innerHTML = '<i class="fa-regular fa-star fa-xs"></i>';
			text.innerHTML = '&nbsp; Star';
			button.setAttribute('onclick','star()');
			counter.innerHTML--;
		}
	});
};

function confirmDelete() {
	var button = document.getElementById("del-btn");
	var text = document.getElementById("del-text");
	var icon = document.getElementById("del-icon");
	
	text.innerHTML = 'Are you sure?';
	button.id = "del-btn-ext";
	icon.id = "del-icon-ext";
	icon.innerHTML = '<i class="fa-solid fa-trash-can fa-inverse"></i>'
	text.id = "del-text-ext";
	button.setAttribute("onclick", "del()");
	button.setAttribute("focusout", "returnNormal()");

	button.addEventListener("focusout", (event) => {
		returnNormal();
	});
};

function returnNormal() {
	var button = document.getElementById("del-btn-ext");
	var text = document.getElementById("del-text-ext");
	var icon = document.getElementById("del-icon-ext");
	
	text.innerHTML = ' Delete';
	button.id = "del-btn";
	icon.id = "del-icon";
	icon.innerHTML = '<i class="fa-solid fa-trash-can"></i>'
	text.id = "del-text";
	button.setAttribute("onclick", "confirmDelete()");
};

function del(){
	$.ajax({
		url: 'delete_recipe/' + username + '/',
		data: {
			'recipe_name_slug': recipe_name_slug,
			'username' : username
		},
		dataType: 'json',
		success: function () {
			window.location = "/pantry/recipe_deleted/";
		}
	});
}


// SEARCH RESULTS PAGE
function searchPersist(){
	document.getElementById("search-bar-id").setAttribute("value", searched)
}

window.onload = searchPersist;


// SEARCH BY INGREDIENT & ADD RECIPE INGREDIENTS PAGES
function validateSelection() {
	var checkboxes = document.getElementsByClassName("checkbox");
	var selected = false;
	var error = document.getElementsByClassName('error-message')[0];
	
	for (i = 0; i < checkboxes.length; i++) {
		if (checkboxes[i].checked) {
			selected = true;
			break;
		}
	}
	
	if (!selected) {
		error.innerHTML = "You need to select at least one ingredient!";
		return false;
	} else {
		return true;
	}
}

//This has been slightly modified from w3schools.org
function renderCollapsible() {
	var collapsible = document.getElementsByClassName("collapsible");
	if (collapsible) {
		for (i = 0; i < collapsible.length; i++) {
			collapsible[i].addEventListener("click", function() {
				this.classList.toggle("collapsible-active");
				var collapsing = this.nextElementSibling;
				if (collapsing.style.display === "flex") {
					collapsing.style.display = "none";
				} else {
					collapsing.style.display = "flex";
				}
			});
		}
	}
}

window.onload = renderCollapsible;