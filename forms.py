from django import forms

class EquipoForm(forms.Form):
    nombre_equipo = forms.CharField(label="Nom Equipo", required=True)
    nombre_jefe = forms.ChoiceField(
        label="Nombre Jefe",
        required=True,
        choices=[
            ('', 'Seleccione...'),
            ('Juan Manuel Siñani Chavez', 'Juan Manuel Siñani Chavez'),
            ('Sergio Santiago Huanca Lopez', 'Sergio Santiago Huanca Lopez'),
            ('Omar Mamani Clavijo', 'Omar Mamani Clavijo'),
            ('Franklin Cayllagua Mamani', 'Franklin Cayllagua Mamani'),
            ('Heynar Freddy Mamani Quispe', 'Heynar Freddy Mamani Quispe'),
        ]
    )    
    membresia = forms.IntegerField(label="Membresía", required=True)
    cantidad = forms.IntegerField(label="Cantidad", required=True)