from django import forms
from . import models
from .models import Event, Update


class CreateEvent(forms.ModelForm):
    event_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Event Name',
        'name': 'event_name',
        'id': 'id_event_name',
    }))
    slug = forms.SlugField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Dont Enter Anythin here!',
        'name': 'slug',
        'id': 'id_slug',
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'type': 'time',
    }))
    location = forms.CharField(max_length=21, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location of the event in college',
    }))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Description'
    }))
    reg = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Link for Registration'
    }))
    orgzer = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Organizer of the Event'
    }))
    # poster = forms.ImageField(required=False, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'file'
    # }))
    # winners = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'form-control',
    #     'placeholder': 'Winners of the event (only to be update once '
    # }))

    class Meta:

        model = models.Event
        fields = ['event_name', 'slug', 'date', 'time', 'location',
                  'reg', 'description', 'orgzer']


class CreateUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name of announcement'
    }))
    Update = forms.CharField(max_length=250, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Body of announcement'
    }))
    till_when = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
        'placeholder': 'Date of Event',
    }))

    class Meta:
        model = models.Update
        fields = ['title', 'till_when', 'Update']
        help_texts = {
            'till_when': ('yyyy:mm:dd'),
        }


# class GalleryForm(forms.ModelForm):
#     class Meta:
#         model = Gallery
#         fields = ['image']


class UpdateBlogPostForm(forms.ModelForm):
    event_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Event Name',
        'name': 'event_name',
        'id': 'id_event_name',
    }))
    slug = forms.SlugField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Dont Enter Anythin here!',
        'name': 'slug',
        'id': 'id_slug',
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'type': 'time',
    }))
    location = forms.CharField(max_length=21, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location of the event in college',
    }))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Description'
    }))
    reg = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Link for Registration'
    }))
    orgzer = forms.CharField(max_length=40, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Organizer of the Event'
    }))
    # poster = forms.ImageField(required=False, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'file'
    # }))
    winners = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'Placeholer': 'Enter the winners if decided'
    }))

    class Meta:
        model = Event
        fields = ['event_name',  'date', 'time', 'location', 'slug',
                  'reg', 'description', 'orgzer', 'winners']

    def save(self, commit=True):
        event = self.instance
        event.event_name = self.cleaned_data['event_name']
        event.date = self.cleaned_data['date']
        event.time = self.cleaned_data['time']
        event.location = self.cleaned_data['location']
        event.reg = self.cleaned_data['reg']
        event.description = self.cleaned_data['description']
        event.winners = self.cleaned_data['winners']
        event.orgzer = self.cleaned_data['orgzer']
        event.slug = self.cleaned_data['slug']

        # if self.cleaned_data['poster']:
        #     event.poster = self.cleaned_data['poster']
        if commit:
            event.save()
        return event
