from django import forms
from . import models
from .models import Event, Update


class CreateEvent(forms.ModelForm):
    event_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Event Name',
        'name': 'event_name',
        'id': 'id_event_name',
    }))
    slug = forms.SlugField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'This is an auto completing field!',
        'name': 'slug',
        'title': 'if it doesnt then type the thing on your with hyphens in between spaces',
        'id': 'id_slug',
        'maxlength': '400',
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'type': 'time',
    }))
    location = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location of the event in college',

    }))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Description'
    }))
    reg = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the  Link associated with the Event ',
    }))
    orgzer = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Organizer of the Event',
        'maxlength': '200',
    }))
    remember_link = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ), help_text="Do you want the event link to be display after the event date is over?")
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
                  'reg', 'description', 'orgzer', 'remember_link']


class CreateUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Name of announcement'
    }))
    Update = forms.CharField(max_length=500, widget=forms.Textarea(attrs={
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
    event_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Event Name',
        'name': 'event_name',
        'id': 'id_event_name',
    }))
    slug = forms.SlugField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'This is auto completing field!',
        'title': 'if it doesnt then type the thing on your with hyphens in between spaces',
        'name': 'slug',
        'id': 'id_slug',
        'maxlength': '400',
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    time = forms.TimeField(widget=forms.TimeInput(attrs={
        'class': 'form-control',
        'type': 'time',
    }))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Location of the event in college',
        'maxlength': '100',
    }))
    description = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Description'
    }))
    reg = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter the  Link associated with the Event ',
    }))
    orgzer = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Organizer of the Event',
        'maxlength': '200',
    }))
    # poster = forms.ImageField(required=False, widget=forms.TextInput(attrs={
    #     'class': 'form-control',
    #     'type': 'file'
    # }))
    winners = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'Placeholer': 'Enter the winners if decided'
    }))

    remember_link = forms.BooleanField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-check-input',
            'type': 'checkbox',
        }
    ), help_text="Do you want the event link to be display after the event date is over?")

    class Meta:
        model = Event
        fields = ['event_name',  'date', 'time', 'location', 'slug',
                  'reg', 'description', 'orgzer', 'winners', 'remember_link']

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
