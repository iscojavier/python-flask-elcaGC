
    $(document).ready(function() {
        $('.editar-btn').click(function() {
            // Lógica para cargar los datos en el modal
                var row = $(this).closest('tr'); // Encuentra la fila más cercana al botón "Editar"
                var nombre = row.find('td:eq(0)').text(); // Obtiene el texto del primer td (el ID del usuario)
                var apellido = row.find('td:eq(1)').text(); // Obtiene el texto del segundo td (el nombre del usuario)
                var rut = row.find('td:eq(2)').text(); // Obtiene el texto del tercer td (el email del usuario)
                var marca = row.find('td:eq(3)').text(); // Obtiene el texto del tercer td (el email del usuario)
                var modelo = row.find('td:eq(4)').text(); // Obtiene el texto del tercer td (el email del usuario)
                var serie = row.find('td:eq(5)').text(); // Obtiene el texto del tercer td (el email del usuario)

            
                // Lógica para actualizar el modal con los datos obtenidos
                $('#editForm').attr('action', '/editar/' + serie); // Actualiza la acción del formulario con la URL de edición del usuario
                $('#nombre').val(nombre); // Actualiza el valor del campo "nombre" en el formulario con el nombre del usuario
                $('#apellido').val(apellido); // Actualiza el valor del campo "email" en el formulario con el email del usuario
                $('#rut').val(rut); // Actualiza el valor del campo "email" en el formulario con el email del usuario
                $('#marca').val(marca); // Actualiza el valor del campo "email" en el formulario con el email del usuario
                $('#modelo').val(modelo); // Actualiza el valor del campo "email" en el formulario con el email del usuario
                $('#serie').val(serie); // Actualiza el valor del campo "email" en el formulario con el email del usuario

            });
        

        });
