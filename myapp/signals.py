from django.contrib.auth.models import Group, Permission

def create_auth_group(sender, **kwargs):

    #create_group
    readers_group = Group.objects.get_or_create(name='Readers')
    authors_group = Group.objects.get_or_create(name='Readers')
    editors_group = Group.objects.get_or_create(name='Readers')

    #create_permissions
    readers_permission = [
        Permission.objects.get(codename='view_post')
    ]

    authors_permission = [
            Permission.objects.get(codename='view_post'),
            Permission.objects.get(codename='delete_post'),
            Permission.objects.get(codename='add_post')
        ]

    editors_permission = [
                Permission.objects.get(codename='view_post'),
                Permission.objects.get(codename='delete_post'),
                Permission.objects.get(codename='add_post'),
                Permission.objects.get(codename='change_post')
            ]
    