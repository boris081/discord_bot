class ConfigDefaults:
    token = None
    owner_id = 'auto'
    timeout = 10.0
    dev_ids = set()
    command_prefix = '!'
    debug_mode = False
    debug_level = 'INFO'
    embeds = False
    block_channels = set()
    delete_invoking = False
    delete_messages = True
    consumer_key = None
    consumer_secret = None
    access_token = None
    access_token_secret = None

    key_file = 'json/key.json'
    setting_file = 'json/setting.json'

    db_path = 'db/member.sqlite'
    db_game_table= 'user_id, username, server_id, point'





