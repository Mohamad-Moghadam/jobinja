USER_PERSMISSION_CLASSES = {

    "Superuser" : [
        "add_superuser", "list_superuser", "add_technicians", "edit_technicians", "delete_technicians", "list_technicians", "retrieve_technicians", "add_entrepreneur", "edit_entrepreneur", "delete_entrepreneur", "list_entrepreneur", "edit_job", "delete_job", "list_job"
    ],

    "Technician" : [
        "add_entrepreneur", "edit_entrepreneur", "delete_entrepreneur", "list_entrepreneur", "edit_job", "delete_job", "list_job"
    ],

    "Entrepreneur" : [
        "add_job", "edit_job", "delete_job", "list_job"
    ]
}