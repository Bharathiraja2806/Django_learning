from django.contrib.auth.models import Group, Permission

def create_auth_group(sender, **kwargs):

    try:
        #create_group
        readers_group, created = Group.objects.get_or_create(name='Readers')
        authors_group, created = Group.objects.get_or_create(name='authors')
        editors_group, created = Group.objects.get_or_create(name='editors')

        #create_permissions
        readers_permission = [
            Permission.objects.get(codename='view_post')
        ]

        authors_permission = [
                Permission.objects.get(codename='view_post'),
                Permission.objects.get(codename='delete_post'),
                Permission.objects.get(codename='add_post')
            ]

        can_publish, created = Permission.objects.get_or_create(codename='can_post', content_type_id = 8 , name= "can publish post")

        editors_permission = [
                    can_publish,
                    Permission.objects.get(codename='delete_post'),
                    Permission.objects.get(codename='add_post'),
                    Permission.objects.get(codename='change_post')
                ]

        #permissions given to groups
        readers_group.permissions.set(readers_permission)
        authors_group.permissions.set(authors_permission)
        editors_group.permissions.set(editors_permission)
        print("Groups and permissions created successfully")
    except Exception as e:
        print(f"An error occured {e}")
    