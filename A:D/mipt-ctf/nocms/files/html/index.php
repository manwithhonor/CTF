<?php

require_once "../include/auth.php";
require_once "../include/utils.php";

if (isset($_GET['page']))
{
    $page = intval($_GET['page']);
} else {
    $page = 1;
}

if (isset($_GET['author']))
{
    $author = intval($_GET['author']);
} else {
    $author = NULL;
}

render_page("../templates/feed.html", array("page" => $page, "author" => $author));

?>
