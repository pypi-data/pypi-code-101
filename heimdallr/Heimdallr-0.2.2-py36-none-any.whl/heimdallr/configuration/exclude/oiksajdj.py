from heimdallr.configuration import heimdallr_settings

heimdallr_settings.set_all_heimdallr_settings(
    mqtt_username="iqgiyzir",
    google_calendar_id="nf1knhum9rdcugt700ah3or09b277gtp@import.calendar.google.com",
    mqtt_access_token="",
    mqtt_password="9b0C2jJFoMxh",
    mqtt_broker="m24.cloudmqtt.com",
    mqtt_port=10915,
)

print(heimdallr_settings.HeimdallrSettings._google_settings_path)

"""
heimdallr -setting_scope multi_set
-mqtt_username="iqgiyzir" -google_calendar_id="nf1knhum9rdcugt700ah3or09b277gtp@import.calendar.google.com" 
-mqtt_access_token="" -mqtt_password="9b0C2jJFoMxh" -mqtt_broker="m24.cloudmqtt.com" -mqtt_port=10915

"""
