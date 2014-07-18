<?php
	$sock = stream_socket_client("unix:///tmp/socket", $errno, $errstr, 30);

	$read = fread($sock, 10);

	if ($read) {
		echo $read;
	}
?>