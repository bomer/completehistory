<link rel="stylesheet" type="text/css" href="css/style.css">
<?php 

// ini_set('html_errors ', true);

require 'lib/recievedfiles.php';

head();

menu();

// $currentdir = scandir('.');
// prettydump($currentdir); // THis dump shows the current workuing dir, to get started

$RF = new ReceivedFiles();

if(isset($_GET['user']) && isset($_GET['chat'])){
	$RF->showChat($_GET['user'],$_GET['chat']);
}
else if(isset($_GET['user'])){
	$RF->showHistory();
}
?>
