<?php

require_once "../include/auth.php";
require_once "../include/utils.php";

if (!$is_auth)
{
    if (isset($_POST['login']) && isset($_POST['password']))
    {
        $login = $_POST['login'];
        $password = $_POST['password'];
        $result = signup($login, $password);
        if ($result)
        {
            header("Location: /login.php");
            exit();
        } else {
            $error = last_error();
        }
    }
    render_page("../templates/register.html", array("error" => $error));
} else {
    header("Location: /");
    exit();
}

?>
