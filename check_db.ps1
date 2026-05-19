
$dbPath = 'C:\Users\Umair Hayat\Desktop\Umair  Hayat  033  Saad Bin Riaz 035        Karan Kumar 099      naresh kumar 032\HospitalManagement (1).accdb'
try {
    $access = New-Object -ComObject Access.Application
    $access.OpenCurrentDatabase($dbPath)
    $db = $access.CurrentDb()
    Write-Host "Tables in $dbPath :"
    foreach ($table in $db.TableDefs) {
        if ($table.Name -notmatch '^MSys') {
            Write-Host "Table: $($table.Name)"
            # foreach ($field in $table.Fields) {
            #    Write-Host "  $($field.Name) ($($field.Type))"
            # }
        }
    }
    $access.CloseCurrentDatabase()
    $access.Quit()
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}
