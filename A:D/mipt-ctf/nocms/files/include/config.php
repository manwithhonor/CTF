<?php

$error_message = "Success";

function last_error()
{
    global $error_message;
    return $error_message;
}

$hmac_password = "ctf_sucks"; // change this password
$salt = "vWYG4ui23f1TuwerA";

$db_path = "/var/www/rw/db.sqlite3";

?>
