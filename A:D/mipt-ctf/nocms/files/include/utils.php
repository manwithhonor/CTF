<?php

require_once "config.php";

function random_str($length, $keyspace = '0123456789abcdef')
{
    $pieces = [];
    $max = mb_strlen($keyspace, '8bit') - 1;
    for ($i = 0; $i < $length; ++$i) {
        $pieces []= $keyspace[random_int(0, $max)];
    }
    return implode('', $pieces);
}

function get_posts($page = 1, $author = NULL)
{
    $page = $page-1;
    global $db_path;
    $db = new PDO("sqlite:".$db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    if ($author)
    {
        $query = "SELECT rowid, author, title, preview FROM posts WHERE author=$author ORDER BY rowid DESC LIMIT 10 OFFSET $page*10";
    } else {
        $query = "SELECT rowid, author, title, preview FROM posts ORDER BY rowid DESC LIMIT 10 OFFSET $page*10";
    }
    $result = $db->query($query);

    return $result->fetchAll();
}

function get_post($post_id)
{
    global $db_path;
    $db = new PDO("sqlite:".$db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $result = $db->query("SELECT author, title, preview, full FROM posts WHERE rowid = $post_id");

    return $result->fetch();
}

function upload_post($userid, $title, $preview, $full)
{
    if (strlen($title) == 0)
    {
        global $error_message;
        $error_message = "Title should not be empty";
        return false;
    }

    if (strlen($title) > 80)
    {
        global $error_message;
        $error_message = "Title too long (max. 80 chars)";
        return false;
    }

    if (strlen($preview) == 0)
    {
        global $error_message;
        $error_message = "Preview should not be empty";
        return false;
    }

    if (strlen($preview) > 200)
    {
        global $error_message;
        $error_message = "Preview too long (max. 200 chars)";
        return false;
    }

    if (strlen($full) == 0)
    {
        global $error_message;
        $error_message = "Fulltext should not be empty";
        return false;
    }

    if (strlen($full) > 400)
    {
        global $error_message;
        $error_message = "Fulltext too long (max. 400 chars)";
        return false;
    }

    global $db_path;
    $db = new PDO("sqlite:".$db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $statement = $db->prepare("insert into posts (author, title, preview, full) values (:author, :title, :preview, :full)");
    if ($userid < 1)
    {
        global $error_message;
        $error_message = "pashol hahui";
        return false;
	
    }
    $statement->execute(array(':author' => $userid, ':title' => $title, ':preview' => $preview, ':full' => $full));

    return true;
}

function render_page($path, $vars = array())
{
    foreach ($vars as $key => $value)
    {
        ${$key} = $value;
    }
    global $is_auth;
    global $login;
    global $userid;

    include "../templates/header.html";

    include $path;

    include "../templates/footer.html";
}

?>
