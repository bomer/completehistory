<?php
// Recieved Files Class
require_once 'tools.php';

class ReceivedFiles{

	public $dir_name = "My Received Files";


	private $possible_users = [];
	private $possible_chats = [];
	private $lastFrom = "";
	private function showUsers(){
		foreach ($this->possible_users as $key => $value) {
			if($value !="." && $value != "..")
				echo "<a href='?user=$value'>$value</a>";
		}
	}

	//List of users I chatted with
	public function showHistory(){
		if(file_exists('./'. $this->dir_name .'/'. $_GET['user'])){
			echo "Hotmail ID - " . $_GET['user'] . "<br> Let's see what dumb shit you said!<br>";

			$historyPath='./'.$this->dir_name.'/'.$_GET['user'].'/History';
			$this->possible_chats=scandir($historyPath);

			foreach ($this->possible_chats as $key => $value) {
				if(strpos($value, 'xml') > 0){
					$size = round(filesize($historyPath.'/'.$value)/1024,2);
					$this->showPerson($value,$size);
				}
			}
		}

	}

	//Show chat $user had with $person
	public function showChat($user,$person){
		$fullpath = './'. $this->dir_name .'/'. $_GET['user']. '/History/' . $person;
		
		if(file_exists($fullpath)){
			$this->outputWindow();

			$xmldata = file_get_contents($fullpath);
			$xml=simplexml_load_string($xmldata);// or die("Error: Cannot read XML correctly");

			echo "<div class='chatwindow'>";
			foreach ($xml->Message as $key => $message) {
				$this->outputMessage($message);
			}
			echo "</div>";
		}else{
			echo "cannot find chat file";
		}

	}

	//This function outputs the message in a nice format.
	/* Message contains teh following attributes:
      ["@attributes"]=>["Date"],["Time"],["DateTime"],["SessionID"]
 	  ["From"]=>["User"]=>["@attributes"]=>["FriendlyName"]
      ["To"]=>["User"]=>["@attributes"]=> ["FriendlyName"]
      ["Text"]
	*/
	private function outputMessage($msg){
		// prettydump($msg);
		$date =	($msg['Date']);
		$time =	($msg['Time']);
		$from =	($msg->From->User['FriendlyName']);
		$to   =	($msg->To->User['FriendlyName']);
		$text = ($msg->Text);

		// echo "$from  and LASTFROM= $this->lastFrom";
		// if($from != $this->lastFrom)
		if(strcmp($from, $this->lastFrom))
			echo "<p class='from'>$from says: <span class='time'>$date  - $time</span> </p>";
		echo "<p class='text'>$text</p>";

		$this->lastFrom=$from;
	}

	private function outputWindow(){


	}

	private function showPerson($name,$size){
		echo "<a href='?user=".$_GET['user']."&chat=$name'>$name ( $size kb)</a><br>";
	}

	//Prepares the class and see's if u can read my recieved files
	function __construct (){
		
		if(file_exists('./'.$dir_name)){
			echo "Your " . $this->dir_name . " Exists. Let's have some fun! <br>";

			$this->possible_users=scandir('./'.$this->dir_name);
			// prettydump($this->possible_users);
			$this->showUsers();
		}else{
			"Missing " . $this->dir_name;
		}

	}

}
