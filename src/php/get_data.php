<?php
include('./db_connection.php'); //load config

$result = mysql_query("SELECT * FROM monlog ORDER BY datetime DESC");

$json = [];
while($row = mysql_fetch_assoc($result)){
  $json[] = $row;
}

echo json_encode($json);
//echo ('{"flights":'.json_encode($flights).', "error": {"code": "000","message": "Flüge konnten erfolgreich in der Datenbank gefunden werden."}}');
?>
