<?php
// declare(strict_types=1);

use PHPUnit\Framework\TestCase;
require_once 'lib/recievedfiles.php';

final class RecievedFilesTest extends TestCase
{

    // public static $instance;

    // public static function setUpBeforeClass(){
    //     RecievedFilesTest::$instance = new ReceivedFiles();

    // }

    public function testShowUsers()
    {

        $expected = "chat";

        $RF = new ReceivedFiles();
        // $this->expectOutputString($expected);

        $this->assertEquals((strpos($this->getActualOutput(), 'da_bomer') !== false), true);
        $this->assertEquals((strpos($this->getActualOutput(), 'jimmeyotoole') !== false), true);
        

        // $RF->showHistory();

        // echo($fakestdout);
        // $this->assert();
    }
    public function testBadFolder()
    {

        $expected = "chat";

        chdir("./lib");

        $RF = new ReceivedFiles();        
        

        $this->assertEquals((strpos($this->getActualOutput(), 'Missing') !== false), true);
        

        // $RF->showHistory();

        // echo($fakestdout);
        // $this->assert();
    }

    public function testShowHistory()
    {
        $_GET['user']="da_bomer2413355128";
 
        $expected = "adamthedumbass2788537618";        
        $RF = new ReceivedFiles();        
        $RF->showHistory();
        $this->assertEquals((strpos($this->getActualOutput(), $expected) !== false), true);

    }

    public function testShowChatWithAdam()
    {
        $_GET['user']="da_bomer2413355128";
        $_GET['chat'] = "adamthedumbass2788537618.xml";        
        
        $RF = new ReceivedFiles();        
        $RF->showChat($_GET['user'],$_GET['chat']);
        $expected="im makin a wikkid flash movie";
        $this->assertEquals((strpos($this->getActualOutput(), $expected) !== false), true);
    }

    public function testShowBrokenChat()
    {
        $_GET['user']="da_bomer2413355128";
        $_GET['chat'] = "adamthedumbass2788537618.xml11111123123";        
        
        $RF = new ReceivedFiles();        
        $RF->showChat($_GET['user'],$_GET['chat']);
        $expected="cannot find chat file";
        $this->assertEquals((strpos($this->getActualOutput(), $expected) !== false), true);
    }


    // public function testCannotBeCreatedFromInvalidEmailAddress()
    // {
    //     $this->expectException(InvalidArgumentException::class);

    //     Email::fromString('invalid');
    // }

    // public function testCanBeUsedAsString()
    // {
    //     $this->assertEquals(
    //         'user@example.com',
    //         Email::fromString('user@example.com')
    //     );
    // }
}
