<?php

require_once "../include/auth.php";
require_once "../include/utils.php";

$post_id = intval($_GET['id']);

render_page("../templates/viewpost.html", array("post_id" => $post_id));
