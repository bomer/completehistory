<?php
// declare(strict_types=1);

use PHPUnit\Framework\TestCase;
require_once 'lib/tools.php';

final class ToolsTest extends TestCase{
	

	public function testHead(){		
		head();
		$this->assertStringNotMatchesFormat("*initial-scale*", $this->getActualOutput());
	}
	public function testMenu(){		
		menu();
		$this->assertStringNotMatchesFormat("*menu*", $this->getActualOutput());
	}
	public function testPrettyDump(){		
		prettydump("hello");
		$this->assertStringNotMatchesFormat("*<pre>*hello*</pre>*", $this->getActualOutput());
	}

}
