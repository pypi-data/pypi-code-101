"""Route definitions."""

from pyramid.security import NO_PERMISSION_REQUIRED


# =============================================================================
def includeme(configurator):
    """Function to include routes.

    :type  configurator: pyramid.config.Configurator
    :param configurator:
        Object used to do configuration declaration within the application.
    """
    # Home
    configurator.add_route('home', '/')
    configurator.add_route('favicon', '/favicon.ico')
    configurator.add_route('robots', '/robots.txt')
    configurator.add_view(
        '.views.home.home_view', route_name='home',
        renderer=configurator.get_settings().get('site.home') or
        'chrysalio:Templates/home.pt')

    # Login/logout
    configurator.add_route('login', '/login')
    configurator.add_route('logout', '/logout')
    configurator.add_view(
        '.views.login.login', route_name='login',
        renderer=configurator.get_settings().get('site.login') or
        'chrysalio:Templates/login.pt', permission=NO_PERMISSION_REQUIRED)

    # Modes
    configurator.add_route('mode', '/mode/{mode_id}')

    # Panel
    configurator.add_route('panel_open', '/panel/open/{panel_id}')
    configurator.add_route('panel_close', '/panel/close/{panel_id}')

    # Attachment
    configurator.add_route('attachment', '/attachment/*path')

    # General settings
    configurator.add_route('settings_view', '/settings/view')
    configurator.add_route('settings_edit', '/settings/edit')

    # Backup
    configurator.add_route('backup', '/backup')

    # Profile
    configurator.add_route('profile_index', '/profile/index')
    configurator.add_route('profile_index_filter', '/profile/index/filter')
    configurator.add_route('profile_create', '/profile/create')
    configurator.add_route('profile_edit', '/profile/edit/{profile_id}')
    configurator.add_route('profile_view', '/profile/view/{profile_id}')

    # User
    configurator.add_route('user_index', '/user/index')
    configurator.add_route('user_index_filter', '/user/index/filter')
    configurator.add_route('user_create', '/user/create')
    configurator.add_route('user_edit', '/user/edit/{user_id}')
    configurator.add_route('user_view', '/user/view/{user_id}')
    configurator.add_route('user_account', '/user/account')
    configurator.add_route('user_password_forgot', '/user/password/forgot')
    configurator.add_route(
        'user_password_reset', '/user/password/reset/{user_id}/{token}')

    # Group
    configurator.add_route('group_index', '/group/index')
    configurator.add_route('group_index_filter', '/group/index/filter')
    configurator.add_route('group_create', '/group/create')
    configurator.add_route('group_edit', '/group/edit/{group_id}')
    configurator.add_route('group_view', '/group/view/{group_id}')
