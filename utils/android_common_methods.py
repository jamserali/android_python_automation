
class CommonMethods:

    @staticmethod
    def get_android_keycodes():
        return {
            # Text input
            "KEYCODE_A": 29,
            "KEYCODE_B": 30,
            "KEYCODE_C": 31,
            "KEYCODE_D": 32,
            "KEYCODE_E": 33,
            "KEYCODE_DEL": 67,  # Backspace
            "KEYCODE_ENTER": 66,
            "KEYCODE_SPACE": 62,

            # Navigation
            "KEYCODE_HOME": 3,
            "KEYCODE_BACK": 4,
            "KEYCODE_MENU": 82,
            "KEYCODE_APP_SWITCH": 187,
            "KEYCODE_DPAD_UP": 19,
            "KEYCODE_DPAD_DOWN": 20,
            "KEYCODE_DPAD_LEFT": 21,
            "KEYCODE_DPAD_RIGHT": 22,
            "KEYCODE_DPAD_CENTER": 23,

            # Media controls
            "KEYCODE_VOLUME_UP": 24,
            "KEYCODE_VOLUME_DOWN": 25,
            "KEYCODE_VOLUME_MUTE": 164,
            "KEYCODE_MEDIA_PLAY_PAUSE": 85,
            "KEYCODE_MEDIA_NEXT": 87,
            "KEYCODE_MEDIA_PREVIOUS": 88,

            # Power & lock
            "KEYCODE_POWER": 26,
            "KEYCODE_WAKEUP": 224,
            "KEYCODE_SLEEP": 223,

            # Numbers
            "KEYCODE_0": 7,
            "KEYCODE_1": 8,
            "KEYCODE_2": 9,
            "KEYCODE_3": 10,
            "KEYCODE_4": 11,
            "KEYCODE_5": 12,
            "KEYCODE_6": 13,
            "KEYCODE_7": 14,
            "KEYCODE_8": 15,
            "KEYCODE_9": 16
        }
