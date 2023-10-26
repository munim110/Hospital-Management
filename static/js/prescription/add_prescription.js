document.addEventListener("DOMContentLoaded", function() {
    function handleAddMedicine(){
        var medicineName = document.getElementById("medicine_name").value;
        var medicineQuantity = document.getElementById("medicine_dose").value;
        var medicineDosage = document.getElementById("medicine_duration").value;

    
        table = document.getElementById("medicine_table");
            // Create a new row
        var newRow = table.insertRow();
    
        // Insert new cells and set their innerHTML
        newRow.insertCell(0).innerHTML = medicineName;
        newRow.insertCell(1).innerHTML = medicineQuantity;
        newRow.insertCell(2).innerHTML = medicineDosage;
    };
    var addButton = document.querySelector("#medicine_table input[type='button']");
    if (addButton) {
        addButton.addEventListener("click", handleAddMedicine);
    }
});
