<?php
include('./db_connection.php'); //load config

$result = mysql_query("SELECT DISTINCT fk_site FROM monlog ORDER BY fk_site ASC");

echo "hello";

$json = [];
while($row = mysql_fetch_assoc($result)){
  $json[] = $row['fk_site'];
}

echo ('{"fk_sites":'.json_encode($json).', "error": {"code": "000","message": "Hosts konnten erfolgreich in der Datenbank gefunden werden."}}');
?>
