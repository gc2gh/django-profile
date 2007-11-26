from django import newforms as forms
from django.core.exceptions import ObjectDoesNotExist
from profile.models import Profile, Avatar

def ProfileForm(request):
    """
    Profile Form. Composed by all the Profile model fields.
    """
    user = request.user
    profile,created = Profile.objects.get_or_create(user=user)

    ProfileEdit = forms.form_for_instance(profile)
    del ProfileEdit.base_fields['user']
    ProfileEdit.base_fields['birthdate'].initial = profile.birthdate.strftime("%Y-%m-%d")
    if request.method == "POST":
        form = ProfileEdit(request.POST, request.FILES)
    else:
        form = ProfileEdit()

    return form

class AvatarForm(forms.Form):
    """
    The avatar form requires only one image field.
    """
    photo = forms.ImageField()
