<?php

	$sock = stream_socket_client("unix:///tmp/socket", $errno, $errstr, 30);

	if (isset($_POST['id'])) {
		if (isset($_POST['content'])) {
			fwrite($sock, $_POST['id'].$_POST['content']);
		}else{
			fwrite($sock, $_POST['id']);
		}
	}

	$read = fread($sock, 20);

	//if (!$read) {
		echo $read."this";
	//}
?>
