from kivy.app import App


class MyApplication(App):
    pass


"""
The KV file has to be in the same dirrectory.
The KV file has to have the same name as your App Class (strip 'App' from its name).
The kv file name has to be lowercase.
"""

if __name__ == '__main__':
    MyApplication().run()