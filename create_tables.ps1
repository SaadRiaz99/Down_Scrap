
$dbPath = 'C:\Users\Umair Hayat\Desktop\Umair  Hayat  033  Saad Bin Riaz 035        Karan Kumar 099      naresh kumar 032\HospitalManagement (1).accdb'
try {
    $access = New-Object -ComObject Access.Application
    $access.OpenCurrentDatabase($dbPath)
    $db = $access.CurrentDb()

    # Drop tables if they exist (or rename)
    $tablesToDrop = @('Users', 'Patients')
    foreach ($t in $tablesToDrop) {
        try {
            $db.Execute("DROP TABLE [$t]")
            Write-Host "Dropped existing table $t"
        } catch {}
    }

    # Create Users Table
    $sqlUsers = "CREATE TABLE Users (
        UserID COUNTER PRIMARY KEY,
        FullName VARCHAR(255),
        Email VARCHAR(255),
        PhoneNumber VARCHAR(50),
        Username VARCHAR(50) UNIQUE,
        [Password] VARCHAR(50),
        [Role] VARCHAR(20),
        CreatedAt DATETIME
    );"
    
    # Create Patients Table
    $sqlPatients = "CREATE TABLE Patients (
        PatientID COUNTER PRIMARY KEY,
        UserID INTEGER,
        Age INTEGER,
        Gender VARCHAR(20),
        Address VARCHAR(255),
        BloodGroup VARCHAR(10),
        MedicalHistory MEMO
    );"

    $db.Execute($sqlUsers)
    Write-Host "Created Users table."
    
    $db.Execute($sqlPatients)
    Write-Host "Created Patients table."

    $access.CloseCurrentDatabase()
    $access.Quit()
} catch {
    Write-Host "Error: $($_.Exception.Message)"
}
