<?php

setcookie("nonce", null, -1);
setcookie("userid", null, -1);
setcookie("sign", null, -1);

header('Location: /');

?>
