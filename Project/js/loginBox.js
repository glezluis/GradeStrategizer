
//login
//checks username entered is correct
function checkUser(){
	//get user input
	var user = document.getElementById( "username" ).value;
	if( user == "kjaing18" ){
		return true;
	}
	return false;
}

//checks password is correct
function checkPass(){
	var pass = document.getElementById( "password" ).value;
	if( pass == "1234" ){
		return true;
	}
	return false;
	
}

//if username/password is correct, login to dash
function goToDash(){
	var user = checkUser();
	var pass = checkPass();
	if( user == true && pass == true ){
		open( "html/Dashboard.html" );
	}
	else if( user == false || pass == false ){
		document.getElementById( "error" ).innerHTML = "Username or Password is incorrect.<br />Please enter again";
	}
	else{
		document.getElementById( "error" ).innerHTML = "Please enter again";
	}
}

//create an account
function openCreate(){
	open( "html/CreateLogin.html");
}

//forgot password
function openForgot(){
	open( "html/ForgotPassword.html" );
}



















