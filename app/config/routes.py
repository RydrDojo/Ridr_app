from system.core.router import routes

# GET Routes ===========================================================#

# Users
routes['default_controller'] = 'Users'
routes['/'] = "Users#index"
routes['/login'] = "Users#login"
routes['/logout'] = "Users#logout"
routes['/user/<user_id>'] = "Users#show_user"
routes['/user/inbox'] = "Users#show_inbox"
routes['/oauth-authorized/<resp>'] = "Users#oauth_authorized"

# Events
routes['/events'] = "Events#events"
routes['/event/new'] = "Events#new"
routes['/event/<event_id>'] = "Events#show_event"
routes['/event/new/list/<events>'] = "Events#new_list"
routes['/event/new/create/<event>'] = "Events#new_create"
routes['/event/<event_id>/delete'] = "Events#delete"

# POST Routes ===========================================================#

# Users
routes['/login/process'] = "Users#login_process"

# Events
routes['POST']['/event/new/process'] = "Events#new_process"
routes['POST']['/event/new/list/process'] = "Events#new_list_process"
routes['POST']['/event/new/create/process'] = "Events#new_create_process"
