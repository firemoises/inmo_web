from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre",required=True, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Moises Diaz'}))

    telefono = forms.CharField(label="Telefono",required=True, widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': '809-123-4567'}))

    correo = forms.EmailField(label="Correo",required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control','placeholder': 'micorreo@gmail.com'}))

    mensaje = forms.CharField(label="Mensaje",required=True,widget=forms.Textarea(
        attrs={'class': 'form-control','placeholder': 'Me interesa ver esta propiedad','rows': '2'}))


    
