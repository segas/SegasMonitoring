<?php
/**
 * Created by Atom.
 * User: Stefan
 * Date: 15.02.2016
 * Time: 11:26
 */

// Verbindung mit Datenbank aufbauen
// Falls Datenbank nicht erreichbar ist gibt er eine Fehlermeldung aus

header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST,GET,OPTIONS');
header('Access-Control-Allow-Headers: Origin, X-Requested-With, Content-Type, Accept');

$mysql_hostname = "192.168.1.15";
$mysql_user = "monitoring";
$mysql_password = "AzMb3_1$";
$mysql_database = "monitoring";

mysql_connect($mysql_hostname, $mysql_user, $mysql_password) or die("Login error! Code: 001"); // Connect to database server(localhost) with username and password.
mysql_select_db($mysql_database) or die("Login error! Code: 004");
?>
