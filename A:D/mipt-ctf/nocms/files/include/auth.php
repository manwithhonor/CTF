<?php

require_once "config.php";
require_once "utils.php";

function is_authorized()
{
    if (isset($_COOKIE['userid']) && isset($_COOKIE['sign']) && isset($_COOKIE['nonce']))
    {
        $userid = $_COOKIE['userid'];
        $sign = $_COOKIE['sign'];
        $nonce = $_COOKIE['nonce'];

        $key = hash_hmac('md5', $hmac_password, $nonce);

        $correct_sign = hash_hmac('md5', $userid, $key);

        if ($correct_sign === $sign)
        {
            return true;
        }
    }

    return false;
}

function auth($login, $password)
{
    global $db_path;
    $db = new PDO("sqlite:".$db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    global $salt;
    $password = md5($salt . $password);

    $result = $db->prepare("select rowid from users where login=:login and password=:password");
    $result->execute(array(':login' => $login, ':password' => $password));

    $user = $result->fetch();
    if (!$user)
    {
        global $error_message;
        $error_message = "Invalid login/password";
        return false;
    }

    $userid = $user['rowid'];

    $nonce = random_str(32);

    $key = hash_hmac('md5', $hmac_password, $nonce);
    $sign = hash_hmac('md5', $userid, $key);

    setcookie("nonce", $nonce);
    setcookie("sign", $sign);
    setcookie("userid", $userid);
    return true;
}

function signup($login, $password)
{
    if (!((strlen($login) >= 3) && (strlen($login) <= 30) && preg_match("|^[A-Za-z0-9\-]+$|", $login)))
    {
        global $error_message;
        $error_message = "Invalid login (^[A-Za-z0-9-]{3,30}$)";
        return false;
    }

    global $db_path;
    $db = new PDO("sqlite:".$db_path);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $result = $db->prepare("select rowid from users where login=:login");
    $result->execute(array(':login' => $login));

    if ($result->fetch())
    {
        global $error_message;
        $error_message = "Login already registered";
        return false;
    }
    global $salt;
    $password = md5($salt . $password);
    $statement = $db->prepare("insert into users (login, password) values (:login, :password)");
    $statement->execute(array(':login' => $login, ':password' => $password));

    return true;
}

function get_login($userid)
{
    global $db_path;
    $db = new PDO("sqlite:".$db_path);
    $userid = preg_quote($userid, "()");
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $result = $db->query("select login from users where rowid=$userid");

    $login = $result->fetch();
    if (!$login)
    {
        return false;
    }

    return $login["login"];
}

function logout()
{
    setcookie("nonce", null, -1);
    setcookie("userid", null, -1);
    setcookie("sign", null, -1);
}

$is_auth = is_authorized();
if ($is_auth)
{
    $userid = $_COOKIE['userid'];
    $login = get_login($userid);
    if ($login === false)
    {
        logout();
        $is_auth = false;
    }
}

?>
