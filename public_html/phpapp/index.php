<?php

define('DINC', 'inc/');
define('DBASE', 'baza');
$dbfile = 'db.sqlite3';
$db=null;
require_once(DINC.'functions.php');
require_once(DINC.'db.php');
require_once(DINC.'users.php');

if (isset($_GET['id']))
	$id=$_GET['id'];
else
	$id='witam';

include_once(DINC.'template.php');

?>
localhost/~kl2ag1/phpapp/index.php
/home/kl2ag1/gitrepo1a/public_html/phpapp/inc
inc/
public_html

