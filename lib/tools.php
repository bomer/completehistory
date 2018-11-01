<?php 

function head(){
	echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
}
function prettydump($v){
	echo "<pre>";
	var_dump($v);
	echo "</pre>";
}

function menu(){
	echo '
	<div>
		<a href="/">Home</a>
	</div>'; 
}
