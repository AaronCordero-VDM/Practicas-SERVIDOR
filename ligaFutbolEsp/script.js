$(inicio);

function inicio(){
    $("#getEqipos").click(function(){
        $.get("equipos.py",
            function(data,status){
                console.log(data)

                let equipos = data.equipos;

                $("#equiposSel").empty();
                for(let i = 0; i<equipos.length; i++){
                    let option = $("<option>").text(equipos[i])
                    $("#equiposSel").append(option)
                }
            }
        )
    })
    $("#getInfo").click(function() {
        let equipo = $("#equiposSel").val();
        $.get("infoEquipos.py", { equipo: equipo }, function(data, status) {
            console.log(data);
            $("#tabla").empty();

            let datosEquipo = data;
            for (dato in datosEquipo){
                let fila = $("<tr>");
                let key = $("<td>").text(dato);
                let value = $("<td>").text(datosEquipo[dato]);
                fila.append(key,value);
                $("#tabla").append(fila);
            }

            // Aquí puedes realizar cualquier otra operación con los datos obtenidos
        });
    });
    
}