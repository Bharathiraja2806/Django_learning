from django.contrib.auth.models import Group, Permission

def create_auth_group(sender, **kwargs):

    #create_group
    readers_group = Group.objects.get_or_create(name='Readers')
    authors_group = Group.objects.get_or_create(name='Readers')
    editors_group = Group.objects.get_or_create(name='Readers')

