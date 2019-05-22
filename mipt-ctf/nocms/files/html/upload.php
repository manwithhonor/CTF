<?php

require_once "../include/auth.php";
require_once "../include/utils.php";

if ($is_auth)
{
    if (isset($_POST['title']) && isset($_POST['preview']) && isset($_POST['full']))
    {
        $title = $_POST['title'];
        $preview = $_POST['preview'];
        $full = $_POST['full'];
        $result = upload_post($userid, $title, $preview, $full);
        if ($result)
        {
            header("Location: /");
            exit();
        } else {
            $error = $error_message;
        }
    }
    render_page("../templates/upload.html", array("error" => $error));
} else {
    header("Location: /login.php");
}

?>
